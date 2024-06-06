from skeleton_file import *

import unittest
import collections as cl

class TestFunctions(unittest.TestCase):
    # 4A
    def test_union_strings(self):
        self.assertEqual(cl.Counter(union_strings("abc", "def")), cl.Counter("abcdef"))
        self.assertEqual(cl.Counter(union_strings("abc", "abc")), cl.Counter("abc"))
        self.assertEqual(cl.Counter(union_strings("", "")), cl.Counter(""))
        self.assertEqual(cl.Counter(union_strings("", "abc")), cl.Counter("abc"))
        self.assertEqual(cl.Counter(union_strings("abc", "")), cl.Counter("abc"))

    # 4B
    def test_format_str(self):
        self.assertEqual(format_str("a?b?c", "123"), "a123b123c")
        self.assertEqual(format_str("a?b?c", "?"), "a?b?c")
        self.assertEqual(format_str("a?b???c", ""), "abc")

    # 4C
    def test_least_pal(self):
        self.assertEqual(least_pal("abba"), 0)
        self.assertEqual(least_pal("abca"), 1)
        self.assertEqual(least_pal("abc"), 1)
        self.assertEqual(least_pal("a"), 0)
        self.assertEqual(least_pal("ab"), 1)
        self.assertEqual(least_pal("abc ba"), 1)
        self.assertEqual(least_pal(""), 0)

    # 4D
    def test_least_frequent(self):
        self.assertEqual(least_frequent("aabcc"), "b")
        self.assertEqual(least_frequent('aea.. e'), " ")
        self.assertEqual(least_frequent("zzz"), "z")
        self.assertEqual(least_frequent("aabbbc"), "c")
        self.assertEqual(least_frequent("aabbccd"), "d")
        self.assertEqual(least_frequent("mississippi"), "m")
        self.assertEqual(least_frequent("dabracadabra"), "c")
        self.assertEqual(least_frequent("1231122334"), "4")

    def test_least_frequent_edge_cases(self):
        self.assertEqual(least_frequent("   "), " ")
        self.assertEqual(least_frequent("12233"), "1")
        self.assertEqual(least_frequent("!@#$$@!"), "#")
        self.assertEqual(least_frequent("a"), "a")
        self.assertEqual(least_frequent(""), None)

    # 4E
    def test_common_suffix(self):
        self.assertEqual(longest_common_suffix(["abc", "defbc", "bc"]), "bc")
        self.assertEqual(longest_common_suffix(["hello", "yello", "mello"]), "ello")
        self.assertEqual(longest_common_suffix(["running", "jogging", "walking"]), "ing")
        self.assertEqual(longest_common_suffix(["apple", "battle", "cattle"]), "le")
        self.assertEqual(longest_common_suffix(["case", "base", "face"]), "e")
        self.assertEqual(longest_common_suffix(["hiking", "biking", "iking"]), "iking")
        self.assertEqual(longest_common_suffix(["end", "bend", "tend"]), "end")
        self.assertEqual(longest_common_suffix(["test", "jest", "best"]), "est")
        self.assertEqual(longest_common_suffix(["night", "fight", "sight"]), "ight")
        self.assertEqual(longest_common_suffix([""]), "")
        
    def test_no_common_suffix(self):
        self.assertEqual(longest_common_suffix(["abc", "def", "ghi"]), "")
        self.assertEqual(longest_common_suffix(["apple", "banana", "cherry"]), "")
        self.assertEqual(longest_common_suffix(["a", "b", "c"]), "")
        
    def test_mixed_length_strings(self):
        self.assertEqual(longest_common_suffix(["short", "longest", "shortest"]), "t")
        self.assertEqual(longest_common_suffix(["car", "scar", "far"]), "ar")
        self.assertEqual(longest_common_suffix(["back", "rack", "stack"]), "ack")
        
    def test_empty_string_in_list(self):
        self.assertEqual(longest_common_suffix(["", "abc", "bc"]), "")
        self.assertEqual(longest_common_suffix(["abc", "", "bc"]), "")
        self.assertEqual(longest_common_suffix(["abc", "def", ""]), "")
        
    def test_single_string(self):
        self.assertEqual(longest_common_suffix(["single"]), "single")

    # 4F
    def test_is_int(self):
        # Valid integers
        self.assertTrue(is_int("123"))
        self.assertTrue(is_int("-123"))
        self.assertTrue(is_int("0"))

        # Invalid integers
        self.assertFalse(is_int("0123"))
        self.assertFalse(is_int("-0123"))
        self.assertFalse(is_int("123a"))
        self.assertFalse(is_int("a123"))
        self.assertFalse(is_int(""))
        self.assertFalse(is_int(" "))
        self.assertFalse(is_int("+123"))
        self.assertFalse(is_int("--123"))
        self.assertFalse(is_int("123.0"))
        self.assertFalse(is_int("12 3"))
        self.assertFalse(is_int("123-"))
        self.assertFalse(is_int("1-23"))
        self.assertFalse(is_int("123."))
        self.assertFalse(is_int(".123"))

    def test_boundary_cases(self):
        # Large integers
        self.assertTrue(is_int(str(10**18)))
        self.assertTrue(is_int(str(-10**18)))
        self.assertFalse(is_int(str(10**18) + "a"))
        self.assertFalse(is_int(str(-10**18) + "a"))

        # Single digit
        self.assertTrue(is_int("5"))
        self.assertTrue(is_int("-5"))
        self.assertFalse(is_int("5a"))
        self.assertFalse(is_int("-5a"))

        # Integer with plus sign (not valid for this function)
        self.assertFalse(is_int("+0"))
        self.assertFalse(is_int("+123"))

    # 4G
    def test_merge(self):
        self.assertEqual(merge("abcd", ""), "abcd")
        self.assertEqual(merge("", "abcd"), "abcd")
        self.assertEqual(merge("aabbddfgk", "adkox"), "aaabbdddfgkkox")
        self.assertEqual(merge("", ""), "")
        self.assertEqual(merge("abcd", "abcd"), "aabbccdd")
        self.assertEqual(merge("abc", "xyz"), "abcxyz")
        self.assertEqual(merge("ace", "bdf"), "abcdef")
        self.assertEqual(merge("aaaa", "aaa"), "aaaaaaa")
        self.assertEqual(merge("a", "b"), "ab")
        self.assertEqual(merge("aaaa", "zzzz"), "aaaazzzz")
        self.assertEqual(merge("1234", "5678"), "12345678")
        self.assertEqual(merge("1234", "4321"), "11223344")
        self.assertEqual(merge("abcd", "efgh"), "abcdefgh")
        self.assertEqual(merge("abc", "cde"), "abccde")
        self.assertEqual(merge("apple", "orange"), "aaeeglnoppr")
        self.assertEqual(merge(" ", "abc"), " abc")
        self.assertEqual(merge("abc", " "), " abc")
        self.assertEqual(merge("a c", "b d"), "  abcd")

    # 5A
    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("tommarvoloriddle", "iamlordvoldemort"))
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("hello", ""))
        self.assertFalse(is_anagram("", "hello"))
        self.assertTrue(is_anagram("a", "a"))
        self.assertTrue(is_anagram("", ""))

    # 5B
    def test_is_anagram_v2(self):
        self.assertTrue(is_anagram_v2("listen", "silent"))
        self.assertTrue(is_anagram_v2("tommarvoloriddle", "iamlordvoldemort"))
        self.assertFalse(is_anagram_v2("hello", "world"))
        self.assertFalse(is_anagram_v2("hello", ""))
        self.assertFalse(is_anagram_v2("", "hello"))
        self.assertTrue(is_anagram("a", "a"))
        self.assertTrue(is_anagram_v2("", ""))

    # 5C
    def test_is_anagram_v3(self):
        self.assertTrue(is_anagram_v3("listen", "silent"))
        self.assertTrue(is_anagram_v3("tommarvoloriddle", "iamlordvoldemort"))
        self.assertFalse(is_anagram_v3("hello", "world"))
        self.assertFalse(is_anagram_v3("hello", ""))
        self.assertFalse(is_anagram_v3("", "hello"))
        self.assertTrue(is_anagram("a", "a"))
        self.assertTrue(is_anagram_v3("", ""))

    # 6A
    def test_eval_mon(self):
        self.assertEqual(eval_mon("+5x^3", 4), 5 * 4**3)
        self.assertEqual(eval_mon("-10x^0", 4), -10 * 4**0)
        self.assertEqual(eval_mon("+1x^10", 2), 1 * 2**10)
        self.assertEqual(eval_mon("+2x^2", 3), 2 * 3**2)
        self.assertEqual(eval_mon("+3x^4", 0), 3 * 0**4)
        self.assertEqual(eval_mon("+4x^1", -5), 4 * (-5)**1)
        self.assertEqual(eval_mon("-7x^5", 1), -7 * 1**5)
        self.assertEqual(eval_mon("+6x^6", -2), 6 * (-2)**6)
        self.assertEqual(eval_mon("-8x^3", 2), -8 * 2**3)
        self.assertEqual(eval_mon("+10x^3", 10), 10 * 10**3)
        self.assertEqual(eval_mon("-11x^3", -3), -11 * (-3)**3)


    # 6B
    def test_eval_pol(self):
        self.assertEqual(eval_pol("+5x^3-17x^2", 1), -12)
        self.assertEqual(eval_pol("+11x^12", 2), 45056)
        self.assertEqual(eval_pol("+5x^3-4x^2+7x^1-5x^0", 4), 279)
        self.assertEqual(eval_pol("+5x^3-4x^2+7x^1-5x^0", 0), -5)

if __name__ == "__main__":
    unittest.main()
