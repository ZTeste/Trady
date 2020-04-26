import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, accuracy_score

FILE = "../data/results.csv"
MODEL_FILENAME = 'model.sav'

data = pd.read_csv(FILE)

X = data.drop(columns=['date', 'bidopen', 'bidclose', 'bidhigh', 'bidlow', 'direction'])
y = data['direction']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)


model = RandomForestClassifier(n_estimators=300, n_jobs=1, criterion='gini', oob_score=True, random_state=0)

model.fit(X_train, y_train)

print('Oob_score_ Score: ', model.oob_score_)


y_pred = model.predict(X_test)
f1_score = f1_score(y_pred, y_test)
print("F1 Score : ", f1_score)

print("Saving model...")
pickle.dump(model, open(MODEL_FILENAME, 'wb'))

print("end")
