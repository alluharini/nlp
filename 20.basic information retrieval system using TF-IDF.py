from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "Machine learning is the study of computer algorithms that improve automatically through experience.",
    "Natural language processing (NLP) is a subfield of artificial intelligence and linguistics concerned with interactions between computers and human language.",
    "Deep learning models can achieve state-of-the-art performance in various tasks such as image recognition, natural language processing, and more."
]
query = "What is machine learning?"
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
query_tfidf = vectorizer.transform([query])
cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()
document_scores = [(idx, score) for idx, score in enumerate(cosine_similarities)]
sorted_document_scores = sorted(document_scores, key=lambda x: x[1], reverse=True)
print("Query:", query)
print("\nRanked Documents:")
for idx, score in sorted_document_scores:
    print(f"Document {idx + 1}: Similarity Score = {score:.4f}")
    print(f"Document Text: {documents[idx]}")
    print()