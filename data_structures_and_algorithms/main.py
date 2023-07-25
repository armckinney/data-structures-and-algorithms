from typing import List

from data_structures_and_algorithms.core import JsonConfigurationProvider
from data_structures_and_algorithms.sneks import CoolSnek, NormalSnek, Snek

CONFIG_FILE = "/workspaces/data-structures-and-algorithms/data_structures_and_algorithms/config/config.json"


def main(snek_type: str) -> None:
    snek_types: List[Snek] = [CoolSnek(), NormalSnek()]

    for snek in snek_types:
        if snek.snek_type == snek_type:
            snek.show_snek()


if __name__ == "__main__":
    config = JsonConfigurationProvider(CONFIG_FILE)
    snek_type = config.get("snek_type")

    main(snek_type)


