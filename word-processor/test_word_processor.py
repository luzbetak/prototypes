import unittest
import os
from word_processor import WordProcessor

class TestWordProcessor(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Initialize the processor with the JSON file."""
        cls.processor = WordProcessor("words.json")
        cls.words = cls.processor.get_all_words()
        
    def test_get_all_words(self):
        """Test that words are extracted correctly from the JSON file."""
        words = self.processor.get_all_words()
        self.assertGreater(len(words), 0, "The word list should not be empty.")
        self.assertIn("Lorem", words, "'Lorem' should be present in the words list.")

    def test_log_word_number_of_characters(self):
        """Test that word character counts are logged correctly."""
        self.processor.log_word_number_of_characters(self.words)
        self.assertTrue(os.path.exists("words_number_of_characters.log"), "Log file should exist.")
        
        with open("words_number_of_characters.log", "r") as logfile:
            lines = logfile.readlines()
            self.assertGreater(len(lines), 0, "Log file should contain entries.")
            self.assertIn("Lorem,5\n", lines, "'Lorem,5' should be in the log file.")

    def test_log_words_odd_character_count(self):
        """Test that words with odd character counts are logged correctly."""
        self.processor.log_words_odd_character_count(self.words)
        self.assertTrue(os.path.exists("words_odd_character_count.log"), "Odd character log file should exist.")
        
        with open("words_odd_character_count.log", "r") as logfile:
            lines = logfile.readlines()
            self.assertGreater(len(lines), 0, "Log file should contain entries.")

            # Verify at least one odd word length is logged
            self.assertIn("Lorem,5\n", lines, "'Lorem,5' should be in the odd character count log file.")

    def test_sort_odd_words_by_character_count(self):
        """Test that the words in 'words_sorted_by_odd_character_count.log' are sorted by word length."""
    
        # Run the sorting method
        self.processor.sort_odd_words_by_character_count(self.words)
    
        with open("words_sorted_by_odd_character_count.log", "r") as logfile:
            lines = logfile.readlines()
            sorted_lengths = [int(line.split(',')[1].strip()) for line in lines]
    
            # Check that the list of word lengths is sorted in ascending order
            self.assertEqual(sorted_lengths, sorted(sorted_lengths), "Words in the log should be sorted by length.")



if __name__ == "__main__":
    unittest.main()

