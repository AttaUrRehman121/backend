from core.asgi import application as app  # Vercel looks for 'app'


handlers = {
    "http": app,
    "websocket": app,
    "lifespan": app,
}