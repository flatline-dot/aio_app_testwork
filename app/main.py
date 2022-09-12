from aiohttp import web
from routes import setup_routes
from settings import config
from db import postgres_connect

app = web.Application()
app['config'] = config
app.cleanup_ctx.append(postgres_connect)
setup_routes(app)
web.run_app(app)
