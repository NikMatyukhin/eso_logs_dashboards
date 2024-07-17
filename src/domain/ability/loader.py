import itertools
import urllib.parse
from typing import Generator

import requests
from bs4 import BeautifulSoup, Tag

from src.settings import LoadingSettings

from .dto import AbilityDTO, AbilityListDTO


class AbilityLoader:
    def __init__(self, settings: LoadingSettings) -> None:
        self._settings = settings

    def _build_abilities_page_url(self, start_value: int = 0) -> str:
        if not start_value:
            return self._settings.abilities_url + urllib.parse.urlencode(
                {"record": "skillTree"}
            )
        return self._settings.abilities_url + urllib.parse.urlencode(
            {"start": str(start_value), "record": "skillTree"}
        )

    def _proceed_soup_table_contents(self, url: str) -> Generator[Tag, object, Tag]:
        for start_value in itertools.count(step=1000):
            response = requests.get(
                url=self._build_abilities_page_url(start_value=start_value)
            )
            soup = BeautifulSoup(response.text, "html.parser")
            skip_header_count = 2

            if not hasattr(soup, "body"):
                raise AttributeError("Parsed soup doesnt have 'body' attribute.")
            body: Tag = getattr(soup, "body")

            if not hasattr(body, "table"):
                raise AttributeError("Parsed soup body doesnt have 'table' attribute.")
            table: Tag = getattr(body, "table")

            for content in table.contents[skip_header_count:]:
                if not isinstance(content, Tag):
                    continue
                yield content

            if not body.find_all("a", href=True, text="Next"):
                return

    def get_abilities(self) -> AbilityListDTO:
        abilities_list = AbilityListDTO()
        for ability in self._proceed_soup_table_contents(
            url=self._settings.abilities_url
        ):
            abilities_list.abilities.append(
                AbilityDTO(
                    id=int(ability.contents[5].text),
                    name=ability.contents[13].text,
                    base_name=ability.contents[11].text,
                    icon=ability.contents[7].img.get("title"),
                    _type=ability.contents[21].text,
                )
            )
        return abilities_list
