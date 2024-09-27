# Word Processor Application

## Exercise

1. In code, get all the words within the [sample data](words.json) into an object or data structure that you can manipulate.
2. Log the number of characters for every word within the "words" key in the sample data.
3. Print an additional log for all words where the number of characters in the word is an odd number.
4. Sort the resulting words from step 3 according to the number of characters in each of them, from least to greatest.
5. Include a README.md explaining how to run your code and tests.

## Project Requirements

1. **Extract Words**: In code, get all the words from the `words.json` sample data into an object or data structure that you can manipulate.
2. **Log Word Character Counts**: Log the number of characters for every word within the "words" key in the sample data.
3. **Log Odd Character Words**: Print an additional log for all words where the number of characters in the word is an odd number.
4. **Sort Odd Character Words**: Sort the resulting words from step 3 according to the number of characters in each of them, from least to greatest.
5. **Provide Documentation**: Include a README.md (this file) explaining how to run the code and tests.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- `unittest` library (comes with the Python standard library)
- A terminal/command line

## Files in the Project

- `word_processor.py`: The main Python script that processes the words.
- `test_word_processor.py`: The test script that verifies the functionalities in `word_processor.py`.
- `words.json`: The input data file that contains the words to be processed.
- `README.md`: This file, providing instructions on how to run the application and tests.
- Generated Log Files (non-unique):
  - `words_number_of_characters.log`
  - `words_odd_character_count.log`
  - `words_sorted_by_odd_character_count.log`

## How to Run the Code

1. **Clone the repository or download the files**:
   - Ensure you have `word_processor.py`, `test_word_processor.py`, and `words.json` in the same directory.

2. **Run the `word_processor.py` script**:
   You can run the main script to process the words and generate the required log files.

   ```bash
   python word_processor.py
   ```

   This will generate the following log files:
   - `words_number_of_characters.log`: Contains every word and its number of characters.
   - `words_odd_character_count.log`: Contains only words with an odd number of characters.
   - `words_sorted_by_odd_character_count.log`: Contains odd character words sorted by their character count.

3. **How to Run the Unit Tests**:

    Ensure that `test_word_processor.py` is in the same directory as `word_processor.py` and `words.json`. Then, follow these steps:

    - Open a terminal or command line.
    - Run the following command to execute the test suite using the `unittest` module:

    ```bash
    python -m unittest test_word_processor.py 
    ```
