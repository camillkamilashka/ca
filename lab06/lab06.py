import itertools

def count_code_words():
    alphabet = ['A', 'B', 'C', 'D', 'E']
    code_words = list(itertools.product(alphabet, repeat=5))
    filtered_code_words = [word for word in code_words if word[0] != 'E' and word[4] != 'A']
    return len(filtered_code_words)

print(count_code_words())
