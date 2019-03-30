# encoding: utf-8
import os
from collections import Counter
from keras.preprocessing import sequence
from keras import optimizers
import lstm as ls
import numpy as np
import tensorflow as tf
import json
from keras.models import model_from_json
def load_data():
    directory1 = './train/neg'
    train_x = []
    train_y = []
    for filename in os.listdir(directory1):
        if filename.endswith(".txt"):
            f = open(directory1 + '/'+filename)
            lines = f.read()
            train_x.append(lines)
            train_y.append(0)
            f.close()
            continue
        else:
    		continue
    directory2 = './train/pos'
    for filename in os.listdir(directory2):
        if filename.endswith(".txt"):
            f = open(directory2 + '/'+filename)
            lines = f.read()
            train_x.append(lines)
            train_y.append(1)
            continue
        else:
    		continue
    directory3 = './test/neg'
    test_x = []
    test_y = []
    for filename in os.listdir(directory3):
        if filename.endswith(".txt"):
            f = open(directory3 + '/'+filename)
            lines = f.read()
            test_x.append(lines)
            test_y.append(0)
            continue
        else:
    		continue
    directory4 = './test/pos'
    for filename in os.listdir(directory4):
        if filename.endswith(".txt"):
            f = open(directory4 + '/'+filename)
            lines = f.read()
            test_x.append(lines)
            test_y.append(1)
            continue
        else:
    		continue
    return train_x, train_y, test_x, test_y
def vocab_to_int_model(train_x,test_x):
    mergelist = train_x + test_x
    allString = ' '.join(mergelist)
    words = allString.split()
    count_words = Counter(words)
    total_words = len(words)
    sorted_words = count_words.most_common(total_words)
    vocab_to_int = {}
    int_to_vocab = {}
    index = 1
    for w,i in sorted_words:
    	vocab_to_int[w] = index
    	int_to_vocab[index] = w
    	index +=1
    return vocab_to_int, int_to_vocab

def tokenized_sequential(vocab_to_int, data,max_words):
    train_x_seq = []
    length = len(data)
    for i in np.arange(length):
    	sample = data[i]
        r = [vocab_to_int[w] for w in sample.split()]
        train_x_seq.append(r)
    X_train = sequence.pad_sequences(train_x_seq, maxlen=max_words)
    return X_train

def save_model(model,vocab_to_int):
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
# serialize weights to HDF5
    model.save_weights("model.h5")
    jsondata = json.dumps(vocab_to_int)
    f = open("vocab_to_int.json","w")
    f.write(jsondata)
    f.close()

def buildingModel():
    np.random.seed(1)
    tf.set_random_seed(1)
    train_x, train_y, test_x, test_y = load_data()
    vocab_to_int, int_to_vocab = vocab_to_int_model(train_x,test_x)

    max_words = 50
    X_train = tokenized_sequential(vocab_to_int, train_x,max_words)
    X_test = tokenized_sequential(vocab_to_int, test_x,max_words)
    print(len(X_train))
    print(len(X_test))
    #Tuning Parameters
    vocabulary_size = len(vocab_to_int.keys())
    embedding_size = 15
    batch_size = 100
    num_epochs = 10
    model = ls.buildmodel(vocabulary_size,embedding_size,max_words)
	#train model
    opt = optimizers.RMSprop(lr=0.0005, rho=0.9, epsilon=None, decay=0.01)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
	#index_valid = np.random.random_integers(batch_size, size = len(X_train))
    x_train = np.array(X_train)
    y_train = np.array(train_y)
    x_test = np.array(X_test)
    y_test = np.array(test_y)
	#x_valid, y_valid = x_train[index_valid], y_train[index_valid]
	#np.delete(x_train,index_valid)
	#np.delete(y_train,index_valid)
	#print(x_valid[0].shape)
	#test model
    model.fit(x_train, y_train, batch_size=batch_size, shuffle=True, epochs=num_epochs, verbose=1)
    scores = model.evaluate(x_test, y_test, verbose=0)
    print(scores)
    save_model(model, vocab_to_int)
    return model, vocab_to_int

def load_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
# load weights into new model
    loaded_model.load_weights("model.h5")
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    dic_file = open('vocab_to_int.json', 'r')
    loaded_dic_json = dic_file.read()
    dic_file.close()
    vocab_to_int = json.loads(loaded_dic_json)
    return loaded_model, vocab_to_int


def load_prediction_data(vocab_to_int):
    f = open("badnews.txt",'r')
    lines = f.read()
    max_words = 50
    x = []
    r = []
    count = 0
    for word in lines.split():
        try:
            r.append(vocab_to_int[word])
            count += 1
        except:
            continue
        if count == max_words:
            break
    r = np.array(r)
    x.append(r)
    print(x[0].shape)
    #x.append(tokenized_sequential(vocab_to_int,lines,max_words))
    return x

if __name__ == '__main__':
    #model, vocab_to_int = buildingModel()
    model, vocab_to_int = load_model()
    x = load_prediction_data(vocab_to_int)
    x = np.array(x)
    out = model.predict_classes(x)
    print(out)






