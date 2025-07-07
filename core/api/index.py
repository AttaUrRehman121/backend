from core.asgi import application 


app = application

handlers = {
    "http": application,
    "websocket": application,
    "lifespan": application,
}