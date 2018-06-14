import json
class SearchEngine:

    def __init__(self):
        with open('./data/index/index.json', 'r') as f:
            self.index = json.load(f)
        with open('./data/repo/inv_vocab.json', 'r') as f:
            self.inv_vocab = json.load(f)
        with open('./data/raw/raw.json', 'r') as f:
            self.raw = json.load(f)


    def search(self,query):
        terms_list = query.split()
        for term in query.split():
            word = "{}".format(self.inv_vocab[term])
            cnt=1
            for i in range(len(self.index[word])):
                if self.index[word][i][1]>cnt:
                    cnt = i
            print("This is the best match\n")
            print(self.raw[self.index[word][cnt][0]])
        # alo = [self.index["{}".format(self.inv_vocab[term])]for term in query.split()]
        # print(alo)

if __name__ == "__main__":
    running = True
    while running:
        print("##########################################")
        user_input=input("Press (0) to search:\nPress (1) to exit: ")
        print("##########################################")
        if user_input == "0":
            query=input("Insert your query: ")
            s = SearchEngine()
            s.search(query.lower())
            
        else:
            running = False
        