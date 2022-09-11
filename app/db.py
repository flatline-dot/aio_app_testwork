from sqlalchemy import MetaData, Column, Table,  Integer, String, Date, JSON

metadata = MetaData()


requests = Table(
    'requests', metadata,

    Column('id', Integer, primary_key=True),
    Column('request_uuid', String(36), nullable=False),
    Column('request_date', Date, nullable=False),
    Column('attachment', JSON, nullable=False),
)
