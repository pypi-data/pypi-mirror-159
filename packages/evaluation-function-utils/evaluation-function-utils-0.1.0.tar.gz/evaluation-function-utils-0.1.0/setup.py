# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['evaluation_function_utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'evaluation-function-utils',
    'version': '0.1.0',
    'description': 'Miscellaneous Utilities to be used by LambdaFeedback Evaluation Functions',
    'long_description': '# Evaluation Function Utilities\n\nPython package containing a range of utilities that might be used by some (but not all) evaluation functions on the LambdaFeedback platform. This package is pre-installed on the [BaseEvaluationFunctionLayer](https://github.com/lambda-feedback/BaseEvalutionFunctionLayer), to be utilised by individual functions to carry a range of common tasks:\n\n- Better error reporting\n- Schema checking\n- Input symbols (multiple ways of inputing the same answer)',
    'author': 'RabidSheep55',
    'author_email': 'rabidsheep55@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
