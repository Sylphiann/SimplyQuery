import pyterrier as pt
import os

index_path = os.path.join(
    "C:", "retrieve", "index"
)
os.makedirs(index_path, exist_ok=True)

# Indexing: Cranfield dataset
# A small corpus of 1,400 scientific abstracts
# Source: https://ir-datasets.com/cranfield.html
indexer = pt.index.IterDictIndexer(index_path)
indexref = indexer.index(pt.get_dataset("irds:cranfield").get_corpus_iter())