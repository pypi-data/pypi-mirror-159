GET = "GET"
POST = "POST"


class Response:
    def status_code(self) -> int:
        """
        响应包状态码\n(如果为-1则表示请求过程发生错误，详细错误用text()方法查看。\n
        :return:
        """
        ...

    def headers(self) -> dict:
        """
        响应头\n
        存在多个值的响应头以列表储存。\n
        :return:
        """
        ...

    def text(self) -> str:
        """
        获取响应正文\n
        :return:
        """
        ...

    def content(self) -> bytes:
        """
        获取响应正文(bytes)\n
        :return:
        """
        ...


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


def request(method: str, url: str, params: dict, data: str, headers: dict, verify: bool, proxy: dict) -> Res:
    """
    发送http请求\n
    :param method: GET,POST
    :param url: 目标url
    :param params: url参数，可省略
    :param data: post文本，可省略
    :param headers: 请求头,可省略
    :param verify: 是否验证https，可省略，默认为不验证
    :param proxy: 是否使用代理，可省略
    :return: Response
    """
    ...
