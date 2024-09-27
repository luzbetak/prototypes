import json

#----------------------------------------------------------------------------------------------------------------------#
class WordProcessor:
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.data = json.load(file)

    # 1. Get all the words from the JSON file
    def get_all_words(self):
        """Returns all the words from the JSON file."""
        words = []
        for item in self.data:
            words.extend(item['words'].split())
        return words

    # 2. Log the number of characters for every word (non-unique)
    def log_word_number_of_characters(self, words):
        """Logs every word and the number of characters it contains to a log file (non-unique)."""
        with open('words_number_of_characters.log', 'w') as logfile:
            print("Words and the number of characters it contains (non-unique):")
            for word in words:
                print(f"{word}, {len(word)}")
                logfile.write(f"{word},{len(word)}\n")

    # 3. Log and print words with odd character counts (non-unique)
    def log_words_odd_character_count(self, words):
        """Logs and prints non-unique words with odd character counts to 'odd_words_character_count.log'."""
        with open('words_odd_character_count.log', 'w') as logfile:
            print("\nWords with an odd number of characters (non-unique):")
            for word in words:
                if len(word) % 2 != 0:
                    print(f"{word}, {len(word)}")
                    logfile.write(f"{word},{len(word)}\n")

    # 4. Sort odd words by the number of characters, from least to greatest (non-unique)
    def sort_odd_words_by_character_count(self, words):
        """Sorts words with odd character counts by the number of characters, from least to greatest and logs to a file."""
        # Filter and sort the words with odd character counts
        odd_words = [(word, len(word)) for word in words if len(word) % 2 != 0]
        sorted_odd_words = sorted(odd_words, key=lambda x: x[1])  # Sort by length

        with open('words_sorted_by_odd_character_count.log', 'w') as logfile:
            print("\nOdd words sorted by character count from least to greatest (non-unique):")
            for word, length in sorted_odd_words:
                print(f"{word}, {length}")
                logfile.write(f"{word},{length}\n")

if __name__ == "__main__":

    processor = WordProcessor("words.json")
    words     = processor.get_all_words()
    processor.log_word_number_of_characters(words)
    processor.log_words_odd_character_count(words)
    processor.sort_odd_words_by_character_count(words)

