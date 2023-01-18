from random import randint

from dataclasses import dataclass
from typing import List


@dataclass
class WorkingFront:
    members: List[str]

    @property
    def total_members(self) -> int:
        return len(self.members)

    def random_member(self) -> str:
        index = randint(0, self.total_members-1)
        return self.members[index]
