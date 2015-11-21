#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kanjilint.code.base import CodeBase
from kanjilint.base import TokenSearchStrategy
from kanjilint.base import TokenReplaceStrategy


class ViolationTokenCode(CodeBase):

    def __init__(self, target, replacement, inspectors=None):
        self.target = target
        self.replacement = replacement
        self.inspectors = inspectors

    @property
    def detect_strategy(self):
        return TokenSearchStrategy(self.target, self.inspectors)

    @property
    def replace_strategy(self):
        return TokenReplaceStrategy(self.target, self.replacement,
                                    self.inspectors)
