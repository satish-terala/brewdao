import brownie
import pytest
from brownie import BrewDAO, accounts, Wei
from brownie.network.gas.strategies import LinearScalingStrategy

initial_supply = 10000

base_gas_price  = LinearScalingStrategy(Wei(17597082), Wei(17597082*10), 1.1)

@pytest.fixture
def brew_dao():

    daoAdmin = accounts[0]
    return BrewDAO.deploy({'from': daoAdmin, "gas_price": base_gas_price})


def test_balances_after_deploy_are_in_owner_account(brew_dao):
    daoOwner = accounts[1]
    token_created = brew_dao.createBrewDAO('ULVA', 'ULVA', initial_supply, daoOwner, True,
                                           {'from': accounts[0], "gas_price": base_gas_price})
    print(token_created)
    token_balance = brew_dao.getTokenBalance(daoOwner.address)
    assert token_balance == initial_supply


def test_create_brew_dao_can_only_be_called_by_dao_admin(brew_dao):
    daoOwner = accounts[1]
    some_other_address = accounts[5]
    with brownie.reverts("Only DAO Admin is allowed to call this method"):
        brew_dao.createBrewDAO('ULVA', 'ULVA', initial_supply, daoOwner, True,
                               {'from': some_other_address, 'gas_price': base_gas_price})
