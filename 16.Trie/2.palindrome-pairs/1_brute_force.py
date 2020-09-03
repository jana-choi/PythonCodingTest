def palindromePairs(words):
    def is_palindrome(word):
        return word == word[::-1]
    
    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])

    return output


if __name__ == "__main__":
    print(palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(palindromePairs(["bat", "tab", "cat"]))