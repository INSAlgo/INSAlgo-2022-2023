class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        good_words = []

        for word in words :
            perm = {}
            rev_perm = {}
            for i in range(len(pattern)) :
                
                # Checking one way
                if pattern[i] in perm :
                    if word[i] != perm[pattern[i]] :
                        break
                else :
                    perm[pattern[i]] = word[i]
                
                # Checking the other way ("abb" does not match "ccc")
                if word[i] in rev_perm :
                    if pattern[i] != rev_perm[word[i]] :
                        break
                else :
                    rev_perm[word[i]] = pattern[i]
                
            else :
                good_words.append(word)
        
        return good_words