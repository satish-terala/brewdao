import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.info("Starting the root for the fast api app.")
    return {"message": "Hello World"}


async  def deploy_brew_token(brewery_name:str,brewery_symbol:str,initial_suppy:int):
    pass