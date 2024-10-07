def spin_words(sentence):
    result = []
    for word in sentence.split():
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)

# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
