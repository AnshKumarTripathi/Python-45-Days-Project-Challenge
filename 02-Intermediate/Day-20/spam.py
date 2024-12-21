# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import nltk
from nltk.corpus import stopwords
import string

# Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Lowercase text
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()  # Split into words
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return ' '.join(words)

# Load the dataset (replace 'spam.txt' with your dataset path)
# Assuming the dataset is tab-separated
df = pd.read_csv('D:/45-Days-Challege-JS-Python/SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])

# Preprocess messages
df['message'] = df['message'].apply(preprocess_text)

# Convert labels to binary (1 for spam, 0 for ham)
df['label'] = df['label'].map({'spam': 1, 'ham': 0})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Convert text data to feature vectors
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)

# Predict the labels on the test set
y_pred = classifier.predict(X_test_counts)

# Evaluate the classifier
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
