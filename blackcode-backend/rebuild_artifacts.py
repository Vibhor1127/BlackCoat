import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from services.preprocessor import preprocess

# Path definitions
csv_path = 'data/Indian_Law_and_Supreme_Court_Database_2026_NLPRAG.csv'
df_pickle_path = 'artifacts/dataframe.pkl'
matrix_pickle_path = 'artifacts/tfidf_matrix.pkl'
vectorizer_pickle_path = 'artifacts/tfidf_vectorizer.pkl'

print("Loading CSV data...")
# Read the master CSV
df = pd.read_csv(csv_path)

# Print initial info
print(f"Loaded {len(df)} rows.")

# Ensure correct datatypes and handle missing values
df = df.fillna("Not Applicable / N.A.")

# Recreate combined_text
print("Generating combined_text...")
df['combined_text'] = (
    df['title'].astype(str).str.lower() + " " +
    df['verbatim_text_excerpt'].astype(str).str.lower() + " " +
    df['simplified_explanation'].astype(str).str.lower() + " " +
    df['keywords'].astype(str).str.lower()
)

# Apply preprocessing to generate final_cleaned_text
print("Preprocessing text (this may take a few seconds)...")
df['final_cleaned_text'] = df['combined_text'].apply(preprocess)

# Add mock columns for intermediate steps if they were in the original dataframe
# (to maintain 100% compatibility with original schema)
df['cleaned_text_tokens'] = df['combined_text']
df['stemmed_text'] = df['combined_text']
df['lemmatized_text'] = df['combined_text']

# Order columns to match the original dataframe columns exactly
original_cols = [
    'provision_id', 'source_type', 'part_chapter', 'article_section', 'title',
    'verbatim_text_excerpt', 'simplified_explanation', 'keywords', 'landmark_case_1',
    'lc1_year', 'lc1_holding_summary', 'landmark_case_2', 'lc2_year', 'lc2_holding_summary',
    'upsc_relevance', 'category', 'enforcement_year', 'nodal_ministry', 'legal_classification',
    'punishment_quantum', 'exceptions_and_limitations', 'cross_references', 'bench_strength',
    'current_precedent_status', 'primary_source_url', 'current_law_mapping', 'row_status',
    'combined_text', 'cleaned_text_tokens', 'stemmed_text', 'lemmatized_text', 'final_cleaned_text'
]
df = df[original_cols]

# Save the dataframe pickle
print(f"Saving dataframe to {df_pickle_path}...")
df.to_pickle(df_pickle_path)

# Initialize and fit TF-IDF Vectorizer
print("Fitting TF-IDF Vectorizer...")
vectorizer = TfidfVectorizer(max_features=5000)
tfidf_matrix = vectorizer.fit_transform(df['final_cleaned_text'])

# Save the vectorizer and matrix pickles
print(f"Saving vectorizer to {vectorizer_pickle_path}...")
with open(vectorizer_pickle_path, 'wb') as f:
    pickle.dump(vectorizer, f)

print(f"Saving matrix to {matrix_pickle_path}...")
with open(matrix_pickle_path, 'wb') as f:
    pickle.dump(tfidf_matrix, f)

print("Artifacts rebuild complete!")
