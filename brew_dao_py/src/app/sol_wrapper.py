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
async def create_tokens(brewery_name: str, brewery_symbol: str, init_supply: int, daoOwner: str,
                        create_tokens: bool) -> str:
    contract = BROWNIE_PROJECT_REFERENCE.BrewDAO[0]
    deployer_account = get_account()
    token_address = contract.createBrewDAO(brewery_name, brewery_symbol, init_supply, daoOwner, create_tokens,
                                           {'from': deployer_account})
    return token_address.return_value

@router.get('/contracts/brewdao/get_token_count')
async def get_token_count(address:str)->int:
    contract = BROWNIE_PROJECT_REFERENCE.BrewDAO[0]
    return contract.getTokenBalance(address)


