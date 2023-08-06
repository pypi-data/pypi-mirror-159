from beadsnum import BeadsNum


class CyberNum:
    """Cyber Number"""

    def __init__(self, value=0):
        self._beadsnum = BeadsNum(value)

        # 最後の列が 1 でなければいけない
        columns = self._beadsnum.columns
        last = len(columns) - 1
        if columns[last] != 1:
            raise ValueError(f"not cyber number: {self._beadsnum.dicordnum}")

        # 1 が連続する列があってはいけない
        pre_column = 0
        for column in columns:
            if column == 1 and pre_column == column:
                raise ValueError(
                    f"not cyber number: {self._beadsnum.dicordnum}")
            pre_column = column

    def __str__(self):
        return f"{self._beadsnum.dicordnum}"

    @property
    def columns(self):
        return self._beadsnum.columns
