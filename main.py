from typing import List

from speaker_selector import SpeakerSelector
from working_front import WorkingFront


def main(people: List[List[str]]):
    fronts = [WorkingFront(members) for members in people]
    selector = SpeakerSelector(fronts)
    return selector.speakers()


if __name__ == '__main__':
    speakers = main([
        ['this', 'is', 'an'],
        ['example', 'of', 'use', 'case.'],
        ['set', 'your', 'own', 'group', 'of', 'people', 'accordingly.']
    ])
    print(', '.join(speakers))
