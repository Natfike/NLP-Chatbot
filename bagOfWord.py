import json
import string
import random

import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout


class BagOfWord:
    model = Sequential()
    def __init__(self):
        self.data_root = 'intents.json'
        self.model = ""
        nltk.download("punkt")
        nltk.download("wordnet")

        data_file = open('intents.json').read()
        data = json.loads(data_file)
        self.data = json.loads(data_file)

        self.words = []
        self.classes = []
        data_X = []
        data_Y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                tokens = nltk.word_tokenize(pattern)
                self.words.extend(tokens)
                data_X.append(pattern)
                data_Y.append(intent["tag"])

                if intent["tag"] not in self.classes:
                    self.classes.append(intent["tag"])

        lemmatizer = WordNetLemmatizer()
        self.lemmatizer = lemmatizer
        self.words = [lemmatizer.lemmatize(word.lower()) for word in self.words if word not in string.punctuation]

        self.words = sorted(set(self.words))
        self.classes = sorted(set(self.classes))

        training = []
        out_empty = [0] * len(self.classes)

        # on créer le sac de mot
        for idx, doc in enumerate(data_X):
            print(idx, doc)
            bow = []
            text = lemmatizer.lemmatize(doc.lower())
            for word in self.words:
                bow.append(1) if word in text else bow.append(0)

            output_row = list(out_empty)
            output_row[self.classes.index(data_Y[idx])] = 1
            training.append([bow, output_row])

        random.shuffle(training)
        training = np.array(training, dtype=object)

        train_X = np.array(list(training[:, 0]))
        train_Y = np.array(list(training[:, 1]))

        model = Sequential()
        model.add(Dense(256, input_shape=(len(train_X[0]),), activation="relu"))
        model.add(Dropout(0.5))
        model.add(Dense(128, activation="relu"))
        model.add(Dropout(0.5))
        model.add(Dense(len(train_Y[0]), activation="softmax"))

        adam = tf.keras.optimizers.legacy.Adam(learning_rate=0.015, decay=1e-6)
        model.compile(loss='categorical_crossentropy',
                      optimizer=adam,
                      metrics=["accuracy"])
        model.fit(x=train_X, y=train_Y, epochs=150, verbose=1)
        self.model = model

    def clean_text(self, text):
        print("text : ", text)
        tokens = nltk.word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        return tokens

    def bag_of_words(self, text, vocab):
        tokens = self.clean_text(text)
        bow = [0] * len(vocab)
        for w in tokens:
            for idx, word in enumerate(vocab):
                if word == w:
                    bow[idx] = 1
        return np.array(bow)

    def pred_class(self, text):
        bow = self.bag_of_words(text, self.words)
        result = self.model.predict(np.array([bow]))[0]
        thresh = 0.5
        y_pred = [[indx, res] for indx, res in enumerate(result) if res > thresh]
        y_pred.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in y_pred:
            return_list.append(self.classes[r[0]])
        return return_list

    def get_response(self, intents_list):
        if len(intents_list) == 0:
            result = "Sorry, I don't understand !"
        else:
            tag = intents_list[0]
            list_of_intents = self.data["intents"]
            for i in list_of_intents:
                if i["tag"] == tag:
                    result = random.choice(i["responses"])
                    break
            return result