import math
from collections import Counter

class TFIDF:
    def __init__(self, documents):
        self.documents = documents
        self.tf = []
        self.idf = {}
        self.tf_idf = []

        self.compute_tf()
        self.compute_idf()
        self.compute_tf_idf()

    def compute_tf(self):
        for doc in self.documents:
            doc_tokens = doc.split()
            doc_length = len(doc_tokens)
            term_frequency = Counter(doc_tokens)
            self.tf.append({term: freq/doc_length for term, freq in term_frequency.items()})

    def compute_idf(self):
        total_documents = len(self.documents)
        for doc in self.documents:
            doc_tokens = set(doc.split())
            for token in doc_tokens:
                if token not in self.idf:
                    count = sum(1 for doc in self.documents if token in doc)
                    self.idf[token] = math.log(total_documents/count)

    def compute_tf_idf(self):
        for doc_tf in self.tf:
            doc_tf_idf = {}
            for term, tf in doc_tf.items():
                doc_tf_idf[term] = tf * self.idf.get(term, 0)
            self.tf_idf.append(doc_tf_idf)

    def search(self, query):
        query_tokens = query.split()
        query_tf = {term: query_tokens.count(term)/len(query_tokens) for term in query_tokens}
        query_tf_idf = {term: tf * self.idf.get(term, 0) for term, tf in query_tf.items()}

        scores = []
        for doc_tf_idf in self.tf_idf:
            score = sum(query_tf_idf.get(term, 0) * doc_tf_idf.get(term, 0) for term in query_tokens)
            scores.append(score)

        sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return sorted_indices


# Example usage:
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

tfidf = TFIDF(documents)
query = "first document"
result_indices = tfidf.search(query)

print("Documents ranked by TF-IDF scores for query:", query)
for idx in result_indices:
    print(documents[idx])
