#!/usr/bin/python
# -*- coding: utf-8 -*-
# Morra project
#
# Copyright (C) 2019-present by Sergei Ternovykh
# License: BSD, see LICENSE for details
"""
Example: Evaluate partial Morra models.
"""
from corpuscula.corpus_utils import download_ud, UniversalDependencies, \
                                    AdjustedForSpeech
from morra import MorphParser3

###
import sys
sys.path.append('../')
###
import _get_names_db
from scripts.local_methods_syntagrus import guess_pos, guess_lemma, guess_feat

MODEL_FN = 'model.pickle'

# we use UD Taiga corpus only as example. For real model training comment
# Taiga and uncomment SynTagRus
corpus_name = 'UD_Russian-Taiga'
#corpus_name = 'UD_Russian-SynTagRus'

download_ud(corpus_name, overwrite=False)
train_corpus = dev_corpus = test_corpus = UniversalDependencies(corpus_name)
#train_corpus = dev_corpus = test_corpus = \
#                         AdjustedForSpeech(UniversalDependencies(corpus_name))

mp = MorphParser3(guess_pos=guess_pos, guess_lemma=guess_lemma,
                  guess_feat=guess_feat)
mp.load(MODEL_FN)

print()
print('== lemma ==')
mp.evaluate_lemma(test_corpus)
print()
print('== pos 1 ==')
mp.evaluate_pos(test_corpus)
print('== pos 1-rev ==')
mp.evaluate_pos(test_corpus, rev=True)
print('== pos 2 ==')
mp.evaluate_pos2(test_corpus, with_backoff=True)
for _r in [0, 1, 2, 20]:
    print('== pos 2:{} =='.format(_r))
    mp.evaluate_pos2(test_corpus, with_backoff=False, max_repeats=_r)
print()
print('== feats 1s ==')
mp.evaluate_feats(test_corpus, joint=False, rev=False)
print('== feats 1s-rev ==')
mp.evaluate_feats(test_corpus, joint=False, rev=True)
print('== feats 2s ==')
mp.evaluate_feats2(test_corpus, joint=False, with_backoff=True)
for _r in [0, 1, 2, 20]:
    print('== feats 2j:{} =='.format(_r))
    mp.evaluate_feats2(test_corpus, joint=False, with_backoff=False,
                       max_repeats=_r)
print()
print('== feats 1j ==')
mp.evaluate_feats(test_corpus, joint=True, rev=False)
print('== feats 1j-rev ==')
mp.evaluate_feats(test_corpus, joint=True, rev=True)
print('== feats 2j ==')
mp.evaluate_feats2(test_corpus, joint=True, with_backoff=True)
for _r in [0, 1, 2, 20]:
    print('== feats 2j:{} =='.format(_r))
    mp.evaluate_feats2(test_corpus, joint=True, with_backoff=False,
                       max_repeats=_r)
print()
for max_s in [None, 0, 1, 2]:
    for max_j in [None, 0, 1, 2]:
        print('== feats 3:{}:{} =='.format('' if max_s is None else max_s,
                                           '' if max_j is None else max_j))
        mp.evaluate_feats3(test_corpus,
                           with_s_backoff=max_s is None, max_s_repeats=max_s,
                           with_j_backoff=max_j is None, max_j_repeats=max_j)
