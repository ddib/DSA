from collections import deque
import string
def string_transformation(words, start, stop):
    """
    Problem:
    You are given a dictionary called words and two string arguments called start and stop. All given strings have equal length.
    Transform string start to string stop one character per step using words from the dictionary. 
    For example, "abc" → "abd" is a valid transformation step because only one character is changed ("c" → "d"), 
    but "abc" → "axy" is not a valid one because two characters are changed ("b" → "x" and "c" → "y").
    You need to find the shortest possible sequence of strings (two or more) such that:
    First string is start.
    Last string is stop.
    Every string (except the first one) differs from the previous one by exactly one character.
    Every string (except, possibly, first and last ones) are in the dictionary of words.
    https://leetcode.com/problems/word-ladder-ii/description/

    
    Complexity:
    * Time: O(n * m), n: number of words. m: number of characters in a word.
    * Space: O(n * m)
    """
    
    def str_difference(str1, str2):
        return sum(1 for a, b in zip(str1, str2) if a != b) # O(m) m: nb of characters
    
    def get_path(start, stop, max_words):
        output = [stop]
        current_word = parent[stop]
        n = 0
        while current_word != start or n > max_words:
            output.append(current_word)
            current_word = parent[current_word]
            n += 1
        output.append(start)
        output.reverse()
        return output
        
    n = len(words)
    m = len(start)
    
    # edge case: not enough words to transform start to stop    
    steps_count = str_difference(start, stop)
    if steps_count > n + 1:
        return ["-1"]
        
        
    # Build graph 
    all_words = words + [start, stop] # space O(n)
    adjMap = {key: [] for key in set(all_words)} # time and space: O(n)
    for word in adjMap.keys(): # time O(n)
        # building the words
        for i in range(m): # time O(m)
            for char in string.ascii_lowercase: # time O(1) -- 26 iterations 
                nei = word[:i] + char + word[i+1:]
                if nei in adjMap.keys() and nei != word:
                    adjMap[nei].append(word)
                  
    # BFS
    queue = deque()
    queue.append(start)
    visited = {key: 0 for key in set(all_words)}
    parent = {key: None for key in set(all_words)}
    while queue:
        word = queue.popleft()
        visited[word] = 2
        for neighbor in adjMap[word]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                parent[neighbor] = word
                queue.append(neighbor)
            if neighbor == stop:
                parent[stop] = word
                return get_path(start, stop, n + 2)
                
    return ["-1"]
