from keras.preprocessing import sequence
from keras import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout

#model archtecture
def buildmodel(vocabulary_size, embedding_size, max_words):
	model=Sequential()
	model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))
	model.add(LSTM(200))
	model.add(Dense(1, activation='tanh'))
	print(model.summary())
	return model




