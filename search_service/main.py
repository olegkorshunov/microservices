from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec.extension import FlaskApiSpec

import search_service.models
from search_service.database import Base, engine
from search_service.search.router import blueprint as searc_b
from search_service.search.router import search

Base.metadata.create_all(bind=engine)
app = Flask(__name__)
# http://127.0.0.1:5000/swagger-ui
docs = FlaskApiSpec()
docs.init_app(app)
app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="search service",
            version="v1",
            openapi_version="2.0",
            plugins=[MarshmallowPlugin()],
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",
    }
)


app.register_blueprint(searc_b, url_prefix="/search")


docs.register(search, blueprint="search")

if __name__ == "__main__":
    app.run(debug=True, passthrough_errors=True, use_debugger=False, use_reloader=False)
