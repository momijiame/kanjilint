#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

from future.utils import with_metaclass


class Inspector(with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def is_misdetection(self, line):
        pass
