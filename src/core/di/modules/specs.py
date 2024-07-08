from domain.spec.repository import SpecRepository

PROVIDERS = [
    (SpecRepository, lambda: SpecRepository()),
]
