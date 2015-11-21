#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


def _load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()]


def _install_requires():
    requires = _load_requires_from_file('requirements.txt')
    return requires


def _test_requires():
    test_requires = _load_requires_from_file('test-requirements.txt')
    return test_requires


def main():
    description = 'Japanese kanji lint'

    setup(
        name='kanjilint',
        version='0.0.1',
        description=description,
        long_description=description,
        classifiers=[
            "Development Status :: 1 - Planning",
            "Programming Language :: Python",
            "Intended Audience :: Developers",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
        ],
        author='momijiame',
        author_email='amedama.ginmokusei@gmail.com',
        url='https://github.com/momijiame/kanjilint',
        zip_safe=False,
        include_package_data=True,
        packages=find_packages(),
        install_requires=_install_requires(),
        tests_require=_test_requires(),
        setup_requires=[],
        test_suite='nose.collector',
        entry_points={
            'console_scripts': [
                'kanjilint = kanjilint.cmd.kanjilint_cmd:main',
            ],
        }
    )


if __name__ == '__main__':
    main()
