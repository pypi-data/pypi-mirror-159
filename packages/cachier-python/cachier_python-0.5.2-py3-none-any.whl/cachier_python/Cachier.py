import requests

from cachier_common_library import DriverType, DriverTypeError


class Cachier:
    def __init__(self: 'Cachier', url: str, driver: str = None) -> None:
        self.url = url

        if driver:
            is_valid_driver = DriverType().is_valid(driver)
            if not is_valid_driver:
                raise DriverTypeError('provided driver is not valid')

        self.driver = driver

    def get(self: 'Cachier', key: str) -> object:
        if not key: return None

        url: str = f'{self.url}?cache_key={key}&driver={self.driver}'
        response: requests.Response = requests.get(url)

        if response.status_code != 200: return None

        response_json: dict = response.json()

        if not response_json: return None

        return response_json['value']

    def set(self: 'Cachier', key: str, value: object, expiry: int | None = None) -> bool:
        if not key: return False

        url: str = f'{self.url}'
        response: requests.Response = requests.post(url, json={
            'cache_key': key,
            'cache_value': value,
            'cache_expiry': expiry,
            'driver': self.driver,
        })

        if response.status_code != 200: return False

        response_json: dict = response.json()

        if not response_json: return False

        return response_json['is_saved_successfully']
