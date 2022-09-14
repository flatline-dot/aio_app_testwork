import sys
import argparse
import json
import asyncio
import aiohttp

from aiopg.sa import create_engine

from app import settings
from app import db


DCN = 'postgresql://{user}:{password}@{host}:{port}/{database}'.format(**settings.config_init['postgres'])


async def fetch_api(url, session, engine):
    global process_status
    async with session.get(url) as response:
        res = await response.read()
        request_uuid = json.loads(res.decode())['request_uuid']

        async with engine.acquire() as conn:
            s = db.requests.select().where(db.requests.c.request_uuid == request_uuid)
            request_item = await conn.execute(s)
            request = await request_item.first()
            process_status += 1
            print(f'{request.id} - {request_uuid} _______ Выполнено {process_status} из {num_tasks}')


async def main(n, attachment_depth):

    url = f'http://localhost:8080/{attachment_depth}'

    tasks = []

    async with aiohttp.ClientSession() as session:
        async with create_engine(DCN) as engine:
            for i in range(n):
                task = asyncio.create_task(fetch_api(url, session, engine))
                tasks.append(task)
            await asyncio.gather(*tasks)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--n', nargs='?')
    argparser.add_argument('--attachment_depth', nargs='?')

    namespace = argparser.parse_args(sys.argv[1:])

    num_tasks = int(namespace.n)
    process_status = 0

    asyncio.run(main(int(namespace.n), namespace.attachment_depth))
