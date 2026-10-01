__all__ = ["linkcheck"]

def linkcheck(link: str, timeout: int = 5) -> bool:
    """指定されたURLが実際に存在するか判定する

    :param link: 値を指定する
    :type link: str
    :param timeout: 応答を待つ秒数を指定する
    :type timeout: int
    :return: 指定されたURLが実際に存在するか返す
    :rtype: bool
    """
