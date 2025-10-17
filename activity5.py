file = open ('CROSSWD.txt', 'r')

# print(type(word_file))
# words = []
# for line in word_file:
#     print(line.strip())
#     words.append(line)
# print(words)
# print([x for x in dir(word_file) if '_' != x[0]])

# data = [1 , 3 , 2 , 8 , 5 , 6 , 10]

# print ([2*x for x in data if x % 2 ==0])

def more_than_20(file):
    words = []
    data = open (file, 'r')
    for word in data:
        if len(word.strip()) > 20:
            words.append(word.strip())
    return words
print(more_than_20("CROSSWD.txt"))

# def has_no_e(word):
#   for letter in word:
#     if letter == 'e' or letter == 'E':
#       return False
#   return True