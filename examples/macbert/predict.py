# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import argparse
import sys

sys.path.append('../..')

from pycorrector.macbert.macbert_corrector import MacBertCorrector


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", default="./outputs-macbert4csc", type=str, help="Dir for model save.")
    args = parser.parse_args()
    print(args)

    m = MacBertCorrector(args.output_dir)
    inputs = [
        '老是较书。',
        '感谢等五分以后，碰到一位很棒的奴生跟我可聊。',
        '遇到一位很棒的奴生跟我聊天。',
        '遇到一位很美的女生跟我疗天。',
        '他们只能有两个选择：接受降新或自动离职。',
        '王天华开心得一直说话。'
    ]
    for i in inputs:
        output = m.correct(i)
        print('input  :', i)
        print('predict:', output)
        print()

    # result:
    # input  : 老是较书。
    # predict: 老师教书。 [('是', '师', 1, 2), ('较', '教', 2, 3)]
    #
    # input  : 感谢等五分以后，碰到一位很棒的奴生跟我可聊。
    # predict: 感谢等五分以后，碰到一位很棒的女生跟我可聊。 [('奴', '女', 15, 16)]


if __name__ == "__main__":
    main()
