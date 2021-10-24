# 正規表現をインポート
import re

# コマンドライン引数を受け取るために利用
import sys

args = sys.argv

# ファイル実行時に該当Performance.logの絶対パスを第一引数として渡す。
path = args[1]

with open(path) as f:
    # ログの各行をリストで取得する。
    log_list = f.readlines()

    # 符号なし0省略なしの正規表現は「\d+(?:\.\d+)?」
    re_target = r"\d+(?:\.\d+)?" + " ms"

    # 秒数を取り出して、格納するためのリストを用意する。
    second_string_list = []
    # print(re.search(re_target, log_list[1]))
    for a_log in log_list:
        # 正規表現でマッチしたものをオブジェクトに格納する。
        re_match = re.search(re_target, a_log)
        if re_match is not None:
            # 正規表現で取り出したものはまだオブジェクトなので、文字列を取り出す。
            second_string = re_match.group()
            # " ms"の部分は不要なので、取り除く
            replaced_second_string = second_string.replace(" ms", "")
            second_string_list.append(replaced_second_string)

    # 秒数が文字列の配列で格納されているので、数字の配列に変換する。
    second_fload_list = [float(s) for s in second_string_list]
    # 配列の合計値を計算する。
    total_second = sum(second_fload_list)
    print(str(total_second) + "ms")
