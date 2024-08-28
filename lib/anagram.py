class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        # separates word characters into list and sorts alpabetically
        word_chars = sorted([char for char in self.word])
        # this list will recieve words that are anagrams of our word
        matches = []
        # iterate over list of anagram words
        for word in anagram_list:
            # store characters of word in list
            chars = []
            for char in word:
                chars.append(char)
            # if sorted chars from anagram match sorted chars of our word
            # append matching word to matches list
            if sorted(chars) == word_chars:
                matches.append(word)
                # print(word)
        # return matches list when method is called on a word
        return matches
    
        print(matches)
       
        
        

# word = Anagram("listen")

# word.match(['enlists', 'google', 'inlets', 'banana', 'netsil'])