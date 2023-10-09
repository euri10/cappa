from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import cappa
from typing_extensions import Annotated

from tests.utils import backends, parse


@backends
def test_positional_arg(backend):
    @dataclass
    class ArgTest:
        numbers: Tuple[int, ...]

    test = parse(ArgTest, "1", "2", "3", "4", backend=backend)
    assert test.numbers == (1, 2, 3, 4)


@backends
def test_option_flag(backend):
    @dataclass
    class ArgTest:
        numbers: Annotated[Tuple[int, ...], cappa.Arg(short=True)]

    test = parse(ArgTest, "-n", "1", "-n", "2", "-n", "3", "-n", "4", backend=backend)
    assert test.numbers == (1, 2, 3, 4)
