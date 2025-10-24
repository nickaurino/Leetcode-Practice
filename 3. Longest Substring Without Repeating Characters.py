class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphabet_hashmap = {}

        word = ""
        word_list = []
        count = 0

        for j in range(len(s)):
            print(j)
            for i in range(j, len(s)):
                if s[i] not in alphabet_hashmap:
                    alphabet_hashmap[s[i]] = 0
                if alphabet_hashmap[s[i]] == 1:
                    break
                word += s[i]
                alphabet_hashmap[s[i]] = 1
            print(word)
            if len(word) > count:
                count = len(word)

            #reset variables
            alphabet_hashmap = {}
            word = ""

        return(count)
