from typing import Any, Iterable, TypeAlias

import aioinject

Providers: TypeAlias = Iterable[aioinject.Provider[Any]]
