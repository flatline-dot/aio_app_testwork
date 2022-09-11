from views import get_request_data


def setup_routes(app):
    app.router.add_get('/', get_request_data)
