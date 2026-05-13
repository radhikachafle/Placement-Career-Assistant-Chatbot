import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

model = pickle.load(open('model/chatbot_model.pkl', 'rb'))
words = pickle.load(open('model/words.pkl', 'rb'))
classes = pickle.load(open('model/classes.pkl', 'rb'))


def bag_of_words(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens]
    bag = [1 if w in tokens else 0 for w in words]
    return np.array(bag)


def predict_intent(sentence, threshold=0.4):
    bow = bag_of_words(sentence)
    proba = model.predict_proba(np.array([bow]))[0]
    max_prob = float(max(proba))
    predicted_class = classes[int(np.argmax(proba))]
    print(f"Intent: {predicted_class} | Confidence: {max_prob:.2%}")
    if max_prob < threshold:
        return "general"
    return predicted_class