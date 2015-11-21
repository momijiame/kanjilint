#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose
from nose.tools.trivial import eq_

from kanjilint.base import TokenSearchStrategy
from kanjilint.base import TokenReplaceStrategy


class Test_TokenSearchStrategy(object):

    def test(self):
        '''
        正常系: 構文解析器を使った探索をテストする
        '''
        strategy = TokenSearchStrategy(u'後で')
        violations = strategy(u'それより後で')

        eq_(len(list(violations)), 1)

        strategy = TokenSearchStrategy(u'後で')
        violations = strategy(u'その前後で')

        eq_(len(list(violations)), 0)

        strategy = TokenSearchStrategy(u'1人で')
        violations = strategy(u'また1人で')

        eq_(len(list(violations)), 1)


class Test_TokenReplaceStrategy(object):

    def test(self):
        '''
        正常系: 構文解析器を使った置換をテストする
        '''
        strategy = TokenReplaceStrategy(u'後で', u'あとで')
        replaced_text = strategy(u'前後で後で')

        eq_(replaced_text, u'前後であとで')


if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)
