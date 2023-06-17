import sys

from functools import reduce
from operator import or_

from boto3.dynamodb.conditions import Attr, ConditionExpressionBuilder


def merge_attr():
    """
    Attrを生成して結合する
    rangeの引数を変えると、build_expressionでの再帰の回数が変わる
    値が大きすぎると、RecursionErrorになる
    
    """
    attrs = [Attr('id').eq(i) for i in range(497)]
    return reduce(or_, attrs)


def main():
    ceb = ConditionExpressionBuilder()
    return ceb.build_expression((merge_attr()))


if __name__ == '__main__':
    
    # 再帰の回数を表示
    print(sys.getrecursionlimit())

    # 実行
    print(main())
