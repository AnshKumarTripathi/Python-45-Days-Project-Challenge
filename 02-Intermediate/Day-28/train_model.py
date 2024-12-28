import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv('D:/45-Days-Challege-JS-Python/IMDB Dataset.csv')

# Preprocess text data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['review'])
y = df['sentiment']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model and vectorizer
joblib.dump(model, 'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = sum(y_pred == y_test) / len(y_test)
print(f'Model Accuracy: {accuracy}')
