import pytest
from main import get_inverse, compose

# ── shared test data ──────────────────────────────────────────────────────────

bij   = {1: 'a', 2: 'b', 3: 'c'}
bij_T = {'a', 'b', 'c'}

inj   = {1: 'a', 2: 'b'}
inj_T = {'a', 'b', 'c'}

sur   = {1: 'a', 2: 'b', 3: 'a'}
sur_T = {'a', 'b'}

f1 = {'a': 1, 'b': 2, 'c': 3}
g1 = {1: 'a', 2: 'b', 3: 'c'}

f2 = {'a': 'x', 'b': 'y'}
g2 = {1: 'a', 2: 'b'}

# ── T1: inverse of bijective function ────────────────────────────────────────

@pytest.mark.T1
def test_inverse_correct():
    assert get_inverse(bij, bij_T) == {'a': 1, 'b': 2, 'c': 3}

@pytest.mark.T1
def test_inverse_single():
    assert get_inverse({1: 'x'}, {'x'}) == {'x': 1}

@pytest.mark.T1
def test_inverse_round_trip():
    inv = get_inverse(bij, bij_T)
    for k, v in bij.items():
        assert inv[v] == k

# ── T2: inverse raises on non-bijective ──────────────────────────────────────

@pytest.mark.T2
def test_inverse_not_injective():
    with pytest.raises(ValueError):
        get_inverse(sur, sur_T)

@pytest.mark.T2
def test_inverse_not_surjective():
    with pytest.raises(ValueError):
        get_inverse(inj, inj_T)

@pytest.mark.T2
def test_inverse_empty():
    assert get_inverse({}, set()) == {}

# ── T3: compose basic ────────────────────────────────────────────────────────

@pytest.mark.T3
def test_compose_basic():
    result = compose(f1, g1)
    assert result == {1: 1, 2: 2, 3: 3}

@pytest.mark.T3
def test_compose_different_types():
    result = compose(f2, g2)
    assert result == {1: 'x', 2: 'y'}

@pytest.mark.T3
def test_compose_single():
    result = compose({'a': 1}, {1: 'a'})
    assert result == {1: 1}

# ── T4: compose edge cases ──────────────────────────────────────────────────

@pytest.mark.T4
def test_compose_empty():
    assert compose({}, {}) == {}

@pytest.mark.T4
def test_compose_domain_mismatch():
    with pytest.raises(ValueError):
        compose({'a': 1}, {1: 'z'})

@pytest.mark.T4
def test_compose_chain():
    h = {1: 'a', 2: 'b'}
    k = {'a': 'x', 'b': 'y'}
    result = compose(k, h)
    assert result == {1: 'x', 2: 'y'}
