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
これは、`Attr`オブジェクトの結合し過ぎが問題となって起こる

