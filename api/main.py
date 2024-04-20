from fastapi import FastAPI


app = FastAPI()



@app.get("/")
def ping_pong():
    print('pong')
    return 'ok'



