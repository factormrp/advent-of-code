import os

from dotenv import load_dotenv, find_dotenv
from typing import Dict, List
from os import getenv
import datetime
import requests

# Load in environment variables
load_dotenv(find_dotenv())
SESSION_COOKIE = getenv("SESSION_COOKIE")


class Source:

    def __init__(self, date: datetime.datetime, cookies: Dict = None) -> None:
        """
        Constructor for Advent of Code data

        Takes in datetime representing date of data to fetch. Optionally takes
        a dictionary specifying the SESSION_ID cookie to use
        """
        self.url = self._get_url_from_date(date)
        if cookies is None:
            self.cookies = {"session": SESSION_COOKIE}
        else:
            self.cookies = cookies

    @property
    def data(self) -> str:
        return self._clean_data()

    @property
    def lines(self) -> List[str]:
        return self._clean_data().split("\n")

    def _fetch_data(self) -> str:
        with requests.get(self.url, cookies=self.cookies) as res:
            data = res.text
        return data

    def _clean_data(self) -> str:
        data = self._fetch_data()
        if data[-1] == "\n":
            return data[:-1]
        return data

    @staticmethod
    def _get_url_from_date(date: datetime.datetime) -> str:
        return f"https://adventofcode.com/{date.year}/day/{date.day}/input"
