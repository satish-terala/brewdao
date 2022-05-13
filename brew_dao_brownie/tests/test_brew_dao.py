import pytest
import brownie
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


def test_create_brew_dao_can_only_be_called_by_dao_admin(brew_dao):
    daoOwner = accounts[1]
    some_other_address=accounts[5]
    with brownie.reverts("Only DAO Admin is allowed to call this method"):
        brew_dao.createBrewDAO('ULVA', 'ULVA', initial_supply, daoOwner, True, {'from': some_other_address})


