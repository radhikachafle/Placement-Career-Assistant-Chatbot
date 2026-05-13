import json
import pickle
import random
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()


def preprocess(intents_path="data/intents.json"):
    with open(intents_path, encoding='utf-8') as f:
        data = json.load(f)

    words = []
    classes = []
    documents = []
    ignore_chars = ['?', '!', '.', ',', "'", '"']

    for intent in data['intents']:
        for pattern in intent['patterns']:
            token_list = nltk.word_tokenize(pattern)
            words.extend(token_list)
            documents.append((token_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

    words = sorted(set([
        lemmatizer.lemmatize(w.lower())
        for w in words
        if w not in ignore_chars
    ]))
    classes = sorted(set(classes))

    print(f"Vocabulary size  : {len(words)}")
    print(f"Intent classes   : {len(classes)}")
    print(f"Training docs    : {len(documents)}")

    pickle.dump(words, open('model/words.pkl', 'wb'))
    pickle.dump(classes, open('model/classes.pkl', 'wb'))

    training = []
    output_empty = [0] * len(classes)

    for doc in documents:
        bag = []
        word_patterns = [lemmatizer.lemmatize(w.lower()) for w in doc[0]]
        for w in words:
            bag.append(1 if w in word_patterns else 0)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training, dtype=object)

    X_train = np.array(list(training[:, 0]))
    y_train = np.array(list(training[:, 1]))

    return X_train, y_train, words, classes