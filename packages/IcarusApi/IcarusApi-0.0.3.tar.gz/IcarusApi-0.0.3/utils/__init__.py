global RED, YELLOW, BLACK, GREEN, MAGENTA, CYAN, WHITE # 可用颜色


def echo(something, color: int, end: str) -> None:
    """
    建议使用的输出\n
    :param something: 可以为任意类型，如果是字典，列表将输出他们在go中的结构
    :param color: 输出的颜色，可省略，默认为白色
    :param end: 输出的结尾，可省略，默认为换行符
    :return:
    """
    ...


def select(title: str, items: list) -> (int, str):
    """
    生成一个选择菜单，方向键选择，Enter确认 \n
    :param title: 标题
    :param items: 可选择的项目，字符串列表，若为空则不会阻塞
    :return: 返回选项序号与选项文本
    """
    ...


def match(left: str, right: str, text: str) -> list:
    """
    匹配文本中满足条件的全部文本（正则实现）\n
    e.g.
    \t echo(match("a", "c", "abc aqc")) \n
    \t result: ["b","q"] \n
    :param left: 左侧文本
    :param right: 右侧文本
    :param text: 需要匹配的文本
    :return: 返回包含结果的字符串列表
    """
    ...
