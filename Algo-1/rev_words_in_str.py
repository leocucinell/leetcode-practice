def reverse_word(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while left <= right:
        s[right], s[left] = s[left], s[right]
        right -=1
        left +=1
    return "".join(str(letter) for letter in s)


def rev_words_in_sentence(sentence):
    new_sentence_list = []
    sentence_list = sentence.split(" ")
    for word in sentence_list:
        rev_word = reverse_word(word)
        new_sentence_list.append(rev_word)

    return " ".join(new_sentence_list)

def main():
    print(rev_words_in_sentence("hello my world"))

if __name__ == "__main__":
    main()
