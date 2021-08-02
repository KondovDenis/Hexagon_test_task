#!/usr/bin/env python3

import setuptools
from convertor import __version__

setuptools.setup(
    name='leet_test_task_decode',
    version=__version__,
    description='This is a test leet task',
    zip_safe=False,
    include_package_data=True,
    packages=setuptools.find_packages('convertor'),
    entry_points={
        'console_scripts': [
            'leet_test_task_decode=convertor.app:decode'
        ]
    },
)
