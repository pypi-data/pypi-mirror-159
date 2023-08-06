from __future__ import annotations
from typing import Callable
import random


class Result:
    def __init__(
        self, rolls: list[int] = [], modifier: int = 0, dice_modifier: int = 0
    ) -> None:
        self._rolls: list[int] = rolls
        self._modifier: int = modifier
        self._dice_modifier: int = dice_modifier

    def __int__(self) -> int:
        return self.get_total()

    def __add__(self, other: Result) -> Result:
        return Result(self._rolls + other._rolls)

    def __iadd__(self, other: Result) -> Result:
        self._rolls.extend(other._rolls)
        return self

    def get_rolls(self) -> list[int]:
        return self._rolls

    def add_rolls(self, rolls:list[int]) -> None:
        self._rolls.extend(rolls)

    def get_total(self) -> int:
        return sum(self._rolls) + self._modifier

    def filter(
        self, filter_func: Callable[[int, int], bool], target: int
    ) -> Result:
        return Result(
            [roll for roll in self._rolls if filter_func(roll, target)]
        )


class Dice:
    def __init__(
        self, lower_limit: int, upper_limit: int, modifier: int = 0
    ) -> None:
        self._lower_limit: int = lower_limit
        self._upper_limit: int = upper_limit
        self._modifier: int = modifier

    def __neg__(self) -> Dice:
        return Dice(-self._upper_limit, -self._lower_limit, -self._modifier)

    def __eq__(self, other: Dice) -> bool:
        return (
            self._lower_limit == other._lower_limit
            and self._upper_limit == other._upper_limit
            and self._modifier == other._modifier
        )

    def __ne__(self, other: Dice) -> bool:
        return (
            self._lower_limit != other._lower_limit
            or self._upper_limit != other._upper_limit
            or self._modifier != other._modifier
        )

    def __add__(self, other: int) -> Dice:
        return Dice(
            self._lower_limit, self._upper_limit, self._modifier + other
        )

    def __radd__(self, other: int) -> Dice:
        return self.__add__(other)

    def __sub__(self, other: int) -> Dice:
        return self.__add__(-other)

    def __rsub__(self, other: int) -> Dice:
        return (self.__neg__().__add__(other))

    def __mul__(self, other: int) -> MultiDice:
        return MultiDice(
            self._lower_limit, self._upper_limit, other, self._modifier * other
        )

    def __rmul__(self, other: int) -> MultiDice:
        return self.__mul__(other)

    def _get_single_roll(self) -> int:
        return random.randint(self._lower_limit, self._upper_limit)

    def roll(self, modifier: int = 0) -> Result:
        return Result([self._get_single_roll()], self._modifier + modifier)

    def rollmany(self, amount: int) -> Result:
        return Result([self._get_single_roll() for _ in range(amount)])


class MultiDice(Dice):
    def __init__(
        self, lower_limit: int, upper_limit: int,
        amount: int, modifier: int = 0
    ) -> None:
        super().__init__(lower_limit, upper_limit, modifier)

        self._amount: int = amount

    def __mul__(self, other: int) -> MultiDice:
        return super().__mul__(self._amount * other)

    def roll(self) -> Result:
        return super().rollmany(self._amount)

    def rollmany(self, amount: int) -> Result:
        return super().rollmany(self._amount * amount)


D4 = Dice(1, 4)
D6 = Dice(1, 6)
D8 = Dice(1, 8)
D10 = Dice(1, 10)
D12 = Dice(1, 12)
D20 = Dice(1, 20)
D100 = Dice(1, 100)
