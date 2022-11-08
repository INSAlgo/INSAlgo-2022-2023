class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        
        good_words = []
        
        for word in words :
            word_set = set(word.lower())
            for line in lines :
                if word_set.issubset(line) :
                    good_words.append(word)
                    break
        
        return good_words