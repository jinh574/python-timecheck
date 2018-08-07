# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


requirements = [
]

setup(
    name='timecheck',
    version='0.1.0',
    license='MIT',
    author='Jeeseung Han',
    author_email='jinh574@naver.com',
    url='https://hashbox.github.io',
    description='Check elapsed time',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[],
)
