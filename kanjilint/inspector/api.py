#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kanjilint.inspector import DynamicUserExclusionInspector


def get_default_inspectors():
    return [
        DynamicUserExclusionInspector,
    ]
