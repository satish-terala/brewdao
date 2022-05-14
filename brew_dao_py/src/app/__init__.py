import logging

from brownie import project, accounts, network, config, Wei
from brownie.exceptions import ProjectNotFound
from brownie.network import gas_price
from brownie.network.account import Account
from brownie.network.gas.strategies import LinearScalingStrategy

from brew_dao_py.src.app.settings import setup_logging

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    'development',
    'ganache',
    'hardhat',
    'local-ganache',
    'mainnet-fork',
    'ganache-cli'
]

setup_logging('logging.yaml')
base_gas_fee=875000000
base_gas_strategy  = LinearScalingStrategy(Wei(base_gas_fee), Wei(base_gas_fee*10), 1.1)

logger = logging.getLogger(__name__)
project_path = 'brew_dao_brownie'

logger.info("Loading Brownie Project.")
try:
    BROWNIE_PROJECT_REFERENCE = project.load(project_path, name='BrewDAO')
    BROWNIE_PROJECT_REFERENCE.load_config()
except ProjectNotFound as exception:
    logger.critical(f"Unable to load projects from {project_path} trying another location")
    logger.exception(exception)


def get_account() -> Account:
    """
    Method to return the current deployment account, this is always the 0th account of the account array
    for any testnet or development blockchain.
    :return:
    """
    if network.is_connected() and network.show_active() == 'development':
        logger.info("Already connected to dev network")
        gas_price(base_gas_strategy)
        deployment_account = accounts[0]
        logger.info(f"Deployment account is {deployment_account}")
        return deployment_account
    else:
        logger.info("Connecting to a development network and fetching tokens.")
        network.connect('development', True)
        gas_price(base_gas_strategy)
        deployment_account = accounts[0]
        logger.info(f"Deployment account is {deployment_account}")
        return deployment_account
