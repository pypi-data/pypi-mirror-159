from datetime import datetime, time
from dotenv import load_dotenv
import requests
import json
import os

from .exceptions import (
    ConnectionException,
    DataException,
    RequestException,
    ResponseException,
)
from . import utils

load_dotenv()
DEBUG = os.environ.get("DEBUG")
DEFAULT_URL = os.environ.get("DATABASE_URL")


class APITools:
    METHODS = {
        "post": requests.post,
        "get": requests.get,
        "update": requests.patch,
        "delete": requests.delete,
    }
    if DEFAULT_URL is None:
        DEFAULT_URL = "https://habitat-api.onrender.com/api"
    if DEBUG:
        DEFAULT_URL = "http://habitat-api:5000/api"

    def __init__(self, api_url=None):
        self.api_url = api_url
        if self.api_url is None:
            self.api_url = os.environ.get("HABITAT_API_URL", self.DEFAULT_URL)
        self.validate_url(self.api_url)

    @staticmethod
    def validate_url(url):
        try:
            resp = requests.get(f"{url}/reading")
        except Exception:
            raise ConnectionException(
                "Incorrect API URL or API unreachable!", key="APIError"
            ).json()

    def request(self, url, method="get", data=None):
        try:
            resp = self.handle_request(url, method, data)
        except Exception as e:
            resp = e
        return resp.json()

    def handle_request(self, url, method, data):
        if data is not None and not isinstance(data, dict):
            raise DataException("Data missing or Dict format invalid!", key="DataError")

        req_method = self.METHODS.get(method)
        if req_method is None:
            raise RequestException("Invalid API request method type", key="DataError")
        try:
            resp = req_method(
                f"{self.api_url}/{url}/",
                json=data,
            )
        except Exception:
            raise ConnectionException("Incorrect API URL or API unreachable!")

        if not (200 <= resp.status_code < 300):
            message = resp.json().get("message")
            if message is None:
                message = resp.json().get("status")
            raise ResponseException(message, key="APIError")

        try:
            return resp
        except Exception:
            raise DataException("API JSON response format invalid!", key="APIError")

    def add_reading(self, temperature=None, humidity=None):
        return self.request(
            "reading",
            method="post",
            data={"temperature": temperature, "humidity": humidity},
        )

    def get_reading(self):
        return self.request("reading")

    def filter_readings(self, period=None, unit=None, date_from=None, date_to=None):
        data = {}
        if period is not None:
            data.update({"period": period, "unit": unit})
        elif date_from is not None:
            data.update({"date_from": date_from, "date_to": date_to})
        return self.request("readings", data=data)

    def get_config(self):
        return self.request("config")

    def set_config(self, data=None):
        if data is not None:
            data = utils.convert_dt_to_iso(data)
        return self.request("config", method="post", data=data)

    def new_config(self):
        return self.request("config/default/")

    def get_stats(self):
        return self.request("config/stats/")
