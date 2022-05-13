// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Token.sol";

interface BrewDAOInterface {
}

contract BrewDAO is BrewDAOInterface {

    address daoAdmin;
    string breweryName;
    string brewerySymbol;
    address breweryOwner;
    BrewToken token;

    event BrewDAOCreated(address indexed _breweryOwnerAddress, address indexed _breweryAdminAddress, string indexed _brewerySymbol);

    constructor(){
        daoAdmin = msg.sender;
    }


    function createBrewDAO(string calldata _breweryName, string calldata _brewerySymbol, uint _initialSupply, address _ownerAddress, bool _createTokens) public onlyDaoAdmin returns (bool){
        breweryName = _breweryName;
        brewerySymbol = _brewerySymbol;
        breweryOwner = _ownerAddress;
        if (_createTokens) {
            token = new BrewToken(_initialSupply, _ownerAddress, _breweryName, _brewerySymbol);
        }
        emit BrewDAOCreated(_ownerAddress, daoAdmin, _brewerySymbol);
        return true;
    }


    function getTokenBalance(address _inAddress) public view returns (uint){
        return token.balanceOf(_inAddress);
    }



    modifier onlyDaoAdmin(){
        require(msg.sender == daoAdmin, "Only DAO Admin is allowed to call this method");
        _;
    }
}
