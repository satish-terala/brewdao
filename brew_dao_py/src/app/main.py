import logging

from fastapi import FastAPI

from brew_dao_py.src.app import sol_wrapper

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(deployer.router)


@app.get("/")
async def root():
    logger.info("Starting the root for the fast api app.")
    return {"message": "Hello World"}

