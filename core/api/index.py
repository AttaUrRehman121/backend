import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from core.asgi import application as app  # 👈 Vercel needs `app` or `handler`

handlers = {
    "http": app,
    "websocket": app,
    "lifespan": app,
}