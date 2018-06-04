import json


class Indexer:

    def __init__(self):
        with open('./data/repo/docs.json', 'r') as f:
            self.docs = json.load(f)

        with open('./data/repo/vocab.json', 'r') as f:
            self.vocab = json.load(f)

        self.postingsFile = {}



    def saveInJSON(self,make=False):
        if make:
            self.makeIndex()
        with open('./data/index/index.json', 'w') as fp:
            json.dump(self.index, fp, sort_keys=True, indent=4)

    def makeIndex(self):
        self.index={word_id:[] for word_id in range(len(self.vocab))}
        for (doc_id,doc) in self.docs.items():
            for i in doc[1]:
                self.index[i[0]].append((doc_id,i[1]))
        


if __name__ == "__main__":
    ind = Indexer()
    ind.saveInJSON(make=True)