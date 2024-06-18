from random import randint
import unittest

from skeleton_file import *

# HELPERS
is_good_slot = lambda slot, tested: slot[1] <= tested[0] or slot[0] >= tested[1]
flatten = lambda l: [item for sublist in l for item in sublist]
random_binary = lambda: bin(randint(0, 4096))[2:]

def generate_prob_list(n):
    sum = 10000
    numbers = []
    for _ in range(n - 1):
        numbers.append(randint(0, sum))
        sum -= numbers[-1]
    return [n/10000 for n in numbers + [sum]]

def generate_random_letters(n):
    letters = []
    while len(letters) < n:
        l = chr(randint(97, 122))
        if l not in letters:
            letters.append(l)
    return letters

def generate_timetable(n):
    slots = []
    start = randint(7, 10)
    for _ in range(n):
        end = randint(min(start, 19), min(start + randint(1, 3), 20))
        if (start, end) not in slots and start < 20 and end != start:
            slots.append((start, end))
            start = min(end + randint(1, 3), 20)
    return slots

def generate_intervals(n):
    intervals = []
    for i in range(n):
        start = randint(i*1000, i*1000 + 1000)
        end = randint(i*1000, start + 2000)
        intervals.append((start, end) if start < end else (end, start))
    return sorted(intervals)

# TESTS
class TestFunctions(unittest.TestCase):
    # QUESTION 1
    def test_divisors(self):
        self.assertEqual(divisors(6), [1, 2, 3])
        self.assertEqual(divisors(28), [1, 2, 4, 7, 14])
        self.assertEqual(divisors(1), [])
        self.assertEqual(divisors(12), [1, 2, 3, 4, 6])
        self.assertEqual(divisors(7), [1])
        self.assertEqual(divisors(496), [1, 2, 4, 8, 16, 31, 62, 124, 248])

    def test_perfect_numbers(self):
        self.assertEqual(perfect_numbers(1), [6])
        self.assertEqual(perfect_numbers(2), [6, 28])
        self.assertEqual(perfect_numbers(3), [6, 28, 496])
        self.assertEqual(perfect_numbers(4), [6, 28, 496, 8128])

    def test_abundant_density(self):
        self.assertEqual(abundant_density(20), 0.15)

    def test_semi_perfect_4(self):
        self.assertTrue(semi_perfect_4(12))
        self.assertTrue(semi_perfect_4(18))
        self.assertTrue(semi_perfect_4(20))
        self.assertFalse(semi_perfect_4(6))
        self.assertFalse(semi_perfect_4(15))
        self.assertFalse(semi_perfect_4(28))

    def test_find_gcd(self):
        self.assertEqual(find_gcd(48, 18), 6)
        self.assertEqual(find_gcd(101, 103), 1)
        self.assertEqual(find_gcd(100, 10), 10)
        self.assertEqual(find_gcd(100, 1), 1)
        self.assertEqual(find_gcd(100, 0), 100)
        self.assertEqual(find_gcd(0, 100), 100)
        self.assertEqual(find_gcd(0, 0), 0)
        self.assertEqual(find_gcd(1, 1), 1)
        self.assertEqual(find_gcd(48, 18), 6)
        self.assertEqual(find_gcd(101, 103), 1)
        self.assertEqual(find_gcd(0, 5), 5)
        self.assertEqual(find_gcd(5, 0), 5)
        self.assertEqual(find_gcd(0, 0), 0)
        self.assertEqual(find_gcd(20, 5), 5)
        self.assertEqual(find_gcd(5, 20), 5)
        self.assertEqual(find_gcd(270, 192), 6)
        self.assertEqual(find_gcd(54, 24), 6)
        self.assertEqual(find_gcd(99, 78), 3)
        self.assertEqual(find_gcd(56, 98), 14)
        self.assertEqual(find_gcd(123456, 789012), 12)
        self.assertEqual(find_gcd(37, 600), 1)
        self.assertEqual(find_gcd(1024, 2048), 1024)
        self.assertEqual(find_gcd(17, 13), 1)


    # QUESTION 2
    def test_coin(self):
        DEBUG = False
        outcomes = {True: 0, False: 0}
        for _ in range(10000):
            outcomes[coin()] += 1
        if DEBUG:
            print("\n")
            print("Testing coin function for 10000 times.")
            print(outcomes)
        self.assertGreater(outcomes[True], 4000)
        self.assertGreater(outcomes[False], 4000)

    def test_sample(self):
        DEBUG = False
        for _ in range(100):
            size = randint(3, 6)
            v = generate_random_letters(size)
            p = generate_prob_list(size)
            samples = [sample(v, p) for _ in range(10000)]
            for i in range(size):
                self.assertAlmostEqual(samples.count(v[i]) / 10000, p[i], delta=0.1)
            if DEBUG:
                print("\n")
                print("Testing sample function for 10000 times.")
                print(f"v: {v}")
                print(f"p: {p}")
                cntr = {i: samples.count(i) / 10000 for i in v}
                print(f"Samples: {cntr}")

    def test_monty_hall(self):
        DEBUG = False
        times = 100000
        result_switch = monty_hall(True, times)
        result_stay = monty_hall(False, times)
        if DEBUG:
            print("\n")
            print(f"Testing monty_hall function for {times} times.")
            print(result_switch, "is the result for switching")
            print(result_stay, "is the result for staying")
        self.assertAlmostEqual(result_switch, 0.66, delta=0.1)
        self.assertAlmostEqual(result_stay, 0.33, delta=0.1)

    def test_sample_anagram(self):
        original = "supercalifragilisticexpialidocious"
        anagram = sample_anagram(original)
        self.assertEqual(sorted(original), sorted(anagram))
        self.assertEqual(sample_anagram(""), "")

        results = [sample_anagram("abc") for _ in range(10000)]
        all(
            self.assertAlmostEqual(results.count(key), 1666, delta=150)
            for key in results
        )

    # QUESTION 3
    def test_inc(self):
        test_increment = lambda st: self.assertEqual(inc(st), bin(int(st, 2) + 1)[2:])
        for _ in range(10000):
            test_increment(random_binary())

    def test_add(self):
        DEBUG = False
        test_add = lambda a, b: self.assertEqual(add(a, b), bin(int(a, 2) + int(b, 2))[2:])
        for i in range(10000):
            b1 = random_binary()
            b2 = random_binary()
            if DEBUG:
                print("\n")
                print("Testing add function for the " + str(i + 1) + "th time.")
                correct_ans = bin(int(b1, 2) + int(b2, 2))[2:]
                print(b1.zfill(len(correct_ans)), "is the first binary number")
                print(b2.zfill(len(correct_ans)), "is the second binary number")
                print(correct_ans, "is the correct answer")
                print(add(b1, b2), "is the function's answer")
            test_add(b1, b2)
    
    def test_mod_two(self):
        DEBUG = False
        test_mod_two = lambda st, n: self.assertEqual(mod_two(st, n), bin(int(st, 2) % 2**n)[2:])
        for i in range(10000):
            binary = random_binary()
            power = randint(1, 10)
            if DEBUG:
                print("\n")
                print("Testing mod_two function for the " + str(i + 1) + "th time.")
                print(binary, "is the binary number")
                print(power, "is the power")
                print(bin(int(binary, 2) % 2**power)[2:], "is the correct answer")
                print(mod_two(binary, power), "is the function's answer")
            test_mod_two(binary, power)


    def test_max_bin(self):
        for _ in range(10000):
            random_binary_numbers = [random_binary() for _ in range(10)]
            self.assertEqual(max_bin(random_binary_numbers), max(random_binary_numbers, key=lambda x: int(x, 2)))
        
    # QUESTION 4
    def test_assess_office_hour(self):
        for _ in range(1000):
            student_schedules_dict = {
                "Alice": generate_timetable(5),
                "Bob": generate_timetable(5),
                "Charlie": generate_timetable(5),
            }
            
            random_hour = randint(7, 19)
            random_slot = (random_hour, random_hour + 1)
            available, ratio = assess_office_hour(random_slot, student_schedules_dict)
            available_intervals = flatten([student_schedules_dict[student] for student in available])
            
            self.assertTrue(all([is_good_slot(random_slot, interval) for interval in available_intervals]))
            self.assertAlmostEqual(ratio, len(available) / len(student_schedules_dict), delta=0.1)
        
    def test_merge_intervals(self):
        for _ in range(50):
            intervals = generate_intervals(1000)
            merged_intervals = merge_intervals(intervals)
            is_in_merged = lambda i: any([i[0] >= m[0] or i[1] <= m[1] for m in merged_intervals])
            self.assertTrue(all([is_in_merged(interval) for interval in intervals]))

    def test_find_perfect_slots(self):
        for _ in range(1000):
            student_schedules_dict = {
                "Alice": generate_timetable(5),
                "Bob": generate_timetable(5),
                "Charlie": generate_timetable(5),
            }
            
            perfect_slots = find_perfect_slots(student_schedules_dict)
            if perfect_slots:
                self.assertGreaterEqual(perfect_slots[0][0], 7)
                self.assertLessEqual(perfect_slots[-1][1], 20)
                self.assertTrue(all([is_good_slot(slot, interval) for slot in perfect_slots for interval in flatten(student_schedules_dict.values())]))

if __name__ == '__main__':
    unittest.main()
