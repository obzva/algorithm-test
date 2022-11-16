from typing import *


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # GRAPH WITH BFS

        # adj_list = collections.defaultdict(set)
        # incoming_edges = collections.Counter({letter: 0 for word in words for letter in word})
        #
        # for first_word, second_word in zip(words, words[1:]):
        #     for letter_of_first, letter_of_second in zip(first_word, second_word):
        #         if letter_of_first != letter_of_second:
        #             if letter_of_second not in adj_list[letter_of_first]:
        #                 adj_list[letter_of_first].add(letter_of_second)
        #                 incoming_edges[letter_of_second] += 1
        #             break
        #     # meaning there is a case that some letters are following the prefix of themselves
        #     else:
        #         if len(first_word) > len(second_word):
        #             return ""
        #
        # output = []
        # queue = collections.deque([letter for letter in incoming_edges if incoming_edges[letter] == 0])
        # while queue:
        #     letter = queue.popleft()
        #     output.append(letter)
        #     for next_letter in adj_list[letter]:
        #         incoming_edges[next_letter] -= 1
        #         if incoming_edges[next_letter] == 0:
        #             queue.append(next_letter)
        #
        # # meaning there is a cycle
        # if len(output) < len(incoming_edges):
        #     return ""
        #
        # return ''.join(output)

        # GRAPH WITH DFS

        incoming_edges = {letter: [] for word in words for letter in word}

        for first_word, second_word in zip(words, words[1:]):
            for letter_of_first, letter_of_second in zip(first_word, second_word):
                if letter_of_first != letter_of_second:
                    if letter_of_first not in incoming_edges[letter_of_second]:
                        incoming_edges[letter_of_second].append(letter_of_first)
                    break
            # meaning there is a case that some letters are following the prefix of themselves
            else:
                if len(first_word) > len(second_word):
                    return ""

        seen = {}
        output = []

        def visit(letter: str) -> bool:
            if letter in seen:
                return seen[letter]

            seen[letter] = False
            for next_letter in incoming_edges[letter]:
                if not visit(next_letter):
                    return False
            seen[letter] = True
            output.append(letter)
            return True

        if not all(visit(letter) for letter in incoming_edges):
            return ""

        return ''.join(output)
