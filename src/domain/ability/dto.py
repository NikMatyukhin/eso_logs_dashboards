from dataclasses import dataclass, field


@dataclass(eq=True, frozen=True)
class AbilityDTO:
    id: int
    name: str = field(hash=False, compare=False)
    base_name: str = field(hash=False, compare=False)
    icon: str = field(hash=False, compare=False)
    _type: str = field(hash=False, compare=False)


@dataclass
class AbilityListDTO:
    abilities: list[AbilityDTO] = field(default_factory=list)
