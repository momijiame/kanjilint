#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil
import tempfile

import click

from kanjilint import api
from kanjilint import util


@click.group()
def cmd():
    pass


def _dir_files(directory):
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            yield os.path.join(dirpath, filename)


def _filepathes(path):
    is_directory = os.path.isdir(path)
    filepathes = _dir_files(path) if is_directory else [path]

    return filepathes


def _map_text(callback, filepathes):
    for filepath in filepathes:
        text, encoding = util.read(filepath)
        if encoding is None:
            # おそらくバイナリファイル
            continue
        callback(text, filepath, encoding)


@cmd.command()
@click.argument('path', type=click.Path())
def detect(path):
    filepathes = _filepathes(path)
    _map_text(_detect, filepathes)


def _detect(text, filepath, _encoding):
    violations = api.detect(text)
    for violation in violations:
        msg = u'{filename}:{lineno}:{pos}:{line}'.format(
            filename=os.path.relpath(filepath),
            lineno=violation.lineno,
            pos=violation.position,
            line=violation.line,
        )
        click.echo(msg)


@cmd.command()
@click.argument('path', type=click.Path())
def replace(path):
    filepathes = _filepathes(path)
    _map_text(_replace, filepathes)


def _replace(text, filepath, encoding):
    # FIXME: ファイルごとに一時ディレクトリを作るのは効率が悪すぎる
    temp_dirpath = tempfile.mkdtemp()

    try:
        shutil.copy(filepath, temp_dirpath)
        filename = os.path.basename(filepath)
        temp_filepath = os.path.join(temp_dirpath, filename)
        encoding = util.get_encoding(temp_filepath)

        replaced_text = api.replace(text)
        util.write(temp_filepath, replaced_text, encoding)

        os.rename(temp_filepath, filepath)
    finally:
        shutil.rmtree(temp_dirpath, ignore_errors=True)


def main():
    cmd()


if __name__ == '__main__':
    sys.exit(main())
