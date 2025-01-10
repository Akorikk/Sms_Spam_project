# Sms_Spam_project

This project involves building a spam message classifier using various libraries and machine learning algorithms. The primary goal is to classify messages as spam or not spam (ham).

# Libraries Used
* Pandas: For data manipulation and analysis.
* NumPy: For numerical operations and array handling.
* NLTK: For natural language processing (NLP) tasks like text preprocessing, stopwords removal, and stemming.
* Sklearn: For machine learning models, vectorization, and data splitting.
* WordCloud: For generating visualizations of frequently occurring words in the dataset.
* Matplotlib: For data visualization and exploratory data analysis (EDA).
* Pickle: For saving and loading the trained model.
* Streamlit: For creating a user interface for the classifier.

# Why stratify=y?
The stratify=y argument ensures that the training and testing sets have the same proportion of spam and ham messages as the original dataset. This is important because the data is imbalanced, meaning there are significantly more ham messages than spam messages. Stratification ensures that both the training and testing sets represent the same distribution of classes.

# Data Preprocessing

We used NLTK for:

Removing non-alphabetic characters
Converting text to lowercase
Tokenizing and stemming the words

# Naive Bayes Algorithm - MultinomialNB
We used the Multinomial Naive Bayes (MultinomialNB) algorithm because it is well-suited for text classification problems, especially when dealing with word counts or frequencies. This algorithm works well when the features (words) are independent, making it ideal for spam classification tasks.

# Model Selection
We experimented with three Naive Bayes algorithms:

GaussianNB
MultinomialNB
BernoulliNB
The best performing algorithm was MultinomialNB, which gave an accuracy score of 97% and a precision score of 100%.


# Why TfidfVectorizer
TfidfVectorizer is generally better for classification because it
Weighs terms by their importance (frequency within a document vs. rarity across the corpus).
Helps reduce the impact of common words and highlights more distinctive terms.
Works well with classifiers like Naive Bayes, which is often used for text classification tasks.