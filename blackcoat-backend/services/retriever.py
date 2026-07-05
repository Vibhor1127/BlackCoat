import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from services.preprocessor import preprocess

# Load artifacts once at startup
with open('artifacts/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('artifacts/tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

df = pd.read_pickle('artifacts/dataframe.pkl')

def retrieve_top_k(query: str, k: int = 4) -> list[dict]:
    cleaned = preprocess(query)
    query_vec = vectorizer.transform([cleaned])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = np.argsort(scores)[::-1][:k]

    results = []
    for idx in top_indices:
        row = df.iloc[idx]
        score = float(scores[idx])
        results.append({
            "provision_id":     str(row.get('provision_id', '')),
            "title":            str(row.get('title', '')).title(),
            "article_section":  str(row.get('article_section', 'N/A')),
            "court_or_source":  str(row.get('source_type', '')),
            "year":             str(row.get('enforcement_year', 'N/A')),
            "verbatim":         str(row.get('verbatim_text_excerpt', '')),
            "simplified":       str(row.get('simplified_explanation', '')),
            "case_1":           str(row.get('landmark_case_1', 'N/A')),
            "case_1_year":      str(row.get('lc1_year', 'N/A')),
            "case_1_holding":   str(row.get('lc1_holding_summary', 'N/A')),
            "case_2":           str(row.get('landmark_case_2', 'N/A')),
            "case_2_year":      str(row.get('lc2_year', 'N/A')),
            "case_2_holding":   str(row.get('lc2_holding_summary', 'N/A')),
            "status":           str(row.get('current_precedent_status', 'N/A')),
            "relevance_score":  round(score * 100, 1),
        })
    return results
