class Requester:
    def __init__(self, raw: str):
        """
        请求器可以通过规则生成请求，并按规则批量发送（尚不可用）\n
        :param raw: 基础请求包
        """
        ...

    def send(self, proxy_name: str, verify: bool) -> list:
        ...

    def set_proxy(self, name: str, proxy: dict) -> None:
        ...

    def set_verify(self, verify: bool):
        ...


def download(url: str, save_path: str, proxy_url: str) -> bool:
    """
    下载文件\n
    :param url: 文件url
    :param save_path: 文件保存路径，如果是文件将会写入文件。可省略，默认当前Icarus工作目录
    :param proxy_url: 代理url，可省略。e.g. http://127.0.0.1:7890 代理到本地clash
    :return: 下载是否成功
    """
    ...
