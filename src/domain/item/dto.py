from dataclasses import dataclass, field


@dataclass
class ItemDTO:
    id: int
    name: str
    icon: str

    item_set_id: int


@dataclass
class ItemListDTO:
    items: list[ItemDTO] = field(default_factory=list)


@dataclass
class ItemSetDTO:
    id: int
    name: str


@dataclass
class ItemSetListDTO:
    item_sets: list[ItemSetDTO] = field(default_factory=list)
