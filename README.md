# はじめに

最近業務で、RDBにも関わらず、一つのテーブルに一つのカラムを管理しているデータベースを触る機会がありました。
そこで、本来行として持つべきテーブルを、列で持つとどれくらいパフォーマンスに影響を及ぼすのか気になり調べてみました。
データの履歴(バージョン)管理のために、列でデータを持つ必要になる方にも参考になると思います。

# 環境

```
% brew info postgresql
postgresql: stable 13.4 (bottled), HEAD
```

# 今回実行したSQL

[こちらのgit]()に記載している。

# パフォーマンステスト: 行指向テーブル

| 処理※1 | テーブル作成 | 全件取得 | 検索 | 作成 | 更新 | 削除 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 時間(ms)※2 | 5.7 | 6.6 | 1.3 | 1481.1 | 7736.5 | 5502.1 |
| 凡その時間(秒) | 1秒以下 | 1秒以下 | 1秒以下 | 1秒 | 8秒 | 6秒 |

※1 行数は約10000行
※2 小数第二位を四捨五入

# パフォーマンステスト: 列指向テーブル

| 処理※1 | テーブル作成 | 全件取得 | 検索 | 作成 | 更新 | 削除 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 時間(ms)※2 | 22.4 | 92.6 | 2.1 | 15878.8 | 108352.1 | 53893.3 |
| 凡その時間(秒) | 1秒以下 | 1秒以下 | 1秒以下 | 15秒 | 108秒 | 53秒 |

※1 行数は約10000行
※2 小数第二位を四捨五入


# 終わりに

結果的に、列で管理すると相当のパフォーマンス低下に繋がることがわかりました。

#### おまけ1: ログファイルの出力方法

- ログファイルの設定場所
```
postgres=# SHOW config_file;
config_file               
-----------------------------------------
 /usr/local/var/postgres/postgresql.conf
(1 row)

Time: 0.398 ms
```

- ログファイルの場所
```
/usr/local/var/log
```

- ログに時間を設定する方法

[Can I log query execution time in PostgreSQL 8.4?](https://stackoverflow.com/questions/12670745/can-i-log-query-execution-time-in-postgresql-8-4)

- ログに出力させたものをgrepを使って、外部のログファイルに出力する方法

```
$ grep "2021-xx-xx 11:50:" postgres.log >> /Users/mac/Psql/ColumnOrientedDatabase/Sql/Insert/Performance/Performance.log
```

#### おまけ2: ログファイルから時間だけを取得するモジュール

下記ディレクトリ(/Users/mac/Psql/ExtractTimeFromPerformanceLog)に、ログファイルから時間だけを取り出すモジュールを作成した。
ファイル実行時に、第一引数として該当のログファイルを指定すると、そのログファイルに記載された時間を合計して、出力するようにした。

- ファイル実行例
```
$ python3 /Users/mac/Psql/ExtractTimeFromPerformanceLog/ExtractTimeFromPerformanceLog.py /Users/mac/Psql/RowOrientedDatabase/Sql/Delete/Performance/Performance.log
5502.076999999987ms
```

#### 注意事項

- UMLのディレクトリでは、ER図と書いているが、リレーションは記載せず、どのようなテーブルがあるかだけを記載した。
- SQLのクエリの書き方で大きくパフォーマンスが変わると思われる。
