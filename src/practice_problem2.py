"""
PRACTICE Exam 2, practice_problem 2.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         Done Ben Hawkins.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Exam 2 question.
#     5 is a "typical" Exam 2 question.
#     7 is a "hard" Exam 2 question.
#    10 is an EXTREMELY hard problem (too hard for an Exam 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
###############################################################################

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_practice_problem2a()
    run_test_practice_problem2b()


###############################################################################
# Students: Some of the testing code below uses a simple testing framework.
# Ask for help if the tests that we supply are not clear to you.
###############################################################################

def run_test_practice_problem2a():
    """ Tests the   practice_problem2a  function. """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this TEST function.
    #   It TESTS the  practice_problem2a  function defined below.
    #   Include at least **   4    ** tests that, taken together,
    #   would form a    ** REASONABLY GOOD test set **
    #   for testing the   practice_problem2a   function defined below.
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    ###########################################################################
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2a   function:')
    print('--------------------------------------------------')

    print("test 1")
    actual = practice_problem2a([2,6,10,2,3], -3)
    expected = [-1, 3, 7, -1, 0]
    print(actual)
    print(expected)

    print("test 2")
    actual = practice_problem2a([0], 0)
    expected = [0]
    print(actual)
    print(expected)

    print("test 3")
    actual = practice_problem2a([0,50,-3, 10], 7)
    expected = [7, 57, 4, 17]
    print(actual)
    print(expected)

    print("test 4")
    actual = practice_problem2a([], -3)
    expected = []
    print(actual)
    print(expected)

def practice_problem2a(sequence, delta):
    """
    What comes in:
      -- A sequence of integers, e.g. ([2, 10, 5, -20, 8])
      -- A number  delta
    What goes out:
      -- Returns a new list that is the same as the given list,
           but with each number in the list having had the given
             delta
           added to it (see example below)
    Side effects: None.
    Example:
       Given the list  [2, 10, 5, -20, 8]  and the number  6,
         this problem returns  [8, 16, 11, -14, 14]
    Type hints:
      :type sequence: [int]
      :type delta:    int
    """
    ###########################################################################
    # Done: 3. Implement and test this function.
    #     WRITE THE TESTS FIRST (above).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      5
    #    TIME ESTIMATE:   5 minutes.
    ###########################################################################
    for k in range(len(sequence)):
        sequence[k] = sequence[k] + delta
    return sequence


def run_test_practice_problem2b():
    """ Tests the   practice_problem2b  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   practice_problem2b  function:')
    print('--------------------------------------------------')

    format_string = '    practice_problem2b( {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 'hBo'
    print_expected_result_of_test([('hello', 'Bye', 'ok joe')], expected,
                                  test_results, format_string)
    actual = practice_problem2b(('hello', 'Bye', 'ok joe'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 'ABCD'
    print_expected_result_of_test([('Alice', 'Bob', 'Carson', 'Devi')],
                                  expected, test_results, format_string)
    actual = practice_problem2b(('Alice', 'Bob', 'Carson', 'Devi'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 'to!'
    print_expected_result_of_test([('', 'tricky', '', 'one, no?', '!')],
                                  expected, test_results, format_string)
    actual = practice_problem2b(('', 'tricky', '', 'one, no?', '!'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 'mom'
    print_expected_result_of_test([('my very long string', 'ok', 'mmmm')],
                                  expected,
                                  test_results, format_string)
    actual = practice_problem2b(('my very long string', 'ok', 'mmmm'))
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    jokes = """
        Q: What is it called when a cat wins a dog show?
        A: A CAT-HAS-TROPHY!

        Q: What do you call a pile of kittens?
        A: a meowntain

        Q: Why don't cats like online shopping?
        A: They prefer a cat-alogue.

        Q: What did the cat say when he lost all his money?
        A: I'm paw!

        Q: Did you hear about the cat who swallowed a ball of yarn?
        A: She had a litter of mittens.

        Q: What do you call a lion who has eaten your mother's sister?
        A: An aunt-eater!

        Q. How do you know when your cat's done cleaning herself?
        A. She's smoking a cigarette.

        source: http://www.jokes4us.com/animaljokes/catjokes.html
        """
    # 5th test: Split  jokes  at spaces to get a list of strings.
    sequence = jokes.split()
    expected = ('QWiicwacwadsAACQWdycapokAamQWdclosAT' +
                'pacQWdtcswhlahmAIpQDyhatcwsaboyAShalom' +
                'QWdycalwheymsAAaQHdykwycdchASsacsh')

    print_expected_result_of_test([sequence], expected, test_results,
                                  format_string)
    actual = practice_problem2b(sequence)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def practice_problem2b(sequence):
    """
    What comes in:
      -- A sequence of strings, e.g. ('hello', 'Bye', 'ok joe')
    What goes out:
      -- Returns the string that contains the first letter in
           each of the strings in the given sequence,
           in the order in which they appear in the sequence.
           (So 'hBo' for the example sequence above).
    Side effects: None.
    Examples:
       Given ['hello', 'Bye', 'ok joe']          returns 'hBo'.
       Given ('Alice, 'Bob', 'Carson', 'Devi')   returns 'ABCD'.
       Given ('', 'tricky', '', 'one, no?', '!') returns 'to!'
       Given [] returns ''
       Given ('my very long string', 'ok', 'mmmm') returns 'mom'
    Type hints:
      :type sequence: [str]
    """
    ###########################################################################
    # Done: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    ###########################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    ###########################################################################
    integer = ""
    for k in range(len(sequence)):
        if len(sequence[k])>0:
            integer = integer + sequence[k][0]
    return integer

###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
