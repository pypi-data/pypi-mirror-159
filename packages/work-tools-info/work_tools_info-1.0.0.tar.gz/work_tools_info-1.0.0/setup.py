# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='work_tools_info',  # 包名
    version='1.0.0',  # 版本号
    description='A small example package',
    long_description=long_description,
    author='zack_liu',
    author_email='liu.zhimin.2019@gmail.com',
    url='https://github.com/liuzhimin2019/work_tools.git',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
    ],
)
