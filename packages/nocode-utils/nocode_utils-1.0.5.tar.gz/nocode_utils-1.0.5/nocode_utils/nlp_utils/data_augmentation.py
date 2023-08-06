# encoding: utf-8
"""
-------------------------------------------------
@author: haohe
@email: haohe@nocode.com
@software: PyCharm
@file: data_augmentation.py
@time: 2022/7/15 14:00
@description:
-------------------------------------------------
"""


def ramdom_word(text, num=10):
    from nlpcda import Randomword
    """
    随机(等价)实体替换
    :param text:
    :param num:
    :return:
    """
    smw = Randomword(create_num=num)
    return smw.replace(text)[1:]


def similar_word(text, num=10):
    from nlpcda import Similarword
    """
    随机同义词替换
    :param text:
    :param num:
    :return:
    """
    smw = Similarword(create_num=num)
    return smw.replace(text)[1:]


def homophone(text, num=10):
    from nlpcda import Homophone
    """
    随机近义字替换
    :param text:
    :param num:
    :return:
    """
    smw = Homophone(create_num=num)
    return smw.replace(text)[1:]


def char_position_exchange(text, num=10):
    from nlpcda import CharPositionExchange
    """
    随机置换邻近的字
    :param text:
    :param num:
    :return:
    """
    smw = CharPositionExchange(create_num=num)
    return smw.replace(text)[1:]


def equivalent_char(text, num=10):
    from nlpcda import EquivalentChar
    """
    等价字替换
    :param text:
    :param num:
    :return:
    """
    smw = EquivalentChar(create_num=num)
    return smw.replace(text)[1:]


def SimGenerator(model_path):
    from nocode_utils.nlp_utils.Simbert import Simbert
    """
    simbert 生成相似句子
    模型下载地址：https://github.com/ZhuiyiTechnology/pretrained-models
    选择 SimBERT-Tiny, SimBERT-Small, SimBERT-Base 其中之一
    源码地址：https://github.com/ZhuiyiTechnology/simbert
    需要 pip install tensorflow==1.14 keras==2.3.1 bert4keras==0.7.7
    :param model_path: 模型路径
    :return:
    """
    return Simbert(model_path)
