from views import get_request_data


def setup_routes(app):
    app.router.add_get('/{attachment_depth}', get_request_data)
