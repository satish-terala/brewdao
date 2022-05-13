import pytest
from brownie import BrewDAO, network, accounts

initial_supply = 10000


@pytest.fixture
def brew_dao():
    daoAdmin = accounts[0]
    return BrewDAO.deploy({'from': daoAdmin})

def test_balances_after_deploy_are_in_owner_account(brew_dao):
    daoOwner = accounts[1]
    token_created  = brew_dao.createBrewDAO('ULVA', 'ULVA', initial_supply, daoOwner, True, {'from': accounts[0]})
    print(token_created)
    token_balance = brew_dao.getTokenBalance(daoOwner.address)
    assert token_balance == initial_supply
