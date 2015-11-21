#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re

from builtins import open
import chardet
from janome.tokenizer import Tokenizer


def read(filepath):
    '''
    マルチバイトを含むテキストファイルを読み込んで文字コードを検出した上でユニコード文字列にして返す
    '''
    with open(filepath, mode='rb') as file_:
        binary = file_.read()
        encoding = _get_encoding(binary)
        if encoding is None:
            return None, None
        text = binary.decode(encoding)
        return text, encoding


def write(filepath, text, encoding):
    '''
    ユニコード文字列を指定されたエンコーディングで書き込む
    '''
    binary = text.encode(encoding)
    with open(filepath, mode='wb') as file_:
        file_.write(binary)


def get_encoding(filepath):
    '''
    テキストファイルのエンコーディングを検出する
    '''
    with open(filepath, mode='rb') as file_:
        binary = file_.read()
        encoding = _get_encoding(binary)
        return encoding


def _get_encoding(binary):
    # いくつかの文字コードに当たりをつけて総当りで調べる
    encoding = _get_encoding_brute_force(binary)
    if encoding is not None:
        return encoding

    # 文字コード検出ライブラリを使ってちゃんと調べる
    encoding = _get_encoding_chardet(binary)
    if encoding is not None:
        return encoding

    # それでも分からなかったらお手上げ (きっとバイナリ)
    return None


def _get_encoding_brute_force(binary):
    encodings = [
        'ascii',
        'utf-8',
        'euc-jp',
        'cp932',
        'iso-2022-jp',
    ]

    for encoding in encodings:
        try:
            binary.decode(encoding)
        except UnicodeDecodeError:
            continue
        return encoding

    return None


def _get_encoding_chardet(binary):
    encoding_info = chardet.detect(binary)
    encoding = encoding_info.get('encoding')
    return encoding


_KANJI_PATTERN = re.compile('[々〇〻\u3220-\u3244\u3280-\u32B0\u3400-\u9FFF\uF900-\uFAFF\u20000-\u2FFFF]')  # noqa


def is_kanji(char):
    return _KANJI_PATTERN.match(char) is not None


_TOKENIZER = Tokenizer()


def tokenize(text):
    return [token.surface for token in _TOKENIZER.tokenize(text)]
