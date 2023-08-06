import re


class DicOrdNum:
    """Dictionary Ordinal Number"""

    pattern = re.compile(r"(A*)(\d+)")

    def __init__(self, value=0):

        try:
            # 整数かどうか判定
            num = int(str(value), 10)
        except ValueError:
            # 整数ではなかった
            result = DicOrdNum.pattern.match(value)
            if result:
                # 構文は合っているようだ
                prefix = result.group(1)
                numeric = result.group(2)

                # 桁数比較
                if len(prefix) + 1 == len(numeric):
                    # Aの個数が合っていた
                    self._num = int(numeric)
                else:
                    # Aの個数が合っていない
                    raise ValueError(f"not dictionary ordinal number: {value}")
            else:
                # 構文エラー
                raise ValueError(f"not dictionary ordinal number: {value}")
        else:
            # 整数だ
            if num < 0:
                # 負数だ
                raise ValueError(f"not dictionary ordinal number: {value}")
            else:
                # 正の数だ
                self._num = value

    def __str__(self):
        figure = len(str(self._num))
        prefix = ""
        for i in range(1, figure):
            prefix += "A"
        return f"{prefix}{self._num}"
