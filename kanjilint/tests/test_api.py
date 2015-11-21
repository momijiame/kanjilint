#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import nose
from nose.tools.trivial import eq_

from kanjilint.api import detect
from kanjilint.api import replace


class Test_detect(object):

    def test_success_hit(self):
        '''
        正常系: 単一の行の中に目当ての文字列が含まれている
        '''
        text = 'ほげほげ。更に、ふがふが'

        hit_list = list(detect(text))
        eq_(hit_list[0].lineno, 1)

    def test_success_miss(self):
        '''
        正常系: 単一の行の中に目当ての文字列が含まれていない
        '''
        text = 'ほげほげ。ふがふが'

        hit_list = list(detect(text))
        eq_(len(hit_list), 0)

    def test_success_hit_on_2nd_line(self):
        '''
        正常系: 二行目に目当ての文字列が含まれている
        '''
        text = '''ほげほげ
更に、ふがふが
ばずばず
'''

        hit_list = (list(detect(text)))
        eq_(hit_list[0].lineno, 2)

    def test_success_hit_multiple_lines(self):
        '''
        正常系: 複数行に目当ての文字列が含まれている
        '''
        text = '''ほげほげ
更に、ふがふが
更に、ばずばず
'''

        hit_list = (list(detect(text)))
        eq_(len(hit_list), 2)
        eq_(hit_list[0].lineno, 2)
        eq_(hit_list[1].lineno, 3)


class Test_replace(object):

    def test_success(self):
        '''
        正常系: 単一の行に目当ての文字列が含まれている
        '''
        text = 'ほげほげ。更に、ふがふが'
        expect = 'ほげほげ。さらに、ふがふが'

        result = replace(text)
        eq_(result, expect)

    def test_success_multiple_lines(self):
        '''
        正常系: 複数行に目当ての文字列が含まれている
        '''
        text = '''ほげほげ
更に、ふがふが
更に、ばずばず
'''
        expect = '''ほげほげ
さらに、ふがふが
さらに、ばずばず
'''

        result = replace(text)
        eq_(result, expect)


if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)
