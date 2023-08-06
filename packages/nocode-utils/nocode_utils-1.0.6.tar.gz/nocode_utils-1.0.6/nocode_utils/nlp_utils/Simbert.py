# encoding: utf-8
"""
-------------------------------------------------
@author: haohe
@email: haohe@nocode.com
@software: PyCharm
@file: Simbert.py
@time: 2022/7/15 14:00
@description:
-------------------------------------------------
"""
#! -*- coding: utf-8 -*-
# SimBERT base 基本例子
# 测试环境：tensorflow 1.14 + keras 2.3.1 + bert4keras 0.7.7

import numpy as np
from bert4keras.backend import keras
from bert4keras.models import build_transformer_model
from bert4keras.tokenizers import Tokenizer
from bert4keras.snippets import sequence_padding, AutoRegressiveDecoder


class Simbert(AutoRegressiveDecoder):
    def __int__(self, model_path, start_id=None, end_id=3):
        self.maxlen = 32

        # bert配置
        self.config_path = model_path + '/bert_config.json'
        self.checkpoint_path = model_path + '/bert_model.ckpt'
        self.dict_path = model_path + '/vocab.txt'

        # 建立分词器
        self.tokenizer = Tokenizer(self.dict_path, do_lower_case=True)  # 建立分词器

        # 建立加载模型
        self.bert = build_transformer_model(
            self.config_path,
            self.checkpoint_path,
            with_pool='linear',
            application='unilm',
            return_keras_model=False,
        )

        self.encoder = keras.models.Model(self.bert.model.inputs, self.bert.model.outputs[0])
        self.seq2seq = keras.models.Model(self.bert.model.inputs, self.bert.model.outputs[1])

    @AutoRegressiveDecoder.set_rtype('probas')
    def predict(self, inputs, output_ids, step):
        token_ids, segment_ids = inputs
        token_ids = np.concatenate([token_ids, output_ids], 1)
        segment_ids = np.concatenate(
            [segment_ids, np.ones_like(output_ids)], 1)
        return self.seq2seq.predict([token_ids, segment_ids])[:, -1]

    def generate(self, text, n=1, topk=5):
        token_ids, segment_ids = self.tokenizer.encode(text, max_length=self.maxlen)
        output_ids = self.random_sample([token_ids, segment_ids], n, topk)  # 基于随机采样
        return [self.tokenizer.decode(ids) for ids in output_ids]

    def gen_synonyms(self, text, n=100, k=20):
        r = self.generate(text, n)
        r = [i for i in set(r) if i != text]
        r = [text] + r
        X, S = [], []
        for t in r:
            x, s = self.tokenizer.encode(t)
            X.append(x)
            S.append(s)
        X = sequence_padding(X)
        S = sequence_padding(S)
        Z = self.encoder.predict([X, S])
        Z /= (Z ** 2).sum(axis=1, keepdims=True) ** 0.5
        argsort = np.dot(Z[1:], -Z[0]).argsort()
        return [r[i + 1] for i in argsort[:k]]

