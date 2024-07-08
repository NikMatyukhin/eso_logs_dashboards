from domain.fight.repository import FightRepository

PROVIDERS = [
    (FightRepository, lambda: FightRepository()),
]
