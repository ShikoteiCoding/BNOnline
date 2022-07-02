
def parse_name(config: dict) -> str | None:
    return config.get("name")

def parse_structure(config: dict) -> str | None:
    return config.get("structure")