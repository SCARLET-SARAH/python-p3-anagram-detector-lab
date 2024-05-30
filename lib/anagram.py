# your code goes here!
def __init__(self, word):
        self.word = word

def match(self, words):
        anagrams = [word for word in words if sorted(word) == sorted(self.word)]
        return anagrams