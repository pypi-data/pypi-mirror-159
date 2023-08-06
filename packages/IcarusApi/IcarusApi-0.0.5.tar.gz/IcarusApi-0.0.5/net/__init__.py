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
