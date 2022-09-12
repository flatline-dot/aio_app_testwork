from aiopg import sa
from sqlalchemy import MetaData, Column, Table,  Integer, String, DateTime, JSON

metadata = MetaData()


requests = Table(
    'requests', metadata,

    Column('id', Integer, primary_key=True),
    Column('request_uuid', String(36), nullable=False),
    Column('request_date', DateTime, nullable=False),
    Column('attachment', JSON, nullable=False),
)


async def postgres_connect(app):
    conf = app['config']['postgres']
    engine = await sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port']
    )

    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()
