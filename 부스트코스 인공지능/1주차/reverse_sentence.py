#문자열을 거꾸로 출력

sentence = "way a is there will a is there where"

def reverse_sentence(sentence):  
    sentence_split = sentence.split()
    sentence_split.reverse()
    sentence = " ".join(sentence_split)
    return sentence

print(reverse_sentence(sentence))