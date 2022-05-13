// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract BrewToken is ERC20 {

    address tokenIssuer;
    address tokenAdmin;

    /*
    *@dev Create an ERC20 compliant Brew token with brewery name and the symbol.
    * _tokenOwner cannot be a 0 address.
    *
    *
    */

    constructor(uint256 _initialSupply, address _tokenOwner, string memory _breweryName, string memory _brewerySymbol) ERC20(_breweryName, _brewerySymbol) {
        tokenIssuer = _tokenOwner;
        tokenAdmin = msg.sender;
        _mint(_tokenOwner, _initialSupply);
    }
}
