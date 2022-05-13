# brewdao

Installation and local env setup.

Pre-req

1. Python 3.8 or above on your machine.

2. Checkout the git repo locally.
3. Install Poetry , instructions [here](https://python-poetry.org/docs/#installation).
4. Inside the folder brewdao, run poetry shell, this should open new virtual env within that folder.
5. Run poetry install to install all required python dependencies listed in pyprojec.toml
6. The top level folder brewdao, has two sub folders - one for the solidity contracts and other for the python wrapper
   that exposes it as a REST endpoint.
7. Running the Python REST application, will load the other project, compile the solidity files and connect your app to
   the local block chain such as ganache-cli (the default)
8. To run the app, from the top level folder on a terminal window run
   - `python -m uvicorn brew_dao_py.src.app.main:app --reload`
9. To access the app go to `http://localhost:8000/docs` , you should see the REST API end points.