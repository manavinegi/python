with open('data.txt', 'r') as file:
    words = file.read().split()
    max_len = len(max(words, key=len))
    min_len = len(min(words, key=len))
    for word in words:
        if len(word) == max_len:
            print('max:',word)
        if len(word) == min_len:
            print('min:',word)
