# CSV17A52
CSV17 Assignment 5-2: Inverse Functions & Composition

## Overview
Implement two functions: computing the inverse of a bijective function and composing two functions. Covers Zybook Chapter 5 (Sections 5.4–5.5).

## Functions to Implement
- `get_inverse(mapping: dict, target: set) -> dict` — Return f⁻¹. Raise ValueError if not bijective.
- `compose(f: dict, g: dict) -> dict` — Return f∘g (apply g first, then f). Raise ValueError if g(x) not in f's domain.

## Test Cases
| Test | Description |
|------|-------------|
| T1 | Inverse of bijective functions |
| T2 | Inverse raises on non-bijective |
| T3 | Compose basic cases |
| T4 | Compose edge cases and errors |

## How to Test
```
python -m pytest main_test.py -v
```
