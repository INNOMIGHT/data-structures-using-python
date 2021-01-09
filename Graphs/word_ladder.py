import collections


class Solution:

    def preprocess(self, word_list):
        d = {}
        for word in word_list:
            for c in range(len(word)):
                wildcard = word[:c] + '*' + word[c+1:]
                if wildcard not in d:
                    d[wildcard] = []
                d[wildcard].append(word)

        return d

    def word_ladder(self, start_word, end_word, word_list):
        processed_words = self.preprocess(word_list)
        print(processed_words)

        queue = collections.deque()
        visited = set()
        queue.append([start_word, 1])
        while queue:
            curr, level = queue.popleft()
            for c in range(len(curr)):
                wildcard = curr[:c] + '*' + curr[c+1:]
                if wildcard in processed_words:
                    for word in processed_words[wildcard]:
                        if word == end_word:
                            return level + 1

                        if word not in visited:
                            visited.add(word)
                            queue.append([word, level+1])

        return 0


solution_check = Solution()
print(solution_check.word_ladder(
    'hit', 'cog',
    ["hot", "dot", "dog", "lot", "log", "cog"]
    ))
