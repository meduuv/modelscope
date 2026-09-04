"""Model family filtering."""


def select_by_family(models: list[dict], family: str) -> list[dict]:
    """Select model records whose family matches case-insensitively."""
    target = family.casefold()
    return [model for model in models if str(model.get("family", "")).casefold() == target]
