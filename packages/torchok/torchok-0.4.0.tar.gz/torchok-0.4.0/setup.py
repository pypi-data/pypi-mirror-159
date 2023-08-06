# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torchok',
 'torchok.callbacks',
 'torchok.constructor',
 'torchok.data',
 'torchok.data.datasets',
 'torchok.data.datasets.classification',
 'torchok.data.datasets.detection',
 'torchok.data.datasets.examples',
 'torchok.data.datasets.representation',
 'torchok.data.datasets.segmentation',
 'torchok.data.transforms',
 'torchok.losses',
 'torchok.losses.common',
 'torchok.losses.representation',
 'torchok.losses.segmentation',
 'torchok.metrics',
 'torchok.models',
 'torchok.models.backbones',
 'torchok.models.backbones.utils',
 'torchok.models.heads',
 'torchok.models.heads.classification',
 'torchok.models.heads.detection',
 'torchok.models.heads.representation',
 'torchok.models.heads.segmentation',
 'torchok.models.modules',
 'torchok.models.modules.blocks',
 'torchok.models.modules.bricks',
 'torchok.models.necks',
 'torchok.models.necks.classification',
 'torchok.models.necks.detection',
 'torchok.models.necks.segmentation',
 'torchok.models.poolings',
 'torchok.models.poolings.classification',
 'torchok.models.poolings.representation',
 'torchok.optim',
 'torchok.optim.optimizers',
 'torchok.optim.schedulers',
 'torchok.tasks']

package_data = \
{'': ['*']}

install_requires = \
['albumentations>=1.2,<1.3',
 'boto3>=1.24,<1.25',
 'faiss>=1.5,<1.6',
 'hydra-core>=1.2,<1.3',
 'mlflow>=1.22,<1.23',
 'numpy>=1.22,<1.23',
 'onnx>=1.12,<1.13',
 'onnxruntime-gpu>=1.11,<1.12',
 'opencv-python>=4.6,<4.7',
 'pandas>=1.4,<1.5',
 'pillow>=9.1,<9.2',
 'pytorch-lightning>=1.6,<1.7',
 'ranx>=0.2,<0.3',
 'torchmetrics>=0.8,<0.9']

setup_kwargs = {
    'name': 'torchok',
    'version': '0.4.0',
    'description': 'The toolkit for fast Deep Learning experiments in Computer Vision',
    'long_description': None,
    'author': 'Vlad Vinogradov',
    'author_email': 'vladt9@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
