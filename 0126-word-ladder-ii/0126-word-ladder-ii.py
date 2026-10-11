from collections import defaultdict,deque
class Solution:
    def findLadders(self,beginWord:str,endWord:str,wordList:list[str])->list[list[str]]:
        words=set(wordList)
        if endWord not in words:
            return []
        parents=defaultdict(list)
        queue=deque([beginWord])
        visited={beginWord}
        found=False
        while queue and not found:
            level_visited=set()
            for _ in range(len(queue)):
                word=queue.popleft()
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch==word[i]:
                            continue
                        new_word=word[:i]+ch+word[i+1:]
                        if new_word not in words or new_word in visited:
                            continue
                        parents[new_word].append(word)
                        level_visited.add(new_word)
                        if new_word==endWord:
                            found=True
                        if new_word not in queue:
                            queue.append(new_word)
            visited.update(level_visited)
        if not found:
            return []
        res=[]
        path=[endWord]
        def backtrack(word):
            if word==beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()
        backtrack(endWord)
        return res