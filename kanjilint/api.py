#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kanjilint.code import api


def detect(text):
    code_instances = api.get_codes()
    for code_instance in code_instances:
        violations = code_instance.detect(text)
        for violation in violations:
            yield violation


def replace(text):
    code_instances = api.get_codes()
    for code_instance in code_instances:
        text = code_instance.replace(text)
    return text
