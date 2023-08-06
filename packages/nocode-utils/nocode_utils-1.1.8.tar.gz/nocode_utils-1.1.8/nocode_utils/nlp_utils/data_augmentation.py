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


def random_word(text, num=10):
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
    smw = CharPositionExchange(create_num=num, char_gram=3, seed=1)
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
