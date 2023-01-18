import math
import unittest

from main import main


class MainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.people = [
            ['a', 'b', 'c'],
            ['d'],
            ['e', 'f']
        ]

    def test_happy_path(self):
        speakers = main(self.people)

        self.assertEqual(len(speakers), 3)
        self.assertTrue(all(isinstance(speaker, str) for speaker in speakers))

    def test_only_one_speaker_of_each_working_front_is_selected(self):
        selected_speakers = main(self.people)

        for speaker in selected_speakers:
            speaker_working_front = [working_front for working_front in self.people
                                     if speaker in working_front][0]
            working_front_without_selected_speaker = [person for person in speaker_working_front
                                              if person != speaker]
            for speaker_not_chosen in working_front_without_selected_speaker:
                self.assertTrue(speaker_not_chosen not in selected_speakers)

    def test_speaker_in_the_same_working_front_has_the_same_chance_of_being_selected(self):
        expected_probabilities = {
            'a': 1/3,
            'b': 1/3,
            'c': 1/3,
            'd': 1,
            'e': 1/2,
            'f': 1/2,
        }
        total_replications = 1000000
        times_selected = {person: 0 for person in ['a', 'b', 'c', 'd', 'e', 'f']}

        for _ in range(total_replications):
            selected_speakers = main(self.people)
            for selected_speaker in selected_speakers:
                times_selected[selected_speaker] += 1

        calculated_probabilities = {person: times_selected[person]/total_replications
                                    for person in ['a', 'b', 'c', 'd', 'e', 'f']}

        for person, calculated_probability in calculated_probabilities.items():
            expected_probability = expected_probabilities[person]
            self.assertTrue(math.sqrt((expected_probability - calculated_probability)**2) < 0.001)

    def test_should_mix_working_fronts_speakers_order(self):
        total_replications = 100000
        times_selected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for _ in range(total_replications):
            selected_speakers = main(self.people)

            for position, speaker in enumerate(selected_speakers):
                for working_group_index, working_group in enumerate(self.people):
                    if speaker in working_group:
                        times_selected[working_group_index][position] += 1

        for working_group in times_selected:
            for speaker_selected_order in working_group:
                speaker_selected_order_probability = speaker_selected_order/total_replications
                
                self.assertTrue(math.sqrt((speaker_selected_order_probability - 1/3)**2) < 0.01)
