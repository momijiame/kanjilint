#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from kanjilint.code import ViolationTokenCode


def get_codes():
    return [
        ViolationTokenCode('更に', 'さらに'),
        ViolationTokenCode('殆ど', 'ほとんど'),
        ViolationTokenCode('下さい', 'ください'),
        ViolationTokenCode('事', 'こと'),
        ViolationTokenCode('物', 'もの'),
        ViolationTokenCode('1人', 'ひとり'),
        ViolationTokenCode('2人', 'ふたり'),
        ViolationTokenCode('そう言う', 'そういう'),
        ViolationTokenCode('お早う', 'おはよう'),
        ViolationTokenCode('そんな風に', 'そんなふうに'),
        ViolationTokenCode('あちらの方', 'あちらのほう'),
        ViolationTokenCode('出来るだけ', 'できるだけ'),
        ViolationTokenCode('恐る恐る', 'おそるおそる'),
        ViolationTokenCode('何時か', 'いつか'),
        ViolationTokenCode('何処か', 'どこか'),
        ViolationTokenCode('何故か', 'なぜか'),
        ViolationTokenCode('良いよ', 'いいよ'),
        ViolationTokenCode('捗る', 'はかどる'),
        ViolationTokenCode('後で', 'あとで'),
        ViolationTokenCode('あの人達', 'あのひとたち'),
        ViolationTokenCode('電話を掛ける', '電話をかける'),
        ViolationTokenCode('ひと通り', 'ひととおり'),
        ViolationTokenCode('ご免なさい', 'ごめんなさい'),
        ViolationTokenCode('丁度', 'ちょうど'),
        ViolationTokenCode('時間が経つ', '時間がたつ'),
        ViolationTokenCode('使い易い', '使いやすい'),
        ViolationTokenCode('何でも', 'なんでも'),
        ViolationTokenCode('言って頂いた', '言っていただいた'),
    ]
