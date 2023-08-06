import re


class BeadsNum:
    """Beads Nested Number"""

    # めんどくさいので .upper() して O と数字で構成されていればOkとする
    pattern1 = re.compile(r"^([O\d]*)$")

    def __init__(self, value=0):

        try:
            # 整数かどうか判定
            num = int(str(value), 10)
        except ValueError:
            # 無視
            pass
        else:
            # タプルとして格納する
            self._numbers = value,
            return

        if type(value) is tuple:
            # タプル型なら
            # そのまま入れる
            self._numbers = value
        else:
            # それ以外は文字列として扱う

            # 大文字に変換
            value = value.upper()

            # A,O と数字で構成されている必要がある
            result = BeadsNum.pattern1.match(value)
            if result:
                pass
            else:
                raise ValueError(f"not beads nested number: {value}")

            # O が２連続してはいけない
            if "OO" in value:
                raise ValueError(f"not beads nested number: {value}")

            # 先頭に O が付いているのは構わないものとし、
            # 先頭に付いている O は削除する
            value = value.lstrip('O')

            # 区切り文字 O で分割
            numerics = value.split('O')

            # 整数化
            numerics = map(lambda x: int(x), numerics)

            # タプルとして格納する
            self._numbers = tuple(numerics)

    def __str__(self):
        text = ""
        for numeric in self._numbers:
            text = f"{text}o{numeric}"
        return text.capitalize()

    @property
    def numbers(self):
        return self._numbers
