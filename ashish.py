from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.utils import shuffle
import keras
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keras import optimizers

df = pd.read_csv("shot_logs_assignment.csv")

df = pd.DataFrame(df)
df = shuffle(df)
#Convert to numeric

df = df.assign(
    Shot_made = lambda dataframe: dataframe['SHOT_RESULT'].map(lambda SHOT_RESULT: 1 if SHOT_RESULT == "made" else 0),
    Is_Loc_A = lambda dataframe: dataframe['LOCATION'].map(lambda LOCATION: 1 if LOCATION == "A" else 0)
)

df.head()

len(df)


#################################################


#One hot for categorical

#encoded_playerid = pd.DataFrame(to_categorical(df['player_id']))
encoded_Player_Age = pd.DataFrame(to_categorical(df['Player_Age']))
#encoded_Player_Pos = pd.DataFrame(to_categorical(df['Player_Pos']))
encoded_Defender_Age = pd.DataFrame(to_categorical(df['Defender_Age']))
#encoded_Defender_Pos = pd.DataFrame(to_categorical(df['Defender_Pos']))
#encoded_CLOSEST_DEFENDER_PLAYER_ID = pd.DataFrame(to_categorical(df['CLOSEST_DEFENDER_PLAYER_ID']))
encoded_Period = pd.DataFrame(to_categorical(df['PERIOD']))
encoded_Is_Loc_A = pd.DataFrame(to_categorical(df['Is_Loc_A']))
encoded_SHOT_NUMBER = pd.DataFrame(to_categorical(df['SHOT_NUMBER']))

#Y One hot
encoded_Shot_made = pd.DataFrame(to_categorical(df['Shot_made']))


len(encoded_Player_Age.iloc[0,])
len(encoded_Shot_made.iloc[0,])

#Join to test

test = encoded_Player_Age.join(encoded_Defender_Age,lsuffix='_left', rsuffix='_right')
#test = test.join(encoded_CLOSEST_DEFENDER_PLAYER_ID,lsuffix='_left', rsuffix='_right')
test = test.join(encoded_Period,lsuffix='_left', rsuffix='_right')
test = test.join(encoded_Is_Loc_A,lsuffix='_left', rsuffix='_right')
test = test.join(encoded_SHOT_NUMBER,lsuffix='_left', rsuffix='_right')
test = test.join(df['CLOSEST_DEFENDER_PLAYER_ID'])
test = test.join(df['player_id'])



test.head()


#################################################


#Normalise numeric vectors
# create scaler
scaler = MinMaxScaler()
# fit and transform in one step
normalized_FGM = scaler.fit_transform(np.array(df['FGM']).reshape(-1, 1))
normalized_DRIBBLES = scaler.fit_transform(np.array(df['DRIBBLES']).reshape(-1, 1))
normalized_TOUCH_TIME = scaler.fit_transform(np.array(df['TOUCH_TIME']).reshape(-1, 1))
normalized_SHOT_DIST = scaler.fit_transform(np.array(df['SHOT_DIST']).reshape(-1, 1))
normalized_CLOSE_DEF_DIST = scaler.fit_transform(np.array(df['CLOSE_DEF_DIST']).reshape(-1, 1))
normalized_PTS = scaler.fit_transform(np.array(df['PTS']).reshape(-1, 1))
normalized_Player_Height = scaler.fit_transform(np.array(df['Player_Height']).reshape(-1, 1))
normalized_Defender_Height = scaler.fit_transform(np.array(df['Defender_Height']).reshape(-1, 1))
normalized_Height_Diff = scaler.fit_transform(np.array(df['Height_Diff']).reshape(-1, 1))
normalized_Player_Weight = scaler.fit_transform(np.array(df['Player_Weight']).reshape(-1, 1))
normalized_Defender_Weight = scaler.fit_transform(np.array(df['Defender_Weight']).reshape(-1, 1))

#Join to test

test = test.join(pd.DataFrame(normalized_FGM),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_DRIBBLES),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_TOUCH_TIME),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_SHOT_DIST),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_CLOSE_DEF_DIST),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_PTS),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_Player_Height),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_Defender_Height),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_Height_Diff),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_Player_Weight),lsuffix='_left', rsuffix='_right')
test = test.join(pd.DataFrame(normalized_Defender_Weight),lsuffix='_left', rsuffix='_right')


#################################################


#Split Response and feature
X = test[:100000]
y = pd.DataFrame([int(i) for i in (encoded_Shot_made.iloc[:,1])][:100000])
sum(y)

#################################################

# define the keras model
from keras.regularizers import l2

model = Sequential()

#good 0.00001
model.add(Dense(16, input_dim=142, activation='relu',kernel_regularizer=l2(0.00001)))
#model.add(Dense(8, activation='relu'))
#model.add(Dense(50, activation='relu'))
#model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#Compile model
#regulariser

#sgd = optimizers.SGD(lr=0.000001)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


#Fit model #1000 epochs
history = model.fit(X, y, epochs=1000, batch_size=400, validation_split=0.2,verbose=0)
#Plot
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.legend()
plt.show()

#Print Accuracy
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

X1 = test[100000:]
y1 = pd.DataFrame([int(i) for i in (encoded_Shot_made.iloc[:,1])][100000:])
pred1 = model.predict_classes(X1)
sum(pred1)

confusion_matrix(y1,pred1)

X.to_csv (r'Xtrain.csv', index = None, header=True)
y.to_csv (r'Ytrain.csv', index = None, header=True)
X1.to_csv (r'Xtest.csv', index = None, header=True)
y1.to_csv (r'Ytest.csv', index = None, header=True)

sum(y)/len(df)


#Accuracy: 90.79

