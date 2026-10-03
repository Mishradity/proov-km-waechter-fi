# test_km_wachter.py
from km_wachter import needs_service, wear_percent, SERVICE_INTERVAL_KM, WARN_AT_PERCENT


def test_almost_due_car_is_flagged():
    # A car at 14,900 of its 15,000 km window is about 99% worn and MUST be flagged.
    assert needs_service({"id": "VOS-4471", "odometer": 14900, "last_service_km": 0}) is True


def test_missing_reading_is_not_treated_as_zero():
    # A car with NO last-service reading must not be treated as fully worn.
    assert needs_service({"id": "VOS-7788", "odometer": 92000}) is False


def test_wear_percent_uses_float_division():
    """Prove the wear calculation uses true (float) division, not integer division.

    14,900 / 15,000 * 100 = 99.33...  — integer division would give 0.
    Also confirms the warning threshold and interval are untouched.
    """
    pct = wear_percent(14900, SERVICE_INTERVAL_KM)
    assert 99.0 < pct < 100.0, f"Expected ~99.3 %, got {pct:.2f} %"
    # Sanity-check constants are still the mandated values
    assert SERVICE_INTERVAL_KM == 15000
    assert WARN_AT_PERCENT == 80
