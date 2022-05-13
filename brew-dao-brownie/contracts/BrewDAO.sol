// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Token.sol";

interface BrewDAOInterface {
}

contract BrewDAO is BrewDAOInterface {

    address daoAdmin;

    constructor(){
        daoAdmin = msg.sender;
    }
}
