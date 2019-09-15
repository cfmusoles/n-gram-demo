# n-gram-demo

### Description 
Prediction of the next work based on an **n-gram** approach. The task shows a simple prediction algorithm. The full input text to the algorithm is:

> Just A Rather Very Intelligent System a.k.a JARVIS is created by Tony Stark natural-language and a sophisticated artificial intelligence user interface computer system, named after Edwin Jarvis, the butler who worked for Howard Stark. Though its primary duty is to automate Stark’s Malibu estate, the lifelike program fulfills many other needs for Stark, like being an information source for him, a diagnostic tool, a consultant and a voice of reason in Stark’s life. It was also responsible to provide security for Tony Stark's Mansion and Stark Tower. After creating the Mark II armor, Stark uploaded JARVIS into all of the Iron Man Armors, as well as allowing him to interact with the other Avengers, giving them valuable information during combat. JARVIS may be the one intellect Stark feels most comfortable opening up to. JARVIS can object to Stark’s commands if necessary. JARVIS speaks with a refined British accent, and is capable of back talk, sarcasm and condescension. During the Ultron Offensive, JARVIS was destroyed by Ultron, although his remaining programming codes unknowingly continued to thwart Ultron's plans of gaining access to nuclear missiles. His remains were found by Stark, who uploaded them into a synthetic body made of vibranium and, in conjunction with Ultron's personality and an Infinity Stone. JARVIS' duties were then taken over by FRIDAY.

This example uses a very simple generative model that takes the last word of the input sentence to predict the next word. It is cummulative, so the prediction is used as the input to predict the next word until a sentence of the required length is achieved.

The predictions are based on n-grams, with a weighed probability using the n-gram counts found in the input *corpus*.


### Requirements

The project is written using python 3 and requires the following libraries:
- NLTK (Natural Language Toolkit). Install instructions [here](https://www.nltk.org/install.html)

### Running the project

To run the project, use 

```
python ngram_demo.py [ngram_size] [nwords] [seed_sentence]
```
*ngram_size*: size of the n-gram (will generate bags of *ngram_size* words combinations). Minimum 2.
*nwords*: number of words to predict (length of the sentence)
*seed_sentence*: input sentence of any length for the algorithm. The prediction is based on this string. Mimimum length 1.

The output of the program consists of the seed sentence plus the predicted next word:
```
Input seed: [seed_sentence]
Predicted sentence: [predicted sentence based on the last word of seed_sentence]
```

Example: *python ngram_demo.py 3 10 Tony Stark is*
```
Input sentence: Tony Stark is
Predicted word: capable of reason in conjunction with a refined British accent
```

### Limitations

- The predictions are based on the previous word alone (though the length of the ngram can be > 2)
- If the *seed_sentence* contains an unknown word (not in the corpus) the algorithm returns an empty word
- Because it is based on a probabilistic model, the same input may yield different output every time
- For this demo, the corpus is not filtered or cleaned
