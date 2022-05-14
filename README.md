# brewdao

Installation and local env setup.

Pre-req

1. Python 3.8 or above on your machine.
2. Install hardhat - follow the instructions on the [hardhat site](https://hardhat.org/getting-started/#installation). If you dont install hardhat, the app starts ganache-cli and will run but we are supposed to use hardhat though. 

3. Clone the git repo locally.
4. Install Poetry , instructions [here](https://python-poetry.org/docs/#installation).
5. Inside the folder brewdao, run poetry shell, this should open new virtual env within that folder.
6. Run poetry install to install all required python dependencies listed in pyprojec.toml
7. The top level folder brewdao, has two sub folders - one for the solidity contracts and other for the python wrapper
   that exposes it as a REST endpoint.
8. Running the Python REST application, will load the other project, compile the solidity files and connect your app to
   the local block chain such as ganache-cli (the default)
9. To run the app, from the top level folder on a terminal window run
   - `python -m uvicorn brew_dao_py.src.app.main:app --reload`
10. To access the app go to `http://localhost:8000/docs` , you should see the REST API end points.
