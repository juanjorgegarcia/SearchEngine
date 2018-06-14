import json
import re

class Repository:
    def __init__(self):
        with open('./data/raw/raw.json', 'r', encoding='utf8') as f:
            self.rawParagraphs = json.load(f)
        with open("./sherlock.txt",'r', encoding='utf8') as f:
            doc_str = f.read()
        reg = re.sub(r'[^ \s a-z0-9]',"", doc_str.lower())
        # f = f.lower().replace('",;/\})({.:/?!][',"")
        self.word_list = reg.split()
        self.word_list = sorted(list(set(self.word_list)))
        self.vocabulary = {}
        self.index = {}
        self.docs = {}

    def processParagraphs(self):
        self.processedParagraphs = {}
        for key, value in self.rawParagraphs.items():
            self.processedParagraphs[key] = re.sub(r'[^ \s a-z0-9]', "", value.lower())

    def saveInJSON(self, make=False):
        if make:
            self.processParagraphs()
            self.makeVocabulary()
            self.makeDocs()
            # self.makeIndex()
        with open('./data/repo/docs.json', 'w') as fp:
            json.dump(self.docs, fp, indent=4)
        with open('./data/repo/vocab.json', 'w') as fp:
            json.dump(self.vocabulary, fp, sort_keys=True, indent=4)
        with open('./data/repo/inv_vocab.json', 'w') as fp:
            json.dump(self.inv_dict, fp, sort_keys=True, indent=4)

    def makeVocabulary(self):
        self.vocabulary = {key:self.word_list[key] for key in range(len(self.word_list))}
        self.inv_dict = {v:k for (k,v) in self.vocabulary.items()}
    
    def makeDocs(self):
        self.docs = {}
        for (key,value) in self.processedParagraphs.items():
            wordlist = []
            docList = []
            for word in value.split():
                wordlist.append((self.inv_dict[word],value.count(word)))
                # docList.append((key,value.count(word)))
            # self.index[self.inv_dict[word]] = docList
            self.docs[key] = [value,wordlist]

    def makeIndex(self):

        # for (word_id,word) in self.vocabulary.items():
        #     self.index[word_id] = []
        #     for (doc_id,doc) in self.docs.items():
        #         if word in doc[0]:
        #             self.index[word_id].append(doc_id)

        self.index={word_id:[] for word_id in range(len(self.vocabulary.items()))}
        for (doc_id,doc) in self.docs.items():
            for i in doc[1]:
                self.index[i[0]].append((doc_id,i[1]))

if __name__ == "__main__":
    repo = Repository()
    repo.saveInJSON(make=True)
