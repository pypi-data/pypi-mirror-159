class Vault:
    def __init__(self, identifications: list):
        """
        用于搜索和聚合数据
        :param identifications: 身份识别字段
        """
        ...

    def exact_search(self, conditions: dict) -> list:
        ...

    def fuzzy_search(self, conditions: dict) -> list:
        ...

    def search(self, query: str) -> list:
        ...

    def load_json(self, name: str, json_data: str, columns_map: dict) -> None:
        ...
