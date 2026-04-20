"""
src/checks.py — Exercise validation helpers for llm-research-lab.

These functions are used in notebook check cells to give clear, beginner-friendly
feedback when exercise answers are right or wrong.

Usage in a notebook:
    import sys
    sys.path.insert(0, "../../")   # adjust path depth as needed
    from src.checks import check_equal, check_type, check_contains
"""


def check_equal(actual, expected, label="Check"):
    """Assert that actual == expected, with a friendly message."""
    if actual == expected:
        print(f"✓ {label} passed!")
    else:
        raise AssertionError(
            f"✗ {label} failed.\n"
            f"  Expected: {expected!r}\n"
            f"  Got:      {actual!r}"
        )


def check_type(value, expected_type, label="Type check"):
    """Assert that value is an instance of expected_type."""
    if isinstance(value, expected_type):
        print(f"✓ {label} passed! (type is {type(value).__name__})")
    else:
        raise AssertionError(
            f"✗ {label} failed.\n"
            f"  Expected type: {expected_type.__name__}\n"
            f"  Got type:      {type(value).__name__}"
        )


def check_contains(container, item, label="Contains check"):
    """Assert that item is in container."""
    if item in container:
        print(f"✓ {label} passed! ({item!r} is present)")
    else:
        raise AssertionError(
            f"✗ {label} failed.\n"
            f"  Expected {item!r} to be in {container!r}"
        )


def check_not_contains(container, item, label="Not-contains check"):
    """Assert that item is NOT in container."""
    if item not in container:
        print(f"✓ {label} passed! ({item!r} is absent)")
    else:
        raise AssertionError(
            f"✗ {label} failed.\n"
            f"  Expected {item!r} NOT to be in {container!r}"
        )


def check_approx(actual, expected, tolerance=1e-6, label="Approximate check"):
    """Assert that actual ≈ expected within a tolerance (for floats)."""
    if abs(actual - expected) <= tolerance:
        print(f"✓ {label} passed! ({actual} ≈ {expected})")
    else:
        raise AssertionError(
            f"✗ {label} failed.\n"
            f"  Expected: {expected} (± {tolerance})\n"
            f"  Got:      {actual}\n"
            f"  Difference: {abs(actual - expected)}"
        )


def check_length(sequence, expected_length, label="Length check"):
    """Assert that len(sequence) == expected_length."""
    actual_length = len(sequence)
    if actual_length == expected_length:
        print(f"✓ {label} passed! (length is {actual_length})")
    else:
        raise AssertionError(
            f"✗ {label} failed.\n"
            f"  Expected length: {expected_length}\n"
            f"  Got length:      {actual_length}"
        )


def check_keys(dictionary, expected_keys, label="Keys check"):
    """Assert that a dict has exactly the expected keys."""
    actual_keys = set(dictionary.keys())
    expected_keys = set(expected_keys)
    if actual_keys == expected_keys:
        print(f"✓ {label} passed! (keys: {sorted(actual_keys)})")
    else:
        missing = expected_keys - actual_keys
        extra = actual_keys - expected_keys
        msg = f"✗ {label} failed.\n"
        if missing:
            msg += f"  Missing keys: {sorted(missing)}\n"
        if extra:
            msg += f"  Unexpected keys: {sorted(extra)}\n"
        raise AssertionError(msg)


def check_all_pass(checks_list, label="All checks"):
    """
    Run a list of (function, args) tuples. Report which pass/fail.

    Example:
        check_all_pass([
            (check_equal, (my_result, 42, "result is 42")),
            (check_type, (my_result, int, "result is int")),
        ])
    """
    passed = 0
    failed = 0
    for fn, args in checks_list:
        try:
            fn(*args)
            passed += 1
        except AssertionError as e:
            print(str(e))
            failed += 1
    print(f"\n{label}: {passed} passed, {failed} failed.")
    if failed > 0:
        raise AssertionError(f"{failed} check(s) failed.")
