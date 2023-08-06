# voladice

A Python package for dice rolling and result manipulation.

## How it works

Voladice is simple in its nature, following a three-step process:

- Create `Dice` or use the already available `D4`, `D6`, `D8`, `D10`, `D12`,
  `D20` and `D100` constants, then roll them to get...
- ...`Result`s! You can combine `Result` objects in many ways, and also filter
  them by providing filter functions (or using the already available `filter`
  functions) and target values, and then...
- ...extract values from the `Results` such as the individual rolls with
  `get_rolls()` or the sum of all rolls (total) with `get_total()` (you can
  also get this by converting the `Result` object to an `int`).

