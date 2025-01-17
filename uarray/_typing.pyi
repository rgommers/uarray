"""Helper module with various typing-related utilities."""

from collections.abc import Callable
from typing import Any, Protocol, TypeVar, Iterable, type_check_only

import uarray

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

@type_check_only
class _PySequence(Protocol[_T_co]):
    def __len__(self) -> int: ...
    def __getitem__(self, key: int, /) -> _T_co: ...

@type_check_only
class _SupportsUADomain(Protocol):
    @property
    def __ua_domain__(self) -> str | _PySequence[str]: ...

@type_check_only
class _SupportsUAConvert(Protocol):
    def __ua_convert__(
        self,
        dispatchables: tuple[uarray.Dispatchable, ...],
        coerce: bool,
        /,
    ) -> Iterable[Any]: ...

_ReplacerFunc = Callable[
    [
        tuple[Any, ...],
        dict[str, Any],
        tuple[uarray.Dispatchable, ...],
    ],
    tuple[tuple[Any, ...], dict[str, Any]],
]

_PyGlobalDict = dict[
    str,
    tuple[
        tuple[_T | None, bool, bool],
        list[_T],
        bool,
    ],
]

_PyLocalDict = dict[
    str,
    tuple[
        list[_T],
        list[tuple[_T, bool, bool]],
    ],
]
