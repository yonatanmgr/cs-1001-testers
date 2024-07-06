import random
from random import randint
import string
import unittest
import numpy as np
from hw3_******** import *
import time


# HELPERS


def generate_k_ordered_list(n, k):
    ls = list(range(n))  # Positions that can be used
    random.shuffle(ls)
    k -= 1
    k_sorted_ls = quick_sort(ls, k)
    return k_sorted_ls


def quick_sort(data, k):
    """Sorts a list using quicksort with a stopping condition for sublists.

    Args:
      data: The list to be sorted.
      k: The minimum sublist length for further recursion.

    Returns:
      The sorted list.
    """
    if len(data) <= k:
        return data
    # print(k)
    pivot = random.choice(data)
    left, right = [], []

    for element in data[1:]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left, k) + [pivot] + quick_sort(right, k)


def generate_graph(n, p):
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                graph[i].append(j)

    return graph


def generate_similar_strings(n, max_length=5, min_length=-1):
    """
    Generates a list of unique strings of varying lengths up to max_length.

    Parameters:
    n (int): Number of strings to generate.
    max_length (int): Maximum length of each string (default is 5).

    Returns:
    list: A list of unique strings of varying lengths.
    """
    if min_length == -1:
        min_length = max_length // 2

    def generate_random_string(length):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    strings = set()

    while len(strings) < n:
        # Randomly decide the length of the new string
        length = random.randint(min_length, max_length)
        new_string = generate_random_string(length)
        strings.add(new_string)

    return list(strings)


def default_pages_data(n, promote_p=0.0, graph_p=0.0, max_str_amount=0, max_strs_length=0, empty_text=True):
    graph = generate_graph(n, graph_p)
    promote = [random.random() < promote_p for __ in range(n)]
    if max_str_amount != 0:
        page_desc = [generate_similar_strings(randint(1, max_str_amount), max_strs_length) for __ in range(n)]
    else:
        page_desc = [[''] for __ in range(n)]
    text = ''
    if not empty_text:
        text = generate_similar_strings(1, max_strs_length)
    return graph, promote, page_desc, text


# TESTS
class TestFunctions(unittest.TestCase):

    def test_PageRank(self):
        # sanity check
        n = 4
        graph, promote, page_desc, text = default_pages_data(n, 0.5, 0)
        rank = PageRank_search(graph, 100, 1, '', page_desc, promote)
        self.assertAlmostEqual(sum(rank), 1, delta=0.001)
        promote = [0 for __ in range(n)]
        promote[0] = 1
        for rk in rank:
            self.assertAlmostEqual(rk, 1 / n, delta=0.2)
        graph, promote, page_desc, text = default_pages_data(3, 0.0, 1)
        promote[0] = 1
        rank = PageRank_search(graph, 400, 1, '', page_desc, promote)

        self.assertEqual(max(rank), rank[0], "promote feature doesnt work as expected")
        graph, promote, page_desc, text = default_pages_data \
            (n=3, promote_p=0.0, graph_p=1, max_str_amount=4, max_strs_length=6)
        rank = PageRank_search(graph, 100, 1, page_desc[0][0], page_desc, promote)
        self.assertEqual(max(rank), rank[0])

        # if the rank of the pages doesnt get closer and closer to a limit then there is probably a mistake in pagerank
        print("RUNNING LONG TEST")
        LONG_TEST = True
        if LONG_TEST:
            n_of_unlikely = 0
            n_of_likely = 0
            for i in range(10, 20, 1):
                graph_p = random.random()
                graph = generate_graph(i, graph_p)
                promote = [random.random() < 0.5 for __ in range(i)]
                page_desc = [generate_similar_strings(random.randint(1, 5), 8) for __ in range(i)]
                rank_p = random.random() / 10 + 0.8
                text = generate_similar_strings(random.randint(0, 4))
                iterations = random.randint(50, 75)
                rank1 = PageRank_search(graph, iterations, rank_p, text, page_desc, promote)
                rank2 = PageRank_search(graph, iterations, rank_p, text, page_desc, promote)
                rank3 = PageRank_search(graph, iterations + 100, rank_p, text, page_desc, promote)
                rank1, rank2, rank3 = np.array(rank1), np.array(rank2), np.array(rank3)
                diff1 = np.sum(np.abs(rank2 - rank1))
                diff2 = np.sum(np.abs(rank3 - rank2))
                if diff1 < diff2:
                    n_of_unlikely += 1
                else:
                    n_of_likely += 1

            self.assertGreaterEqual(n_of_likely, n_of_unlikely * 3 / 4,
                                    "The page rank algortihm doesnt settle down to a limit")

    def test_sort_almost_k(self):
        for n in range(3, 20):
            k = random.randint(1, n)
            ls = generate_k_ordered_list(n, k)
            sorted_ls = sorted(ls)
            ls2 = ls.copy()
            sort_almost_k(ls, k)
            if sorted_ls != ls:
                print(sorted_ls)
                print(ls)
                print(ls2)
                print(k)
            self.assertEqual(sorted_ls, ls)

    def test_find_percentile_almost_k(self):
        for i in range(3, 10):
            k = 10
            ls = generate_k_ordered_list(i, k)
            m = randint(1, len(ls) - 1)

            self.assertEqual(sorted(ls)[m - 1], find_percentile_almost_k(ls, k, m), 'Incorrect value returned ')
        rng = range(10, 100, 10)
        time_ls = [0 for __ in range(len(rng))]
        i = 0
        for n in rng:
            k = 3
            ls = generate_k_ordered_list(n, k)
            m = randint(1, len(ls) - 1)
            t1 = time.time()
            for __ in range(100):
                find_percentile_almost_k(ls, k, m)
            t2 = time.time()
            time_ls[i] += t2 - t1
            i += 1
        tot_time = sum(time_ls) / len(time_ls)
        for t in time_ls:
            self.assertAlmostEqual(tot_time, t, delta=0.02,
                                   msg='not running in O(1), might run faster than linear but' +
                                       'a O(1) exists but isnt required')


if __name__ == '__main__':
    unittest.main()
