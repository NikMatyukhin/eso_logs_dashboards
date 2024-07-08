from typing import Sequence

import inject
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from db.models import Item, ItemSet
from domain.item.dto import ItemDTO, ItemListDTO, ItemSetDTO, ItemSetListDTO


class ItemRepository:
    _session: Session = inject.attr(Session)

    def create_item_set(self, dto: ItemSetDTO) -> ItemSet:
        model = ItemSet(
            id=dto.id,
            name=dto.name,
        )
        self._session.add(model)
        self._session.flush()
        self._session.refresh(model)

        return model

    def create_item_sets(self, dto: ItemSetListDTO) -> None:
        models = [
            ItemSet(
                id=item_set.id,
                name=item_set.name,
            )
            for item_set in dto.item_sets
        ]
        self._session.add(models)
        self._session.flush()

    def create_or_update_item_sets(self, dto: ItemSetListDTO) -> None:
        query = insert(ItemSet).values(
            [
                dict(
                    id=item_set.id,
                    name=item_set.name,
                )
                for item_set in dto.item_sets
            ],
        )
        query = query.on_conflict_do_update(
            index_elements=["id"],
            set_=dict(name=query.excluded.name),
        )
        self._session.execute(query)
        self._session.commit()

    def create_item(self, dto: ItemDTO) -> Item:
        model = Item(
            id=dto.id,
            name=dto.name,
            icon=dto.icon,
            item_set_id=dto.item_set_id,
        )
        self._session.add(model)
        self._session.flush()
        self._session.refresh(model)

        return model

    def create_items(self, dto: ItemListDTO) -> None:
        models = [
            Item(
                id=item.id,
                name=item.name,
                icon=item.icon,
                item_set_id=item.item_set_id,
            )
            for item in dto.items
        ]
        self._session.add(models)
        self._session.flush()

    def create_or_update_items(self, dto: ItemListDTO) -> None:
        query = insert(Item).values(
            [
                dict(
                    id=item.id,
                    name=item.name,
                    icon=item.icon,
                    item_set_id=item.item_set_id,
                )
                for item in dto.items
            ],
        )
        query = query.on_conflict_do_update(
            index_elements=["id"],
            set_=dict(
                name=query.excluded.name,
                icon=query.excluded.icon,
                item_set_id=query.excluded.item_set_id,
            ),
        )
        self._session.execute(query)
        self._session.commit()

    def get_by_id(self, item_id: int) -> Item:
        query = select(Item).where(Item.id == item_id)
        result = self._session.execute(query)
        return result.scalar_one()

    def get_by_ids(self, items_ids: list[int]) -> Sequence[Item]:
        query = select(Item).where(Item.id.in_(items_ids))
        result = self._session.execute(query)
        return result.scalars().all()
