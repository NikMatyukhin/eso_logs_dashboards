from typing import Generator

import requests
from bs4 import BeautifulSoup, Tag

from .dto import ItemDTO, ItemListDTO, ItemSetDTO, ItemSetListDTO


class ItemLoader:
    # TODO: APP or PARSE SETTINGS NEED HERE
    ITEM_SETS_URL = "https://esolog.uesp.net/viewlog.php?record=setSummary"
    ITEMS_URL = "https://esolog.uesp.net/viewlog.php"
    ID_COLUMN_INDEX = 3
    NAME_COLUMN_INDEX = 5
    ITEMS_COLUMN_INDEX = 37

    def _proceed_soup_table_contents(self, url: str) -> Generator[Tag, object, Tag]:
        response = requests.get(url=url)
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

    def get_item_sets(self) -> ItemSetListDTO:
        table_content = self._proceed_soup_table_contents(url=self.ITEM_SETS_URL)
        return ItemSetListDTO(
            item_sets=[
                ItemSetDTO(
                    id=int(item_set.contents[self.ID_COLUMN_INDEX].text),
                    name=item_set.contents[self.NAME_COLUMN_INDEX].text,
                )
                for item_set in table_content
            ]
        )

    def get_items(self) -> Generator[ItemListDTO, object, None]:
        for item_set in self._proceed_soup_table_contents(url=self.ITEM_SETS_URL):
            full_items_url = self.ITEMS_URL + item_set.contents[
                self.ITEMS_COLUMN_INDEX
            ].a.get("href")

            items_list = ItemListDTO()
            for item in self._proceed_soup_table_contents(url=full_items_url):
                items_list.items.append(
                    ItemDTO(
                        id=int(item.contents[3].text),
                        name=item.contents[5].a.text,
                        icon=item.contents[7].img.get("title"),
                        item_set_id=int(item_set.contents[3].text),
                    )
                )
            yield items_list
