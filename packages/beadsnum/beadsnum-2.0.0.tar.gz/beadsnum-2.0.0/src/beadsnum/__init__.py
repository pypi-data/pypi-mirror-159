import re
from dicordnum import DicOrdNum


class BeadsNum:
    """Beads Nested Number"""

    # めんどくさいので .upper() して O と数字で構成されていればOkとする
    # 辞書順記数法に対応するために、めんどくさいので A が含まれていてもOkとする
    pattern1 = re.compile(r"^([AO\d]*)$")

    def __init__(self, value=0):

        try:
            # 整数かどうか判定
            int(str(value), 10)
        except ValueError:
            # 無視
            pass
        else:
            # タプルとして格納する
            self._columns = value,
            return

        if type(value) is tuple:
            # タプル型なら
            # そのまま入れる
            self._columns = value
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

            # 辞書順記数法に対応するために、 A を除去する
            value = value.replace('A', '')

            # O が２連続してはいけない
            if "OO" in value:
                raise ValueError(f"not beads nested number: {value}")

            # 先頭に O が付いているのは構わないものとし、
            # 先頭に付いている O は削除する
            value = value.lstrip('O')

            # 区切り文字 O で分割
            columns = value.split('O')

            # 整数化
            columns = map(lambda x: int(x), columns)

            # タプルとして格納する
            self._columns = tuple(columns)

    def __str__(self):
        text = ""
        for column in self._columns:
            text = f"{text}o{column}"
        # 先頭を大文字にする
        text = f"O{text[1:]}"
        return text

    @property
    def columns(self):
        return self._columns

    @property
    def dicordnum(self):
        """辞書順記数法"""
        text = ""
        for column in self._columns:
            text = f"{text}o{DicOrdNum(column)}"
        # 先頭を大文字にする
        text = f"O{text[1:]}"
        return text
