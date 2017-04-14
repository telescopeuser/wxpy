#!/usr/bin/env python3
# coding: utf-8

import re
import io

from setuptools import find_packages, setup

with io.open('wxpy/__init__.py', encoding='utf-8') as fp:
    version = re.search(r"__version__\s*=\s*'([\w\-.]+)'", fp.read()).group(1)

with io.open('README.rst', encoding='utf-8') as fp:
    readme = fp.read()

setup(
    name='wxpy',
    version=version,
    packages=find_packages(),
    package_data={
        '': ['*.rst'],
    },
    include_package_data=True,
    entry_points={
            'console_scripts': [
                'wxpy = wxpy.utils:shell_entry'
            ]
        },
    install_requires=[
        'itchat==1.2.32',
        'requests',
    ],
    url='https://github.com/youfou/wxpy',
    license='MIT',
    author='Youfou',
    author_email='youfou@qq.com',
    description='微信机器人 / 优雅的微信个人号API',
    long_description=readme,
    keywords=[
        '微信',
        'WeChat',
        'API'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        'Topic :: Utilities',
    ]
)
