import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the Chicago Cricket data
df = pd.read_csv('chicago_cricket_data.csv')

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(df, df['Result'], test_size=0.25)

# Train a machine learning model on the training set
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the machine learning model on the test set
score = model.score(X_test, y_test)
print('Score:', score)

# Use the machine learning model to make predictions
predictions = model.predict(X_test)
print('Predictions:', predictions)
