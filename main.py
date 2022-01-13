from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    number = 1
    while True:
        data = await ws.receive_json()
        data["ID"] = number
        number += 1
        await ws.send_json(data)
