import unicodedata

def normalize_string(word):
    return unicodedata.normalize('NFKD',word).replace(' ','').lower()

def sort_str(word):
    return sorted(
            w for w in normalize_string(word) if w.isalpha()
        )

def is_anagram(word,second):
    return sort_str(word) == sort_str(second)
        
#moje rozwiązanie
def anagram(word,second):
    word_list = [normalize('NFD',w)[0] for w in word.replace(' ','').lower() if w.isalpha()]
    second_list = [normalize('NFD',sw)[0] for sw in second.replace(' ','').lower() if sw.isalpha()]
    return sorted(word_list) == sorted(second_list)
