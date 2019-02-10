# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_dataset 1'] = {
    'data': {
        'dataset': {
            'id': 369,
            'images': [
                {
                    'id': 1920093,
                    'name': 'Bazla-14-100-brain - 2015-06-19 23.34.11.ndpi [Series 1]'
                },
                {
                    'id': 1920094,
                    'name': 'Bazla-14-100-brain - 2015-06-19 23.34.11.ndpi [Series 2]'
                },
                {
                    'id': 1920095,
                    'name': 'Bazla-14-100-brain - 2015-06-19 23.34.11.ndpi [Series 3]'
                }
            ],
            'name': 'Baz1a-14-100-brain',
            'projects': [
                {
                    'id': 101,
                    'name': 'idr0018-neff-histopathology/experimentA'
                }
            ]
        }
    }
}

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

snapshots['test_image_dataset 1'] = {
    'data': {
        'image': {
            'datasets': [
                {
                    'id': 369,
                    'name': 'Baz1a-14-100-brain'
                }
            ],
            'id': 1920095,
            'name': 'Bazla-14-100-brain - 2015-06-19 23.34.11.ndpi [Series 3]'
        }
    }
}

snapshots['test_project 1'] = {
    'data': {
        'project': {
            'datasets': [
                {
                    'id': 408,
                    'name': 'Colocalising'
                },
                {
                    'id': 407,
                    'name': 'Genomic separation 100kb'
                },
                {
                    'id': 401,
                    'name': 'Genomic separation 25kb'
                },
                {
                    'id': 402,
                    'name': 'Genomic separation 42kb'
                },
                {
                    'id': 403,
                    'name': 'Genomic separation 51kb'
                },
                {
                    'id': 404,
                    'name': 'Genomic separation 64kb'
                },
                {
                    'id': 405,
                    'name': 'Genomic separation 70kb'
                },
                {
                    'id': 406,
                    'name': 'Genomic separation 71kb'
                }
            ],
            'id': 151,
            'name': 'idr0027-dickerson-chromatin/experimentA'
        }
    }
}
