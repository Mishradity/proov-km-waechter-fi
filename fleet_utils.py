# fleet_utils.py
# Shared formatting and conversion helpers for KM-Waechter.

KM_TO_MILES: float = 0.62137  # 1 km = 0.62137 miles (was 1.609, which is miles-to-km — inverted)


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles for the UK partner report."""
    return km * KM_TO_MILES


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a number as a whole-number percentage string."""
    return f"{int(value)}%"


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list, or 0 if the list is empty."""
    if not values:
        return 0
    return sum(values) / len(values)
