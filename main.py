import nltk
from nltk.corpus import words

nltk.download('words')     # Download English dictionary
word_list = words.words()  # Assign English dictionary to word_list

# The full letter-to-number key
letter_key = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: '',
              15: '', 16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: ''}


def find_word(pattern: list) -> list:
    """
    This method uses the blanks and numbers provided to guess what the word could be

    :param pattern: The numbers associated with the blanks
    :return: The word
    """

    possible_words = [word for word in word_list if (len(pattern) == len(word)) and is_matching(word, pattern)]
    # print(f"In findWord: {possible_words}")  # Debugging
    return possible_words


def is_matching(proposed_word, pattern) -> bool:
    """
    This function checks if a given word matches a given numerical pattern by mapping the word to its own pattern and
    comparing them.
    For example, "test" matches the pattern [1, 2, 3, 1].
    :param proposed_word: Proposed word to check
    :param pattern: Given pattern
    """

    pattern = fix_pattern(pattern)  # Fix pattern to sequential numbers
    letter_map = {}                 # Letter is the key, number is the value
    proposed_word_pattern = []      # The numerical pattern of the proposed word
    current_letter_num = 1          # Current number

    # Check if the pattern and the words both have the same length
    if len(pattern) != len(proposed_word):
        return False

    # Map the word to its own pattern, then return the comparison

    # For every letter in the word,
    #   Check if the letter is in the map already
    #       If not, use current_letter_num to assign that letter a number, then increment it
    #   Add the number to proposed_word_pattern
    for letter in proposed_word:
        if letter not in letter_map:
            letter_map[letter] = current_letter_num
            current_letter_num += 1
        proposed_word_pattern.append(letter_map[letter])

    # print(f"Proposed_word_pattern: {proposed_word_pattern} vs. pattern: {pattern}")  # Debugging
    return proposed_word_pattern == pattern


def fix_pattern(pattern: list) -> list:
    """
    This method takes a list of numbers and returns a new list where the numbers are made sequential.

    :param pattern: The original list of numbers
    :return: A new list of numbers made sequential
    """

    # Get the unique numbers in the original order
    sorted_unique_nums = sorted(set(pattern), key=pattern.index)

    # Create a mapping from original numbers to their new sequential values
    mapping = {num: index + 1 for index, num in enumerate(sorted_unique_nums)}

    # Transform the original list using the mapping
    return [mapping[num] for num in pattern]


def find_solution(blanks, nums):
    """
    This method uses the list of words that have already been solved and the numbers that have been found using the
    previous methods to find the final solution.

    :param blanks: A list of each group of blanks, consisting of a number of blanks for the solution to the puzzle
    :param nums: The numbers associated with the blanks
    :return: The solution
    """
    pass


if __name__ == '__main__':
    print("Solve for solution or word?")
    userIn = input().strip().lower()
    if (userIn == "w") or (userIn == "word"):
        nums = []

        # Get the letters in the word
        wordNums = input("\nEnter only the numbers in the order they're shown, separated by spaces: ").strip()
        for number in wordNums.split():
            nums.append(int(number))

        print(f"Possible words: {find_word(nums)}")  # TODO: make the list print prettier
        # print(f"Final letter key: {letter_key}")  # Not implemented yet
    else:
        exit(0)

# TODO: Allow user to enter letters into the key so that the program can find a solution
# TODO: Have program utilize key to further rule out impossible words
# TODO: Allow user to enter letters in addition to numbers to rule out words For example: Word is "test", you have "T",
    # TODO: ^ then you would enter "T 2 3 T" and program would rule
