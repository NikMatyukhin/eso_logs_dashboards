from domain.actor.repository import ActorRepository
from domain.actor.service import ActorService

PROVIDERS = [
    (ActorRepository, lambda: ActorRepository()),
    (ActorService, lambda: ActorService()),
]
