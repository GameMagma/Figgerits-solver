import nltk
from nltk.corpus import words

nltk.download('words')
word_list = words.words()

letter_key = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: '', 10: '', 11: '', 12: '', 13: '', 14: '',
              15: '', 16: '', 17: '', 18: '', 19: '', 20: '', 21: '', 22: '', 23: '', 24: '', 25: '', 26: ''}


def find_word(nums: list) -> list:
    """
    This method uses the blanks and numbers provided to guess what the word could be

    :param nums: The numbers associated with the blanks
    :return: The word
    """

    possible_words = [word for word in word_list if (len(nums) == len(word)) and pattern_matcher(word, nums)]
    print(f"In findWord: {possible_words}")
    return possible_words


def pattern_matcher(word, pattern):
    """
    This function checks if a given word matches a given numerical pattern without converting the pattern to sequential numbers.
    For example, "test" matches the pattern [1, 2, 3, 1].
    :param word: Proposed word to check
    :param pattern: Given pattern
    """

    pattern = fix_pattern(pattern)

    


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

        print(find_word(nums))
        print(f"Final letter key: {letter_key}")
    else:
        exit(0)
