import json


class Extractor:

    def __init__(self,filepath):
        with open(filepath, "r") as f:
            self.string = f.read()
        # self.string = f.lower().replace(",.:/?!][","")

    def splitByParagraphs(self):
        paragraph = ""
        paragraphs = []
        self.paragraphs = {}
        c = 0
        for i in range(len(self.string)):
            paragraph += self.string[i]
            if self.string[i-1] == "\n" and self.string[i] == "\n":
                c += 1
                self.paragraphs[c] = paragraph
                paragraph = ""

    def saveInJSON(self):
        with open('./data/raw/raw.json', 'w') as fp:
            json.dump(self.paragraphs, fp, sort_keys=True, indent=4)

    # def saveInTxt(self):
    #     with open('./raw/raw.txt', 'wb') as fp:
    #         pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    extractor = Extractor("./sherlock.txt")
    extractor.splitByParagraphs()
    extractor.saveInJSON()
