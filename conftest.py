import pytest
from os import getenv
from omero.gateway import BlitzGateway


@pytest.fixture
def omero():
    conn = BlitzGateway(
        host=getenv('IDR_HOST'),
        username=getenv('IDR_USER'),
        passwd=getenv('IDR_PASSWORD'),
        secure=True)
    r = conn.connect()
    assert r
    try:
        ctx = dict(conn=conn, qs=conn.getQueryService())
        yield ctx
    finally:
        conn.close()
