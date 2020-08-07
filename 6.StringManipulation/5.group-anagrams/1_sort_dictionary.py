import collections

def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams["".join(sorted(word))].append(word)

    ana_list = list(anagrams.values())
    for i in range(len(ana_list)):
        ana_list[i].sort()
    return ana_list

    # return anagrams.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))