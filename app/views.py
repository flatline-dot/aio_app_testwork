from aiohttp import web


async def get_request_data(request):
    return web.Response(text='Hello world!')
