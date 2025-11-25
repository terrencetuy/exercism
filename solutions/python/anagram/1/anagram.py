def find_anagrams(word, candidates):
    return [
        candidate for candidate in candidates 
        if candidate.lower() != word.lower() and sorted(list(word.lower())) == sorted(list(candidate.lower()))
    ]
