import uuid

from datetime import datetime
from aiohttp import web
from db import requests


def generate_attachment(level):
    attachment = {}
    snippet = attachment
    for _ in range(level):
        n = 1
        while n != 0:
            if not snippet:
                snippet['entity'] = {}
                n -= 1
            else:
                snippet = snippet['entity']
    return attachment


async def get_request_data(request):
    response = {}
    attachment_depth = request.match_info['attachment_depth']

    try:
        attachment_depth = int(attachment_depth)
    except ValueError:
        return web.json_response({'error': 'Bad request'})

    response['request_uuid'] = str(uuid.uuid4())
    response['request_date'] = datetime.now().isoformat()
    response['attachment'] = generate_attachment(attachment_depth)

    async with request.app['db'].acquire() as conn:
        ins = requests.insert().values(**response)
        await conn.execute(ins)

    return web.json_response(response)
