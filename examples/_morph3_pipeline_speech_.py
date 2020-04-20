#!/usr/bin/python
# -*- coding: utf-8 -*-

from corpuscula.corpus_utils import download_syntagrus, syntagrus, \
                                    AdjustedForSpeech
from local_methods import guess_pos, guess_lemma, guess_feat
from morra import MorphParser3

download_syntagrus(overwrite=False)
train_corpus = dev_corpus = test_corpus = AdjustedForSpeech(syntagrus)

def get_model (load_corpuses=True, load_model=True):
    mp = MorphParser3(guess_pos=guess_pos, guess_lemma=guess_lemma,
                      guess_feat=guess_feat)
    if load_corpuses:
        mp.load_test_corpus(dev_corpus)
        mp.load_train_corpus(train_corpus)
    if load_model:
        mp.load('model_speech_.pickle')
    return mp

def reload_train_corpus ():
    mp._train_corpus = None
    mp.load_train_corpus(train_corpus)

mp = get_model(load_model=False)
mp.parse_train_corpus()
mp.save('model_speech_.pickle')

mp = get_model()
mp.train_lemma(epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_lemma(test_corpus)

mp = get_model()
mp.train_pos(rev=False, seed=4, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_pos(test_corpus, rev=False)

mp = get_model()
mp.train_pos(rev=True, seed=4, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_pos(test_corpus, rev=True)

mp = get_model()
mp.train_pos2(seed=4, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_pos2(test_corpus)
mp.evaluate_pos2(test_corpus, with_backoff=False)
'''
mp = get_model()
mp.train_feats(joint=False, rev=False, seed=21, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_feats(test_corpus, joint=False, rev=False)

mp = get_model()
mp.train_feats(joint=False, rev=True, seed=21, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_feats(test_corpus, joint=False, rev=True)

mp = get_model()
mp.train_feats2(joint=False, seed=21, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_feats2(test_corpus, joint=False)
mp.evaluate_feats2(test_corpus, joint=False, with_backoff=False)

mp = get_model()
mp.train_feats(joint=True, rev=False, seed=21, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_feats(test_corpus, joint=True, rev=False)

mp = get_model()
mp.train_feats(joint=True, rev=True, seed=21, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_feats(test_corpus, joint=True, rev=True)

mp = get_model()
mp.train_feats2(joint=True, seed=21, epochs=-3)
mp.save('model_speech_.pickle')
mp.evaluate_feats2(test_corpus, joint=True)
mp.evaluate_feats2(test_corpus, joint=True, with_backoff=False)
print()
mp.evaluate_feats3(test_corpus)
mp.evaluate_feats3(test_corpus, with_s_backoff=False, with_j_backoff=False)

print()
print()
print('FINAL TESTS')
mp = get_model(load_corpuses=False)
print()
print('== lemma ==')
mp.evaluate_lemma(test_corpus)
print()
print('== pos 1 ==')
mp.evaluate_pos(test_corpus)
print('== pos 1-rev ==')
mp.evaluate_pos(test_corpus, rev=True)
print('== pos 2 ==')
mp.evaluate_pos2(test_corpus)
print('== pos 2- ==')
mp.evaluate_pos2(test_corpus, with_backoff=False)
print()
print('== feats 1s ==')
mp.evaluate_feats(test_corpus, joint=False, rev=False)
print('== feats 1s-rev ==')
mp.evaluate_feats(test_corpus, joint=False, rev=True)
print('== feats 2s ==')
mp.evaluate_feats2(test_corpus, joint=False)
print('== feats 2s- ==')
mp.evaluate_feats2(test_corpus, joint=False, with_backoff=False)
print()
print('== feats 1j ==')
mp.evaluate_feats(test_corpus, joint=True, rev=False)
print('== feats 1j-rev ==')
mp.evaluate_feats(test_corpus, joint=True, rev=True)
print('== feats 2j ==')
mp.evaluate_feats2(test_corpus, joint=True)
print('== feats 2j- ==')
mp.evaluate_feats2(test_corpus, joint=True, with_backoff=False)
print()
print('== feats 3 ==')
mp.evaluate_feats3(test_corpus)
print('== feats 3- ==')
mp.evaluate_feats3(test_corpus, with_s_backoff=False, with_j_backoff=False)
print()
print('== 1s ==')
mp.evaluate(test_corpus)
print('== 1s-rev ==')
mp.evaluate(test_corpus, pos_rev=True, feats_rev=True)
print('== 1j ==')
mp.evaluate(test_corpus, feats_joint=True)
print('== 1j-rev ==')
mp.evaluate(test_corpus, pos_rev=True, feats_joint=True, feats_rev=True)
print()
print('== 2s ==')
mp.evaluate2(test_corpus, feats_joint=False)
print('== 2s-p ==')
mp.evaluate2(test_corpus, pos_backoff=False, feats_joint=False)
print('== 2s-f ==')
mp.evaluate2(test_corpus, feats_joint=False, feats_backoff=False)
print('== 2s-pf ==')
mp.evaluate2(test_corpus, pos_backoff=False, feats_joint=False, feats_backoff=False)
print()
print('== 2j ==')
mp.evaluate2(test_corpus, feats_joint=True)
print('== 2j-p ==')
mp.evaluate2(test_corpus, pos_backoff=False, feats_joint=True)
print('== 2j-f ==')
mp.evaluate2(test_corpus, feats_joint=True, feats_backoff=False)
print('== 2j-pf ==')
mp.evaluate2(test_corpus, pos_backoff=False, feats_joint=True, feats_backoff=False)
print()
print('== 3 ==')
mp.evaluate3(test_corpus)
print('== 3-p ==')
mp.evaluate3(test_corpus, pos_backoff=False)
print('== 3-f ==')
mp.evaluate3(test_corpus, feats_s_backoff=False, feats_j_backoff=False)
print('== 3-pf ==')
mp.evaluate3(test_corpus, pos_backoff=False, feats_s_backoff=False, feats_j_backoff=False)
'''
