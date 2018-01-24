import nltk

sentence = 'I am going to take NLP class this semester'
tokens = nltk.word_tokenize(sentence) #tokenization

print(sentence) #print the sentence
print(tokens)  #print each words in sentence (after tokenization)
length = len(tokens)
print('length',length) #length of the sentence

n = 1
for word in tokens: #ittrate the tokens to separate its words
    print('word',n,': ',len(word))
    n += 1

