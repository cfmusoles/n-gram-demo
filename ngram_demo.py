############################################
## n-gram prediction demo project ##########
## Input: 
##      - ngram_size: maximum size of the n-gram (will generate bags of *ngram_size* and less words combinations)
##      - nwords: number of words to predict
##      - seed_sentence: input sentence for the algorithm. The prediction is based on this string.
## Output:
##      - next *nwords* predicted based on the input sentence
############################################

import sys
import random
import nltk
nltk.download('punkt')


# training data provided
training_data = "Just A Rather Very Intelligent System a.k.a JARVIS is created by Tony Stark natural-language and a sophisticated artificial intelligence user interface computer system, named after Edwin Jarvis, the butler who worked for Howard Stark. Though its primary duty is to automate Stark’s Malibu estate, the lifelike program fulfills many other needs for Stark, like being an information source for him, a diagnostic tool, a consultant and a voice of reason in Stark’s life. It was also responsible to provide security for Tony Stark's Mansion and Stark Tower. After creating the Mark II armor, Stark uploaded JARVIS into all of the Iron Man Armors, as well as allowing him to interact with the other Avengers, giving them valuable information during combat. JARVIS may be the one intellect Stark feels most comfortable opening up to. JARVIS can object to Stark’s commands if necessary. JARVIS speaks with a refined British accent, and is capable of back talk, sarcasm and condescension. During the Ultron Offensive, JARVIS was destroyed by Ultron, although his remaining programming codes unknowingly continued to thwart Ultron's plans of gaining access to nuclear missiles. His remains were found by Stark, who uploaded them into a synthetic body made of vibranium and, in conjunction with Ultron's personality and an Infinity Stone. JARVIS' duties were then taken over by FRIDAY."
tokens = nltk.word_tokenize(training_data)


###########################
## AUXILIARY FUNCTIONS

# get a random choice of word, based on weighed distribution
def weighted_choice(choices):
   dist = sum(count for ngram, count in choices)
   p = random.uniform(0, dist)
   cummulative_p = 0
   for ngram, count in choices:
      if cummulative_p + count > p:
         return ngram
      cummulative_p += count
    
# produdes the next probable word based on the ngrams, given current_word
def predict_next_word(current_word,ngrams):
    # Get all possible choices where the first element is the current word
    choices = [ngram for ngram in ngrams if ngram[0][0] == current_word]

    if not choices:
        return None
    else:
        # Choose a random next word based on weighed probability
        word = weighted_choice(choices)[1]
        return word

############################


if __name__ == '__main__': 
    # process command line arguments
    if len(sys.argv) < 4:
        print("Input error: usage -> python ngram_demo.py ngram_size nwords seed_sentence")
        exit()

    ngram_size = int(sys.argv[1])
    nwords = int(sys.argv[2])
    seed_sentence = [sys.argv[x] for x in range(3,len(sys.argv))]
    predicted_word = ''

    # generate n-grams
    ngrams = list(nltk.ngrams(tokens,ngram_size))

    # find frequencies
    fdist = nltk.FreqDist(ngrams)

    # sort them in descending order of popularity
    sorted_ngrams = sorted(fdist.items(), key=lambda x: -x[1])

    #Simple prediction model based on the last word of the seed sentence
    # cummulative model, the next predicted word is used as input to predict the following (until nwords have been found)
    predicted_sentence = []
    current_word = seed_sentence[-1]
    for i in range(nwords):
        next_word = predict_next_word(current_word,sorted_ngrams)
        if not next_word:
            break
        predicted_sentence.append(next_word)
        current_word = next_word

    # Display results
    input_sentence = " ".join(seed_sentence)
    print('Input sentence: ' + input_sentence)
    print('Predicted word: ' + " ".join(predicted_sentence))
