def reverse_sentence(sentence):
    words = sentence.split() #words = ["We","are","ready"]
    reversed_words = list(reversed(words)) #reversed_words = ["ready","are","We"]
    return ' '.join(reversed_words) # ready are We
print(reverse_sentence(str(input())))