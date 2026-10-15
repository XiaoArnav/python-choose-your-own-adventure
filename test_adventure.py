import io
import unittest
from unittest.mock import patch

import adventure


class AdventureTests(unittest.TestCase):
    def test_get_choice_reprompts_for_invalid_input(self):
        with patch("builtins.input", side_effect=["hello", "0", "2"]):
            with patch("sys.stdout", new_callable=io.StringIO) as fake_stdout:
                choice = adventure.get_choice("Pick one", ["A", "B", "C"])

        self.assertEqual(choice, 2)
        output = fake_stdout.getvalue()
        self.assertEqual(output.count("Please enter a number from 1 to 3."), 2)

    def test_play_game_reports_win_and_score(self):
        # Path 1 (forest) -> choice 1 (win)
        with patch("builtins.input", side_effect=["1", "1"]):
            with patch("sys.stdout", new_callable=io.StringIO) as fake_stdout:
                result, score = adventure.play_game()

        self.assertEqual(result, "win")
        self.assertEqual(score, adventure.WIN_SCORE)
        output = fake_stdout.getvalue()
        self.assertIn("You won this adventure!", output)
        self.assertIn("Final score: 2", output)

    def test_play_game_reports_survive_and_score(self):
        # Path 3 (river) -> choice 3 (survive)
        with patch("builtins.input", side_effect=["3", "3"]):
            with patch("sys.stdout", new_callable=io.StringIO) as fake_stdout:
                result, score = adventure.play_game()

        self.assertEqual(result, "survive")
        self.assertEqual(score, adventure.SURVIVE_SCORE)
        output = fake_stdout.getvalue()
        self.assertIn("You survived this adventure!", output)
        self.assertIn("Final score: 1", output)


if __name__ == "__main__":
    unittest.main()
