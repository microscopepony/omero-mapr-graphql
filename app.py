#!/usr/bin/env python

from os import getenv
# import omero.clients
from omero.gateway import BlitzGateway
from flask import Flask, g
from flask_graphql import GraphQLView
from idr_graphql import schema


def omero_connect():
    conn = BlitzGateway(
        host=getenv('IDR_HOST'),
        username=getenv('IDR_USER'),
        passwd=getenv('IDR_PASSWORD'),
        secure=True)
    r = conn.connect()
    assert r
    return conn


def get_omero_ctx():
    if not hasattr(g, 'omero'):
        print('Connecting to OMERO')
        conn = omero_connect()
        conn.c.enableKeepAlive(60)
        g.omero = dict(conn=conn, qs=conn.getQueryService())
    print('Connected')
    return g.omero


app = Flask(__name__)
app.debug = True
# https://github.com/graphql-python/flask-graphql/issues/52#issuecomment-412773200
app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql', schema=schema, graphiql=True, get_context=get_omero_ctx))


@app.teardown_appcontext
def shutdown_session(exception=None):
    if hasattr(g, 'omero'):
        print(g.omero)
        g.omero['conn'].close()


if __name__ == '__main__':
    conntest = omero_connect()
    conntest.close()
    app.run()
