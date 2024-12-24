import pyterrier as pt
import pandas as pd
import os

class Retriever():
    """
    Retriever class used for data retrieval operations of query, 
    through merging the dataset with the query-transformed model.
    """
    def __init__(self):
        self.dataset = pt.get_dataset("irds:cranfield")
        self.index_path = os.path.join("C:", "retrieve", "index")
        self.model = pt.BatchRetrieve(self.index_path, wmodel = "BM25")
        self.collection = self.get_collection()


    def get_collection(self):
        dataset = pt.get_dataset("irds:cranfield")
        corpus_iter = dataset.get_corpus_iter()
        collection = pd.DataFrame(corpus_iter, columns=["docno", "title", "text"])
        collection = collection.drop_duplicates()
        return collection


    def iterate_df(self, data):
        result = []
        for _, row in data.iterrows():
            text = dict()
            text["docno"] = row["docno"]
            text["title"] = row["title"]
            text["content"] = f"{row["text"][:200]}..."
            result.append(text)
        return result


    def get_serp(self, query: str, top: int = 30):
        result = self.model.transform(query)

        merged = pd.merge(result, self.collection, how='left', on=['docno'])
        final = self.iterate_df(merged.head(top))
        return final


    def get_data_by_docno(self, docno):
        filtered: pd.DataFrame = self.collection[self.collection["docno"] == str(docno)]
        if not filtered.empty:
            result = dict()
            row = filtered.iloc[0]
            result["title"] = row["title"]
            result["content"] = row["text"]
            return result
        else:
            raise ValueError(f"Document with docno: {docno} not found")


def main():
    retr = Retriever()
    docno = 109

    result = retr.get_data_by_docno(docno)
    print(result)

if __name__ == "__main__":
    main()