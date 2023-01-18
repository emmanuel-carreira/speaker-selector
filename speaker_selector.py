from random import shuffle
from typing import List

from working_front import WorkingFront


class SpeakerSelector:
    def __init__(self, fronts: List[WorkingFront]) -> None:
        shuffle(fronts)
        self.fronts = fronts

    def speakers(self) -> List[str]:
        selected_speakers = [front.random_member() for front in self.fronts]
        return selected_speakers
