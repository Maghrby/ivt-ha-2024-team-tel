from algorithms.backtrack import (
    add_operators,
    permute_iter,
    anagram,
    array_sum_combinations,
    unique_array_sum_combinations,
    combination_sum,
    get_factors,
    recursive_get_factors,
    find_words,
    generate_abbreviations,
    generate_parenthesis_v1,
    generate_parenthesis_v2,
    letter_combinations,
    palindromic_substrings,
    pattern_match,
    permute_unique,
    permute,
    permute_recursive,
    subsets_unique,
    subsets,
    subsets_v2,
)

import unittest


class TestAddOperator(unittest.TestCase):
    def test_add_operators(self):
        # "123", 6 -> ["1+2+3", "1*2*3"]
        s = "123"
        target = 6
        self.assertEqual(add_operators(s, target), ["1+2+3", "1*2*3"])
        # "232", 8 -> ["2*3+2", "2+3*2"]
        s = "232"
        target = 8
        self.assertEqual(add_operators(s, target), ["2+3*2", "2*3+2"])

        s = "123045"
        target = 3
        answer = ['1+2+3*0*4*5',
                  '1+2+3*0*45',
                  '1+2-3*0*4*5',
                  '1+2-3*0*45',
                  '1-2+3+0-4+5',
                  '1-2+3-0-4+5',
                  '1*2+3*0-4+5',
                  '1*2-3*0-4+5',
                  '1*23+0-4*5',
                  '1*23-0-4*5',
                  '12+3*0-4-5',
                  '12-3*0-4-5']
        self.assertEqual(add_operators(s, target), answer)
    #added
    def test_add_operators_leading_zeros(self):
        self.assertEqual(sorted(add_operators("105", 5)), sorted(["1*0+5", "10-5"]))

    def test_add_operators_large_numbers(self):
        # Assuming it could handle large integers without integer overflow issues.
        self.assertIn("123+456789", add_operators("123456789", 456912))

    def test_add_operators_target_zero(self):
        self.assertEqual(sorted(add_operators("123", 0)), sorted(["1*2*3-6", "1-2+3-2"]))

    def test_add_operators_empty_string(self):
        self.assertEqual(add_operators("", 100), [])

    def test_add_operators_no_possible_solution(self):
        self.assertEqual(add_operators("123", 999), [])

    def test_add_operators_complex_combinations(self):
        s = "123456"
        target = 15
        # Only for demonstration purposes, would need actual outputs from the function
        expected_outputs = ["1+2+3+4+5-6", "12-3-4+5+6"]
        results = add_operators(s, target)
        for expected in expected_outputs:
            self.assertIn(expected, results)


class TestPermuteAndAnagram(unittest.TestCase):

    def test_permute(self):
        perms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        self.assertEqual(perms, permute("abc"))

    def test_permute_iter(self):
        it = permute_iter("abc")
        perms = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
        for i in range(len(perms)):
            self.assertEqual(perms[i], next(it))
   #added
    def test_angram(self):
        self.assertTrue(anagram('apple', 'pleap'))
        self.assertFalse(anagram("apple", "cherry"))
    
    def test_permute_empty(self):
        self.assertEqual(permute(""), [])

    def test_permute_repeated_characters(self):
        perms = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
        self.assertEqual(sorted(permute("aabb")), sorted(perms))

    def test_anagram_empty_strings(self):
        self.assertTrue(anagram('', ''))


class TestArrayCombinationSum(unittest.TestCase):

    def test_array_sum_combinations(self):
        A = [1, 2, 3, 3]
        B = [2, 3, 3, 4]
        C = [2, 3, 3, 4]
        target = 7
        answer = [[1, 2, 4], [1, 3, 3], [1, 3, 3], [1, 3, 3],
                  [1, 3, 3], [1, 4, 2], [2, 2, 3], [2, 2, 3],
                  [2, 3, 2], [2, 3, 2], [3, 2, 2], [3, 2, 2]]
        answer.sort()
        self.assertListEqual(sorted(array_sum_combinations(A, B, C, target)),
                             answer)

    def test_unique_array_sum_combinations(self):
        A = [1, 2, 3, 3]
        B = [2, 3, 3, 4]
        C = [2, 3, 3, 4]
        target = 7
        answer = [(2, 3, 2), (3, 2, 2), (1, 2, 4),
                  (1, 4, 2), (2, 2, 3), (1, 3, 3)]
        answer.sort()
        self.assertListEqual(sorted(unique_array_sum_combinations(A, B, C,
                                                                  target)),
                             answer)

    #added
    def test_array_sum_combinations_empty(self):
        A = []
        B = [2, 3]
        C = [3]
        target = 5
        self.assertEqual(array_sum_combinations(A, B, C, target), [])

    def test_unique_array_sum_combinations_negative_numbers(self):
        A = [1, -2, 3]
        B = [2, -3, 3]
        C = [2, 3]
        target = 3
        expected = [(-2, 3, 2), (1, 2, 0)]
        self.assertListEqual(sorted(unique_array_sum_combinations(A, B, C, target)), sorted(expected))

class TestCombinationSum(unittest.TestCase):

    def check_sum(self, nums, target):
        if sum(nums) == target:
            return (True, nums)
        else:
            return (False, nums)

    def test_combination_sum(self):
        candidates1 = [2, 3, 6, 7]
        target1 = 7
        answer1 = [
            [2, 2, 3],
            [7]
        ]
        self.assertEqual(combination_sum(candidates1, target1), answer1)

        candidates2 = [2, 3, 5]
        target2 = 8
        answer2 = [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ]
        self.assertEqual(combination_sum(candidates2, target2), answer2)
    #added 
    def test_combination_sum_no_combination(self):
        candidates = [3, 4, 7]
        target = 2
        self.assertEqual(combination_sum(candidates, target), [])

    def test_combination_sum_empty_candidates(self):
        candidates = []
        target = 7
        self.assertEqual(combination_sum(candidates, target), [])

class TestFactorCombinations(unittest.TestCase):

    def test_get_factors(self):
        target1 = 32
        answer1 = [
            [2, 16],
            [2, 2, 8],
            [2, 2, 2, 4],
            [2, 2, 2, 2, 2],
            [2, 4, 4],
            [4, 8]
        ]
        self.assertEqual(sorted(get_factors(target1)), sorted(answer1))

        target2 = 12
        answer2 = [
            [2, 6],
            [2, 2, 3],
            [3, 4]
        ]
        self.assertEqual(sorted(get_factors(target2)), sorted(answer2))
        self.assertEqual(sorted(get_factors(1)), [])
        self.assertEqual(sorted(get_factors(37)), [])

    def test_recursive_get_factors(self):
        target1 = 32
        answer1 = [
            [2, 16],
            [2, 2, 8],
            [2, 2, 2, 4],
            [2, 2, 2, 2, 2],
            [2, 4, 4],
            [4, 8]
        ]
        self.assertEqual(sorted(recursive_get_factors(target1)),
                         sorted(answer1))

        target2 = 12
        answer2 = [
            [2, 6],
            [2, 2, 3],
            [3, 4]
        ]
        self.assertEqual(sorted(recursive_get_factors(target2)),
                         sorted(answer2))
        self.assertEqual(sorted(recursive_get_factors(1)), [])
        self.assertEqual(sorted(recursive_get_factors(37)), [])
    
    #added 
    def test_factor_combinations_prime(self):
        target = 13
        self.assertEqual(sorted(get_factors(target)), [])

    def test_factor_combinations_small_numbers(self):
        self.assertEqual(sorted(get_factors(3)), [])
        self.assertEqual(sorted(get_factors(2)), [])


class TestFindWords(unittest.TestCase):

    def test_normal(self):
        board = [
             ['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']
        ]

        words = ["oath", "pea", "eat", "rain"]
        result = find_words(board, words)
        test_result = ['oath', 'eat']
        self.assertEqual(sorted(result),sorted(test_result))

    def test_none(self):
        board = [
             ['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']
        ]

        words = ["chicken", "nugget", "hello", "world"]
        self.assertEqual(find_words(board, words), [])

    def test_empty(self):
        board = []
        words = []
        self.assertEqual(find_words(board, words), [])

    def test_uneven(self):
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e']
        ]
        words = ["oath", "pea", "eat", "rain"]
        self.assertEqual(find_words(board, words), ['eat'])

    def test_repeat(self):
        board = [
            ['a', 'a', 'a'],
            ['a', 'a', 'a'],
            ['a', 'a', 'a']
        ]
        words = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        self.assertTrue(len(find_words(board, words)) == 5)
    
    #added 
    def test_find_words_single_row(self):
        board = [['a', 'b', 'c', 'd']]
        words = ["abcd", "ab", "bc", "cd"]
        self.assertEqual(sorted(find_words(board, words)), sorted(["abcd", "ab", "bc", "cd"]))



class TestGenerateAbbreviations(unittest.TestCase):
    def test_generate_abbreviations(self):
        word1 = "word"
        answer1 = ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3',
                   '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']
        self.assertEqual(sorted(generate_abbreviations(word1)),
                         sorted(answer1))

        word2 = "hello"
        answer2 = ['hello', 'hell1', 'hel1o', 'hel2', 'he1lo', 'he1l1', 'he2o',
                   'he3', 'h1llo', 'h1ll1', 'h1l1o', 'h1l2', 'h2lo', 'h2l1',
                   'h3o', 'h4', '1ello', '1ell1', '1el1o', '1el2', '1e1lo',
                   '1e1l1', '1e2o', '1e3', '2llo', '2ll1', '2l1o', '2l2',
                   '3lo', '3l1', '4o', '5']
        self.assertEqual(sorted(generate_abbreviations(word2)),
                         sorted(answer2))
    
    #added 
    def test_generate_abbreviations_empty(self):
        word = ""
        self.assertEqual(sorted(generate_abbreviations(word)), [""])

    def test_generate_abbreviations_long_string(self):
        word = "word" * 5  # 20 characters
        self.assertEqual(len(generate_abbreviations(word)), 2 ** 20)  # 1,048,576 combinations


class TestPatternMatch(unittest.TestCase):

    def test_pattern_match(self):
        pattern1 = "abab"
        string1 = "redblueredblue"
        pattern2 = "aaaa"
        string2 = "asdasdasdasd"
        pattern3 = "aabb"
        string3 = "xyzabcxzyabc"

        self.assertTrue(pattern_match(pattern1, string1))
        self.assertTrue(pattern_match(pattern2, string2))
        self.assertFalse(pattern_match(pattern3, string3))

    #added 
    def test_pattern_match_non_matching_patterns(self):
        self.assertFalse(pattern_match("aabb", "xyzxyz"))

    def test_pattern_match_repeated_pattern_characters(self):
        self.assertTrue(pattern_match("aabb", "xxxyyy"))


class TestGenerateParenthesis(unittest.TestCase):

    def test_generate_parenthesis(self):
        self.assertEqual(generate_parenthesis_v1(2), ['()()', '(())'])
        self.assertEqual(generate_parenthesis_v1(3), ['()()()', '()(())',
                         '(())()', '(()())', '((()))'])
        self.assertEqual(generate_parenthesis_v2(2), ['(())', '()()'])
        self.assertEqual(generate_parenthesis_v2(3), ['((()))', '(()())',
                         '(())()', '()(())', '()()()'])
    
    #added 
    def test_generate_parenthesis_zero(self):
        self.assertEqual(generate_parenthesis_v1(0), [])
        self.assertEqual(generate_parenthesis_v2(0), [])


class TestLetterCombinations(unittest.TestCase):

    def test_letter_combinations(self):
        digit1 = "23"
        answer1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(letter_combinations(digit1)), sorted(answer1))

        digit2 = "34"
        answer2 = ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']
        self.assertEqual(sorted(letter_combinations(digit2)), sorted(answer2))
    
    #added 
    def test_letter_combinations_empty(self):
        digit = ""
        self.assertEqual(letter_combinations(digit), [])



class TestPalindromicSubstrings(unittest.TestCase):

    def test_palindromic_substrings(self):
        string1 = "abc"
        answer1 = [['a', 'b', 'c']]
        self.assertEqual(palindromic_substrings(string1), sorted(answer1))

        string2 = "abcba"
        answer2 = [['abcba'], ['a', 'bcb', 'a'], ['a', 'b', 'c', 'b', 'a']]
        self.assertEqual(sorted(palindromic_substrings(string2)),
                         sorted(answer2))

        string3 = "abcccba"
        answer3 = [['abcccba'], ['a', 'bcccb', 'a'],
                   ['a', 'b', 'ccc', 'b', 'a'],
                   ['a', 'b', 'cc', 'c', 'b', 'a'],
                   ['a', 'b', 'c', 'cc', 'b', 'a'],
                   ['a', 'b', 'c', 'c', 'c', 'b', 'a']]
        self.assertEqual(sorted(palindromic_substrings(string3)),
                         sorted(answer3))


class TestPermuteUnique(unittest.TestCase):

    def test_permute_unique(self):
        nums1 = [1, 1, 2]
        answer1 = [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
        self.assertEqual(sorted(permute_unique(nums1)), sorted(answer1))

        nums2 = [1, 2, 1, 3]
        answer2 = [[3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3],
                   [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3],
                   [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]
        self.assertEqual(sorted(permute_unique(nums2)), sorted(answer2))

        nums3 = [1, 2, 3]
        answer3 = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2],
                   [1, 3, 2], [1, 2, 3]]
        self.assertEqual(sorted(permute_unique(nums3)), sorted(answer3))


class TestPermute(unittest.TestCase):

    def test_permute(self):
        nums1 = [1, 2, 3, 4]
        answer1 = [[1, 2, 3, 4], [2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1],
                   [1, 3, 2, 4], [3, 1, 2, 4], [3, 2, 1, 4], [3, 2, 4, 1],
                   [1, 3, 4, 2], [3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1],
                   [1, 2, 4, 3], [2, 1, 4, 3], [2, 4, 1, 3], [2, 4, 3, 1],
                   [1, 4, 2, 3], [4, 1, 2, 3], [4, 2, 1, 3], [4, 2, 3, 1],
                   [1, 4, 3, 2], [4, 1, 3, 2], [4, 3, 1, 2], [4, 3, 2, 1]]
        self.assertEqual(sorted(permute(nums1)), sorted(answer1))

        nums2 = [1, 2, 3]
        answer2 = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2],
                   [1, 3, 2], [1, 2, 3]]
        self.assertEqual(sorted(permute(nums2)), sorted(answer2))

    def test_permute_recursive(self):
        nums1 = [1, 2, 3, 4]
        answer1 = [[1, 2, 3, 4], [2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1],
                   [1, 3, 2, 4], [3, 1, 2, 4], [3, 2, 1, 4], [3, 2, 4, 1],
                   [1, 3, 4, 2], [3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1],
                   [1, 2, 4, 3], [2, 1, 4, 3], [2, 4, 1, 3], [2, 4, 3, 1],
                   [1, 4, 2, 3], [4, 1, 2, 3], [4, 2, 1, 3], [4, 2, 3, 1],
                   [1, 4, 3, 2], [4, 1, 3, 2], [4, 3, 1, 2], [4, 3, 2, 1]]
        self.assertEqual(sorted(permute_recursive(nums1)), sorted(answer1))

        nums2 = [1, 2, 3]
        answer2 = [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2],
                   [1, 3, 2], [1, 2, 3]]
        self.assertEqual(sorted(permute_recursive(nums2)), sorted(answer2))


class TestSubsetsUnique(unittest.TestCase):

    def test_subsets_unique(self):
        nums1 = [1, 2, 2]
        answer1 = [(1, 2), (1,), (1, 2, 2), (2,), (), (2, 2)]
        self.assertEqual(sorted(subsets_unique(nums1)), sorted(answer1))

        nums2 = [1, 2, 3, 4]
        answer2 = [(1, 2), (1, 3), (1, 2, 3, 4), (1,), (2,), (3,),
                   (1, 4), (1, 2, 3), (4,), (), (2, 3), (1, 2, 4),
                   (1, 3, 4), (2, 3, 4), (3, 4), (2, 4)]
        self.assertEqual(sorted(subsets_unique(nums2)), sorted(answer2))


class TestSubsets(unittest.TestCase):

    def test_subsets(self):
        nums1 = [1, 2, 3]
        answer1 = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
        self.assertEqual(sorted(subsets(nums1)), sorted(answer1))

        nums2 = [1, 2, 3, 4]
        answer2 = [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4],
                   [1, 3], [1, 4], [1], [2, 3, 4], [2, 3], [2, 4], [2],
                   [3, 4], [3], [4], []]
        self.assertEqual(sorted(subsets(nums2)), sorted(answer2))

    def test_subsets_v2(self):
        nums1 = [1, 2, 3]
        answer1 = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
        self.assertEqual(sorted(subsets_v2(nums1)), sorted(answer1))

        nums2 = [1, 2, 3, 4]
        answer2 = [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4],
                   [1, 3], [1, 4], [1], [2, 3, 4], [2, 3], [2, 4], [2],
                   [3, 4], [3], [4], []]
        self.assertEqual(sorted(subsets_v2(nums2)), sorted(answer2))


if __name__ == '__main__':

    unittest.main()
