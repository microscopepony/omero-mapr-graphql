from graphene.test import Client
from idr_graphql import schema
import json


def equal_dicts(a, b):
    print json.dumps(a, sort_keys=True)
    print json.dumps(b, sort_keys=True)
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def test_image_gene(omero):
    client = Client(schema)
    executed = client.execute("""{
      image(id: 1030631) {
        id
        name
        annotations(mapr: GENE) {
          __typename
          name
        }
      }
    }""", context=omero)
    assert 'error' not in executed
    assert equal_dicts(executed['data'], {
        "image": {
            "id": 1030631,
            "name": "Primary_062 [Well B11 Field #1]",
            "annotations": [{
                "__typename": "Gene",
                "name": "polo"
            }]
        }
    })


def test_image_phenotype(omero):
    client = Client(schema)
    executed = client.execute("""{
      image(id: 1030631) {
        id
        name
        annotations(mapr: PHENOTYPE) {
          __typename
          name
        }
      }
    }""", context=omero)
    assert 'error' not in executed
    assert equal_dicts(executed['data'], {
        "image": {
            "id": 1030631,
            "name": "Primary_062 [Well B11 Field #1]",
            "annotations": [{
                "__typename": "Phenotype",
                "name": "defective cell-cell aggregation"
            }]
        }
    })


def test_gene(omero):
    client = Client(schema)
    executed = client.execute("""{
      gene(key: "Gene Symbol", value: "djc5b") {
        id
        name
        images {
          id
          name
        }
      }
    }""", context=omero)
    assert 'error' not in executed
    assert equal_dicts(executed['data'], {
        "gene": [{
            "id": 7123814,
            "images": [{
                "id": 1839829,
                "name": "HT45 [Well C5, Field 2]"
            }, {
                "id": 1839828,
                "name": "HT45 [Well C5, Field 1]"
            }],
            "name": "DJC5B"
        }]
    })
