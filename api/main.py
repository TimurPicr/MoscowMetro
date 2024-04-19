from fastapi import FastAPI

from mod.test_model import mse

app = FastAPI()



@app.get("/")
def ping_pong():
    print('pong')
    return mse()



