import nltk

input = open('input.txt') #open the input of .txt file
sentence = input.read() #read a sentence from the file
print('Sentence :', sentence)

output = open('result.txt','w') #open the output of .txt file

tokens = nltk.word_tokenize(sentence)
length = len(tokens)
print('Word of the Sentence: ', str(tokens))
print('Length: ', str(length))

output.write('Word of the Sentence: ' + str(tokens) + '\n') #writing the output text
