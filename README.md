# OMERO.mapr GraphQL

An experiment in querying [OMERO.mapr](https://github.com/ome/omero-mapr) [IDR](https://idr.openmicroscopy.org/) metadata using GraphQL.

This notebook should be run in the [imagedata/idr-notebooks Docker image](https://hub.docker.com/r/imagedata/idr-notebooks/).


## Flask graphql app

Run:
```
flask run -h 0.0.0.0 -p 5000
```
and go to http://172.17.0.2:5000/graphql in a web browser.
You should see a basic GraphQL IDE.
Example query:
`{ image(id: 1030631) { annotations(mapr: GENE) { name value { name value } } } }`
