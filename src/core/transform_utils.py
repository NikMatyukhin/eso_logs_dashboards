from collections import defaultdict
from typing import KeysView, Mapping, Sequence, TypeVar

from .gql.schemas import BaseModelWithID

TModel = TypeVar("TModel", bound=BaseModelWithID)


def transform_to_id_map(
    models: list[TModel], ids: KeysView[int] | None = None
) -> Mapping[int, TModel]:
    return {model.id: model for model in models if ids is None or model.id in ids}


def transform_to_id_seq_map(
    models: list[TModel], ids: KeysView[int] | None = None
) -> Mapping[int, Sequence[TModel]]:
    id_seq_map: Mapping[int, list] = defaultdict(list)
    for model in models:
        if ids is None or model.id in ids:
            id_seq_map[model.id].append(model)
    return id_seq_map
