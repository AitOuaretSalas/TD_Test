from dataclasses import dataclass
from typing import Sequence

@dataclass
class Pizza:
    name: str
    price: float
    description: str
    ingredients: Sequence[str]
    base: str

