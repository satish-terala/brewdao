import logging

from brownie import project, accounts, network, config
from brownie.exceptions import ProjectNotFound

from brew_dao_py.src.app.settings import setup_logging

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    'development',
    'ganache',
    'hardhat',
    'local-ganache',
    'mainnet-fork'
]

setup_logging('logging.yaml')

logger = logging.getLogger(__name__)
project_path = 'brew_dao_brownie'

logger.info("Loading Brownie Project.")
try:
    BROWNIE_PROJECT_REFERENCE = project.load(project_path, name='BrewDAO')
    BROWNIE_PROJECT_REFERENCE.load_config()
except ProjectNotFound as exception:
    logger.critical(f"Unable to load projects from {project_path} trying another location")
    logger.exception(exception)

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    if network.show_active() in config['networks']:
        return accounts.add(config['wallets']['from_key'])
    return None
