from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wl = set(wordList)

        if endWord not in wl:
            return 0

        q = deque([beginWord])
        step = 1
        visited = {beginWord}

        while q:

            # Process one complete BFS level
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return step

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in wl and new_word not in visited:
                            visited.add(new_word)
                            q.append(new_word)

            # Move to the next level
            step += 1

        return 0
            
        