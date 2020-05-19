# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    author="Gilles Wetzel",
    author_email='gilles.wetzel@statec.etat.lu',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="OCR box detection",
    include_package_data=True,
    keywords='ocr_box',
    name='ocr_box',
    packages=find_packages(include=['ocr_box', 'ocr_box.*']),
    test_suite='tests',
    url='https://github.com/wetgi/ocr_box',
    version='0.1.0',
    zip_safe=False,
)
