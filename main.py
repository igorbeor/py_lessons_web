import os

from shortly import Shortly
from werkzeug.middleware.shared_data import SharedDataMiddleware


redis_host = "localhost"
redis_port = 6379
with_static = True

app = Shortly({"redis_host": redis_host, "redis_port": redis_port})
if with_static:
    app.wsgi_app = SharedDataMiddleware(
        app.wsgi_app,
        {"/static": os.path.join(os.path.dirname(__file__), "static")}
    )
