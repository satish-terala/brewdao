import logging

from fastapi import APIRouter

from brew_dao_py.src.app import get_account, BROWNIE_PROJECT_REFERENCE

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/contracts/deploy/brewdao')
async def deploy_brew_dao():
    deployer_account = get_account()
    contract = BROWNIE_PROJECT_REFERENCE.BrewDAO.deploy({'from': deployer_account})


@router.get('/contracts/brewdao/create_tokens')
async def create_tokens(brewery_name: str, brewery_symbol: str, init_supply: int, daoOwner: str, create_tokens: bool):
    contract = BROWNIE_PROJECT_REFERENCE.BrewDAO[0]
    deployer_account = get_account()
    token_created = contract.createBrewDAO(brewery_name, brewery_symbol, init_supply, daoOwner, create_tokens,
                                           {'from': deployer_account})
