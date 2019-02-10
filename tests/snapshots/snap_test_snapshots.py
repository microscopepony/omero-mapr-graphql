# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_image_gene 1'] = {
    'data': {
        'image': {
            'annotations': [
                {
                    '__typename': 'Gene',
                    'name': 'polo'
                }
            ],
            'id': 1030631,
            'name': 'Primary_062 [Well B11 Field #1]'
        }
    }
}

snapshots['test_image_phenotype 1'] = {
    'data': {
        'image': {
            'annotations': [
                {
                    '__typename': 'Phenotype',
                    'name': 'defective cell-cell aggregation'
                }
            ],
            'id': 1030631,
            'name': 'Primary_062 [Well B11 Field #1]'
        }
    }
}

snapshots['test_gene 1'] = {
    'data': {
        'gene': [
            {
                'id': 7123814,
                'images': [
                    {
                        'id': 1839829,
                        'name': 'HT45 [Well C5, Field 2]'
                    },
                    {
                        'id': 1839828,
                        'name': 'HT45 [Well C5, Field 1]'
                    }
                ],
                'name': 'DJC5B'
            }
        ]
    }
}
