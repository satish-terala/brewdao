import logging

from fastapi import APIRouter

from brew_dao_py.src.app import get_account, BROWNIE_PROJECT_REFERENCE

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/contracts/deploy/brewdao')
async def deploy_brew_dao():
    deployer_account = get_account()
    contract = BROWNIE_PROJECT_REFERENCE.BrewDAO.deploy({'from': deployer_account})
