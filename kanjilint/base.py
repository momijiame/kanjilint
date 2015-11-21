#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import abc
from collections import namedtuple

from future.utils import with_metaclass

from kanjilint.util import tokenize

'''
「前後で後に」を「前後にあとで」に開く必要があるので単純な置換ではダメ
'''


class Violation(namedtuple('Violation', ['lineno', 'position', 'line'])):

    def __hash__(self):
        return hash(self.lineno) + hash(self.position) + hash(self.line)

    def __eq__(self, other):
        if not isinstance(other, Violation):
            return False

        if self.lineno != other.lineno:
            return False

        if self.position != other.position:
            return False

        if self.line != other.line:
            return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Detector(with_metaclass(abc.ABCMeta)):

    def detect(self, text):
        hit_lines = self.detect_strategy(text)
        return hit_lines

    @abc.abstractproperty
    def detect_strategy(self):
        pass


class SearchStrategy(with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def __call__(self, text):
        pass


class TokenSearchStrategy(SearchStrategy):

    def __init__(self, word, inspectors=None):
        inspectors = inspectors or []

        self.tokens = tokenize(word)
        self.inspectors = inspectors
        self._word = word

    def _is_misdetection(self, line):
        if len(self.inspectors) < 1:
            return False

        for inspector in self.inspectors:
            if inspector.is_misdetection(line):
                return True

        return False

    def _match(self, tokens):
        for index, expect_token in enumerate(self.tokens):
            target_token = tokens[index]
            if target_token != expect_token:
                return False
        return True

    def find(self, tokens):
        for index in range(len(tokens) - len(self.tokens) + 1):
            is_match = self._match(tokens[index:])
            if not is_match:
                continue
            # トークン同士が一致するものが見つかったので場所を返す
            return index
        else:
            # 見つからなかった (break しなかった) ので誤検出として -1 を返す
            return -1

    def __call__(self, text):
        lines = text.split(os.linesep)

        for lineno, line in enumerate(lines, start=1):

            # 先にざっくりと文字列のレベルで一致するか確認しておく
            position = line.find(self._word)
            if position == -1:
                continue

            # それっぽいものが見つかったら構文解析器を使って詳しく調べる
            tokens = tokenize(line)
            index = self.find(tokens)
            if index == -1:
                continue

            # さらに誤検出ではないか調べる (インスペクタが登録されているときだけのオプション)
            if self._is_misdetection(line):
                continue

            yield Violation(lineno, position, line)


class Replacer(with_metaclass(abc.ABCMeta)):

    def replace(self, text):
        result = self.replace_strategy(text)
        return result

    @abc.abstractproperty
    def replace_strategy(self):
        pass


class ReplaceStrategy(with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def __call__(self, text):
        pass


class TokenReplaceStrategy(ReplaceStrategy):

    def __init__(self, target, replacement, inspectors=None):
        inspectors = inspectors or []

        self.tokens = tokenize(target)
        self.replacement = replacement
        self.inspectors = inspectors

        self._search_strategy = TokenSearchStrategy(target)

    def _is_misdetection(self, line):
        if len(self.inspectors) < 1:
            return False

        for inspector in self.inspectors:
            if inspector.is_misdetection(line):
                return True

        return False

    def __call__(self, text):
        # 文章にトークンが含まれるかあらかじめ調べておく
        violations = self._search_strategy(text)
        try:
            next(violations)
        except StopIteration:
            # 要素がひとつもないということは置換対象が見つからないということ
            return text

        lines = text.split(os.linesep)

        replaced_lines = (self._replace(line) for line in lines)
        replaced_text = os.linesep.join(replaced_lines)
        return replaced_text

    def _replace(self, line):
        tokens = tokenize(line)
        index = self._search_strategy.find(tokens)

        if index == -1:
            return line

        if self._is_misdetection(line):
            return line

        replaced_tokens = (tokens[:index] +
                           [self.replacement] +
                           tokens[index + len(self.tokens):])
        return ''.join(replaced_tokens)
