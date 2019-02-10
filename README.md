# OMERO.mapr GraphQL

An experiment in querying [OMERO.mapr](https://github.com/ome/omero-mapr) [IDR](https://idr.openmicroscopy.org/) metadata using GraphQL.

This notebook should be run in the [imagedata/idr-notebooks Docker image](https://hub.docker.com/r/imagedata/idr-notebooks/).


## Flask graphql app

Run:
```
flask run
```
and go to http://localhost:5000/graphql in a web browser.
You should see a basic GraphQL IDE.
Example query:
`{ image(id: 1030631) { annotations(mapr: GENE) { name value { name value } } } }`
Pass `-h ADDRESS` or `-p PORT` to listen on a different interface or port.


## Running tests

```
IDR_HOST=idr.openmicroscopy.org IDR_USER=<USER> IDR_PASSWORD=<PASSWORD> pytest
```

[`tests/test_snapshots.py`](tests/test_snapshots.py) makes use of [SnapshotTest](https://github.com/syrusakbary/snapshottest).
Run with `pytest --snapshot-verbose` for more information, or `pytest --snapshot-update` to update the snapshots.
