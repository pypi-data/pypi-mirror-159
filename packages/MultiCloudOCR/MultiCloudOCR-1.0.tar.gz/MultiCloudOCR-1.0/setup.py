#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# DevVersion: Python3.6.8
# Date: 2020-09-25 09:13
# PyCharm|setup

from setuptools import (setup, find_packages)

setup(
    # 包名
    name="MultiCloudOCR",
    # 版本
    version="1.0",
    description="This is a package to use different OCR model, including Ali, Baidu, etc.",
    # github地址[我学习的样例地址]
    url='https://github.com/snowroll/python-sdk.git',
    # 包的解释地址
    long_description=open('ReadMe.md', encoding='utf-8').read(),
    # 需要包含的子包列表
    packages=find_packages()
)
'''
name 包的名字
version 依赖关系很重要
packages 需要包含的子包列表，用find_packages()查找
url：包的链接，通常为 Github 上的链接，或者是 readthedocs 链接
setup_requires：指定依赖项
test_suite：测试时运行的工具
'''
