def argv(name: int) -> str:
    """
    获取Icarus命令行参数
    :param name: 可以是整型也可以是字符串
    :return: 值
    """
    ...


def env(name: str, value: str) -> str:
    """
    获取Icarus环境变量
    :param name: 变量名
    :param value: 若此参数不存在则为获取，若此参数存在则为修改
    :return: 环境变量的值
    """
    ...


def shell_exec(cmd: str, args: list, cmd_dir: str) -> None:
    """
    在本地执行shell命令，以任务执行，非阻塞函数。
    :param cmd: 要执行的命令
    :param args: 命令行参数，类型为字符串列表，可省略
    :param cmd_dir: 执行命令的位置，可省略
    :return: 返回任务id
    """
