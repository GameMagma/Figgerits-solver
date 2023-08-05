import nltk
from nltk.corpus import words
import re

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


def find_solution(blanks, nums):
    """
    This method uses the list of words that have already been solved and the numbers that have been found using the
    previous methods to find the final solution.

    :param blanks: A list of each group of blanks, consisting of a number of blanks for the solution to the puzzle
    :param nums: The numbers associated with the blanks
    :return: The solution
    """
    pass


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


def format_list(input_list: list) -> str:
    """
    This takes a list and formats it to be a string formatted as a neat, comma-delimited list.
    :param input_list: The list to format
    :return: The formatted list
    """
    return ", ".join([str(x) for x in input_list])


if __name__ == '__main__':
    flag = True
    while flag:
        userIn = input("\nSolve for solution (s), key (k), or word (w)? Enter now: ").strip().lower()
        # Can't do "w" or "word" with match-case statements, but this is more efficient and nobody but me will use this
        match userIn:
            case "w":
                # Attempt to solve word
                nums = []  # Variable containing mystery word's pattern

                # Get the letters in the word
                wordNums = input("\nEnter only the numbers in the order they're shown, separated by spaces: ").strip()
                for number in wordNums.split():
                    nums.append(int(number))

                results = find_word(nums)
                print(f"{len(results)} possible words")
                print(f"Possible words: {format_list(results)}")
            case "s":
                # Attempt to solve solution
                pass
            case "k":
                # Enter into key
                user_in = input(
                    "Enter a number followed by a space and then the letter it's associated with, separating"
                    " each entry with commas, like this: 1 a, 2 b, 3 c, 4 d, 5 e. Enter now: ").strip(",. ").lower()

                key_groups = user_in.split(",")  # Split the string into a list of groups, like ["1 a", "2 b"...]

                # Check to make sure each group follows the regex, then add it to the letter_key. If it doesn't fit,
                # notify the user and toss it out.
                for group in key_groups:
                    group = group.strip()
                    if re.search('^[0-9]+ [a-z]$', group):
                        num, char = group.split()    # Split the number and letter into two variables
                        letter_key[int(num)] = char  # Add the relation to the dictionary
                    else:
                        print(f"Group {group} is invalid.")  # Didn't fit the regex. Notify the user and move on.

                print(f"New key: {letter_key}")
            case _:
                flag = False

# TODO: Write find_solution (look for each individual word then use AI to check for coherent sentences?)
# TODO: Have program utilize key to further rule out impossible words
# TODO: Use AI to look at the clue and the list of possible words to see the most likely candidate(?)
# TODO: Allow user to enter letters in addition to numbers to rule out words For example: Word is "test", you have "T",
    # TODO: ^ then you would enter "T 2 3 T" and program would rule
