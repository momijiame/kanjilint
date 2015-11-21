#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kanjilint.inspector.base import Inspector


class DynamicUserExclusionInspector(Inspector):

    def is_misdetection(self, line):
        # Click が読み込んだ設定をグローバル変数から手に入れる
        global CONTEXT
        rules = CONTEXT['IGNORE']

        for rule in rules:
            # ユーザが意図的に排除したい文字列と一致した
            if line.find(rule) != -1:
                return True

        return False
