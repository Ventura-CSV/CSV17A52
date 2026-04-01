from __future__ import annotations


def get_inverse(mapping: dict, target: set) -> dict:
    """Return f⁻¹ as a dict. Raise ValueError if f is not bijective."""
    # === TODO START ===
    values = list(mapping.values())
    if len(values) != len(set(values)):
        raise ValueError("Function is not injective — inverse is not well-defined.")
    if set(values) != target:
        raise ValueError("Function is not surjective — inverse is not well-defined.")
    return {v: k for k, v in mapping.items()}
    # === TODO END ===


def compose(f: dict, g: dict) -> dict:
    """Return f∘g as a dict (apply g first, then f).
    For each key x in g, compute f(g(x)).
    Raise ValueError if g(x) is not in f's domain.
    """
    # === TODO START ===
    result = {}
    for x, gx in g.items():
        if gx not in f:
            raise ValueError(f"g({x})={gx} is not in f's domain.")
        result[x] = f[gx]
    return result
    # === TODO END ===
