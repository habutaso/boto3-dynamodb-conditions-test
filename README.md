# setup
```bash
$ git clone https://github.com/habutaso/boto3-dynamodb-conditions-test
$ cd boto3-dynamodb-conditions-test
$ pip install pipenv
$ pipenv install
$ pipenv shell
```

# run
```
$ python main.py
```

# exit Pipenv
```
$ deactivate
```

# エラー
`ConditionExpressionBuilder`を実行中に、再帰処理のスタック上限を表すエラーが出力される
```bash
RecursionError: maximum recursion depth exceeded while getting the str of an object
```
これは、`Attr`オブジェクトが多すぎて、相互再帰を想定以上に繰り返すことで起こる  
`boto3.dynamodb.conditions.ConditionExpressionBuilder`のコードを見るともう少し理解深まる  
https://github.com/boto/boto3/blob/edb50b6c788018acf353fa7cb47794639a70db06/boto3/dynamodb/conditions.py#LL305C9-L305C9

