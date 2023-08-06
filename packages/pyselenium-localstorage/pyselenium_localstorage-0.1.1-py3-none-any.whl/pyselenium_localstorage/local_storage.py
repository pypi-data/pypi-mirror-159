from pyselenium_localstorage import codes


class LocalStorage:

    def __init__(self, driver):
        self.driver: 'selenium.webdriver.remote.webdriver.WebDriver' = driver

    def _exec(self, script: str, *args):
        return self.driver.execute_script(script, *args)

    def __len__(self) -> int:
        try:
            return int(self._exec(codes.LENGTH))
        except (ValueError, TypeError):
            return 0

    def dict(self) -> dict:
        return self._exec(codes.DICTIONARY)

    def items(self):
        """e.g. {k: v for k, v in local_storage.items()}"""
        return self.dict().items()

    def keys(self) -> list:
        return list(self._exec(codes.KEYS))

    def values(self) -> list:
        return list(self.dict().values())

    def get(self, key):
        return self._exec(codes.GET, key)

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def set(self, key, value):
        self._exec(codes.SET, key, value)

    def __setitem__(self, key, value):
        self.set(key, value)

    def has(self, key):
        return key in self.keys()

    def __contains__(self, key):
        return self.has(key)

    def remove(self, key):
        if key not in self.keys():
            raise KeyError(key)
        self._exec(codes.DEL, key)

    def __delitem__(self, key):
        self.remove(key)

    def clear(self):
        self._exec(codes.CLEAR)

    def __iter__(self):
        return self.keys().__iter__()

    def __repr__(self):
        return self.items().__str__()

    def __str__(self):
        return self.__repr__()
