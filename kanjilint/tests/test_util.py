#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nose
from nose.tools.trivial import eq_

from kanjilint.util import is_kanji


class Test_is_kanji(object):

    def test(self):
        '''
        正常系/異常系: 色々な文字を使って判定する
        '''
        eq_(is_kanji(u'あ'), False)
        eq_(is_kanji(u'亜'), True)
        eq_(is_kanji(u'　'), False)
        eq_(is_kanji(u'＿'), False)


if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)
