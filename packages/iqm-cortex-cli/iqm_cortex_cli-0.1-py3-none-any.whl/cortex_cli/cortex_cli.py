# Copyright 2021-2022 IQM client developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Command line interface for interacting with IQM's quantum computers.
"""
import datetime
import json
import logging
import os
import sys
import time
from pathlib import Path

import click

from cortex_cli import __version__
from cortex_cli.auth import (ClientAuthenticationError, login_request,
                             logout_request, refresh_request,
                             time_left_seconds)
from cortex_cli.token_manager import (check_daemon, daemonize_token_manager,
                                      kill_by_pid)

HOME_PATH = str(Path.home())
CONFIG_PATH = f'{HOME_PATH}/.config/iqm-cortex-cli/config.json'
TOKENS_PATH = f'{HOME_PATH}/.cache/iqm-cortex-cli/tokens.json'
BASE_URL = 'https://auth.demo.qc.iqm.fi'
REALM_NAME = 'cortex'
CLIENT_ID = 'iqm_client'
USERNAME = ''
REFRESH_PERIOD = 3*60 # in seconds

class ClickLoggingHandler(logging.Handler):
    """Simple log handler using click's echo function."""
    def __init__(self):
        super().__init__(level=logging.NOTSET)
        self.formatter = logging.Formatter('%(message)s')

    def emit(self, record):
        click.echo(self.format(record))

logger = logging.getLogger('cortex_cli')
logger.addHandler(ClickLoggingHandler())
logger.setLevel(logging.INFO)

def _setLogLevelByVerbosity(verbose: bool) -> int:
    """Sets logger log level to DEBUG if verbose is True, to INFO otherwise.
    Args:
        verbose: whether logging should be verbose (i.e. DEBUG level)
    Returns:
        int: logging level which was set
    """
    if verbose:
        logger.setLevel(logging.DEBUG)
        return logging.DEBUG
    logger.setLevel(logging.INFO)
    return logging.INFO

def _validate_path(ctx: click.Context, param: object, path: str) -> str:
    """Callback for CLI prompt. If needed, confirmation to overwrite is prompted.

    Args:
        ctx: click context
        param: click prompt param object
        path: path provided by user
    Returns:
        str: confirmed and finalized path
    """
    if ctx.obj and param.name in ctx.obj:
        return path
    ctx.obj = { param.name: True }

    # File doesn't exist, no need to confirm overwriting
    if not Path(path).is_file():
        return path

    # File exists, so user must either overwrite or enter a new path
    while True:
        msg = f"{click.style('File at given path already exists. Overwrite?', fg='red')}"
        if click.confirm(msg, default=None):
            return path

        new_path = click.prompt(
            'New file path',
            type=click.Path(dir_okay=False, writable=True))

        if new_path == path:
            continue
        return new_path

@click.group()
@click.version_option(__version__)
def cortex_cli() -> None:
    """Interact with an IQM quantum computer with Cortex CLI."""
    return

@cortex_cli.command()
@click.option(
    '--config-file',
    prompt='Where to save config',
    callback=_validate_path,
    default=CONFIG_PATH,
    type=click.Path(dir_okay=False, writable=True),
    help='Location where the configuration file will be saved.')
@click.option(
    '--tokens-file',
    prompt='Where to save auth tokens',
    callback=_validate_path,
    default=TOKENS_PATH,
    type=click.Path(dir_okay=False, writable=True),
    help='Location where the tokens file will be saved.')
@click.option(
    '--base-url',
    prompt='Base URL of IQM auth server',
    default=BASE_URL,
    help='Base URL of IQM authentication server.')
@click.option(
    '--realm',
    prompt='Realm on IQM auth server',
    default=REALM_NAME,
    help='Name of the realm on the IQM authentication server.')
@click.option(
    '--client-id',
    prompt='Client ID',
    default=CLIENT_ID,
    help='Client ID on the IQM authentication server.')
@click.option(
    '--username',
    prompt='Username (optional)',
    required=False,
    default=USERNAME,
    help='Username. If not provided, it will be asked for at login.')
@click.option('-v', '--verbose', is_flag=True, help='Print extra information.')
def init(config_file, tokens_file, base_url, realm, client_id, username, verbose) -> None: #pylint: disable=too-many-arguments
    """Initialize configuration and authentication."""
    _setLogLevelByVerbosity(verbose)

    path_to_dir = Path(config_file).parent
    config_json = json.dumps({
        'base_url': base_url,
        'realm': realm,
        'client_id': client_id,
        'username': username,
        'tokens_file': tokens_file
    })

    # Tokens file exist, so daemon may be running. Notify user and kill daemon.
    if Path(tokens_file).is_file():
        pid = check_daemon(tokens_file)
        if pid:
            logger.info('Active token manager (PID %s) will be killed.', pid)
            kill_by_pid(pid)

    try:
        path_to_dir.mkdir(parents=True, exist_ok=True)
        with open(Path(config_file), 'w', encoding='UTF-8') as file:
            file.write(config_json)
            logger.debug('Saved configuration file: %s', config_file)
    except OSError as error:
        raise click.ClickException(f'Error writing configuration file, {error}') from error

    logger.info("Cortex CLI initialized successfully. Login and start the token manager with 'cortex auth login'.")


@cortex_cli.group()
def auth() -> None:
    """Manage authentication."""
    return

@auth.command()
@click.option(
    '--config-file',
    default=CONFIG_PATH,
    type=click.Path(exists=True, dir_okay=False),
    help='Location of the configuration file to be used.')
@click.option('-v', '--verbose', is_flag=True, help='Print extra information.')
def status(config_file, verbose) -> None:
    """Check status of authentication."""
    _setLogLevelByVerbosity(verbose)

    logger.debug('Using configuration file: %s', config_file)
    config = _read_json(config_file)
    tokens_file = config['tokens_file']
    if not Path(tokens_file).is_file():
        raise click.ClickException(f'Tokens file not found: {tokens_file}')

    tokens_data = _read_json(tokens_file)

    click.echo(f'Tokens file: {tokens_file}')
    if not 'pid' in tokens_data:
        click.echo("Tokens file doesn't contain PID. Probably, 'cortex auth login' was launched with '--no-daemon'\n")

    click.echo(f"Last refresh: {tokens_data['timestamp']}")
    seconds_at = time_left_seconds(tokens_data['access_token'])
    time_left_at = str(datetime.timedelta(seconds=seconds_at))
    click.echo(f'Time left on access token (hh:mm:ss): {time_left_at}')
    seconds_rt = time_left_seconds(tokens_data['refresh_token'])
    time_left_rt = str(datetime.timedelta(seconds=seconds_rt))
    click.echo(f'Time left on refresh token (hh:mm:ss): {time_left_rt}')

    active_pid = check_daemon(tokens_file)
    if active_pid:
        click.echo(f'Token manager: {click.style("RUNNING", fg="green")} (PID {active_pid})')
    else:
        click.echo(f'Token manager: {click.style("NOT RUNNING", fg="red")}')

@auth.command()
@click.option(
    '--config-file',
    default=CONFIG_PATH,
    type=click.Path(exists=True, dir_okay=False),
    help='Location of the configuration file to be used.')
@click.option('--username', help='Username for authentication.')
@click.option('--password', help='Password for authentication.')
@click.option('--refresh-period', default=REFRESH_PERIOD, help='How often to reresh tokens (in seconds).')
@click.option('--no-daemon', is_flag=True, default=False, help='Do not start token manager to refresh tokens.')
@click.option('-v', '--verbose', is_flag=True, help='Print extra information.')
def login(config_file, username, password, refresh_period, no_daemon, verbose) -> None: #pylint: disable=too-many-arguments
    """Authenticate on the IQM server."""
    _setLogLevelByVerbosity(verbose)

    config = _read_json(config_file)
    base_url, realm, client_id = config['base_url'], config['realm'], config['client_id']
    tokens_file = config['tokens_file']

    if Path(tokens_file).is_file():
        if check_daemon(tokens_file):
            logger.info("Login aborted, because token manager is already running. See 'cortex auth status'.")
            return

        # Tokens file exists; Refresh tokens without username/password
        refresh_token = _read_json(tokens_file)['refresh_token']
        logger.debug('Attempting to refresh tokens by using existing refresh token from file: %s', tokens_file)

        new_tokens = None
        try:
            new_tokens = refresh_request(base_url, realm, client_id, refresh_token)
        except ClientAuthenticationError:
            logger.info('Failed to refresh tokens by using existing token. Switching to username/password.')

        if new_tokens:
            save_tokens_file(tokens_file, new_tokens, base_url)
            logger.debug('Saved new tokens file: %s', tokens_file)
            if no_daemon:
                logger.info('Existing token was used to refresh session. Token manager not started.')
            else:
                logger.info('Existing token was used to refresh the auth session. Token manager started.')
                daemonize_token_manager(refresh_period, config)
            return

    # Login with username and password
    username = username or config['username'] or click.prompt('Username')
    if config['username']:
        click.echo(f'Username: {username}')
    password = password or click.prompt('Password', hide_input=True)

    try:
        tokens = login_request(base_url, realm, client_id, username, password)
    except ClientAuthenticationError as error:
        raise click.ClickException('Invalid username and/or password') from error

    logger.info('Logged in successfully as %s', username)
    save_tokens_file(tokens_file, tokens, base_url)
    click.echo(f"""To use the tokens file with IQM Client or IQM Client-based software, set the environment variable:
export IQM_TOKENS_FILE={tokens_file}
Refer to IQM Client documentation for details: https://iqm-finland.github.io/iqm-client/""")

    if no_daemon:
        logger.info('Token manager not started.')
    else:
        daemonize_token_manager(refresh_period, config)
        logger.info('Token manager started.')

@auth.command()
@click.option(
    '--config-file',
    type=click.Path(exists=True, dir_okay=False),
    default=CONFIG_PATH)
@click.option(
    '--keep-tokens',
    is_flag=True, default=False,
    help="Don't delete tokens file, but kill token manager daemon.")
@click.option('-f', '--force', is_flag=True, default=False, help="Don't ask for confirmation.")
def logout(config_file, keep_tokens, force) -> None:
    """Either logout completely, or just stop token manager while keeping tokens file."""
    config = _read_json(config_file)
    base_url, realm, client_id = config['base_url'], config['realm'], config['client_id']
    tokens_file = config['tokens_file']

    tokens = _read_json(tokens_file)
    pid = tokens['pid'] if 'pid' in tokens else None
    refresh_token = tokens['refresh_token']

    extra_msg = ' and kill token manager' if check_daemon(tokens_file) else ''

    if keep_tokens and not check_daemon(tokens_file):
        click.echo('Token manager is not running, and you chose to keep tokens. Nothing to do, exiting.')
        return

    # 1. Keep tokens, kill daemon
    if keep_tokens and pid:
        if force or click.confirm(f'Keep tokens file{extra_msg}. OK?', default=None):
            kill_by_pid(pid)
            return

    # 2. Keep tokens, do nothing
    if keep_tokens and not pid:
        logger.info('No PID found in tokens file. Token manager is not running, so tokens may be stale.')

    # 3. Delete tokens, perform logout, kill daemon
    if not keep_tokens and pid:
        if force or click.confirm(f'Logout from server, delete tokens{extra_msg}. OK?', default=None):
            try:
                logout_request(base_url, realm, client_id, refresh_token)
            except ClientAuthenticationError as error:
                raise click.ClickException(f'Error when logging out: {error}') from error
            kill_by_pid(pid)
            os.remove(tokens_file)
            logger.info('Logged out successfully.')
            return

    # 4. Delete tokens, perform logout
    if not keep_tokens and not pid:
        logger.info('No PID found in tokens file. Token manager daemon is not running, so tokens may be stale.')
        if force or click.confirm('Logout from server and delete tokens. OK?', default=None):
            try:
                logout_request(base_url, realm, client_id, refresh_token)
            except ClientAuthenticationError as error:
                raise click.ClickException(f'Error when logging out: {error}') from error

            os.remove(tokens_file)
            logger.info('Logged out successfully.')
            return

    logger.info('Logout aborted.')

def save_tokens_file(path: str, tokens: dict[str, str], auth_server_url: str) -> None:
    """Saves tokens as JSON file at given path.

    Args:
        path (str): path to the file to write
        access_token(str): authorization access token
        refresh_token(str): authorization refresh token
    Raises:
        OSError: if writing to file fails
    """
    path_to_dir = Path(path).parent
    tokens_data = {
        'timestamp': time.ctime(),
        'access_token': tokens['access_token'],
        'refresh_token': tokens['refresh_token'],
        'auth_server_url': auth_server_url
    }

    try:
        path_to_dir.mkdir(parents=True, exist_ok=True)
        with open(Path(path), 'w', encoding='UTF-8') as file:
            file.write(json.dumps(tokens_data))
    except OSError as error:
        raise click.ClickException(f'Error writing tokens file, {error}') from error


def _read(filename: str) -> str:
    """Opens and reads the given file.

    Args:
        filename (str): name of the file to read
    Returns:
        str: contents of the file
    Raises:
        ClickException: if file is not found
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as error:
        raise click.ClickException(f'File {filename} not found') from error

def _read_json(filename: str) -> dict:
    """Opens and parses the given JSON file.

    Args:
        filename (str): name of the file to read
    Returns:
        dict: object derived from JSON file
    Raises:
        JSONDecodeError: if parsing fails
    """
    try:
        json_data = json.loads(_read(filename))
    except json.decoder.JSONDecodeError as error:
        raise click.ClickException(f'Decoding JSON has failed, {error}') from error
    return json_data


if __name__ == '__main__':
    cortex_cli(sys.argv[1:])  # pylint: disable=too-many-function-args
