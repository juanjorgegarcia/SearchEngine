# class FileReader:

#     def __init__(self,filepath):
#         with open(filepath, "r") as f:
#             f = f.read()
#         # self.string = f.lower().replace(",.:/?!][","")
#         self.string = f
#         self.list = self.string.split()
#         self.unique_words = list(set(self.list))
#         self.paragraphs = {}
#         self.postingsFile = {}

#     def splitByParagraphs(self):
#         paragraph = ""
#         paragraphs = []
#         self.paragraphs = {}
#         c=0
#         for i in range(len(self.string)):
#             paragraph+=self.string[i]
#             if self.string[i-1] == "\n" and self.string[i] == "\n":
#                 c+=1
#                 self.paragraphs[c] = paragraph
#                 paragraph = ""
    
#     def countWordsInParagraphs(self):
#         self.postingsFile = {}
#         for word in self.unique_words:
#             self.postingsFile[word] = []
#             for paragraph in self.paragraphs.keys():
#                 if word in self.paragraphs[paragraph]:
#                     wordFrequency = self.paragraphs[paragraph].count(word)
#                     self.postingsFile[word].append([paragraph,wordFrequency])

# oi = FileReader("./sherlock.txt")
# oi.splitByParagraphs()
# oi.countWordsInParagraphs()
# print(oi.postingsFile)

        
        


            

# from string import maketrans # Required to call maketrans function.

# f = open("./sherlock.txt","r")
# # f_string = f.read().lower()
# # f_splitted = f_string.split()

# # # # print(f_splitted[0])
# # # paragraph = ""
# # # paragraphs = []
# # # for i in range(len(f_string)):
# # #     paragraph+=f_string[i]
# # #     if f_string[i-1] == "\n" and f_string[i] == "\n":
# # #         paragraphs.append(paragraph)
# # #         paragraph = ""
# # paragraph = ""
# # paragraphs = []
# # paragraphs = {}
# # c=0
# # for i in range(len(f_string)):
# #     paragraph+=f_string[i]
# #     if f_string[i-1] == "\n" and f_string[i] == "\n":
# #         c+=1
# #         paragraphs[c] = paragraph
# #         # paragraphs.append(paragraph)
# #         paragraph = ""


# # print(paragraphs[6])    

# # paragraphs = [for i in range(len) if]

# # oi = '/n'
# # unique_values = list(set(f_splitted))
# # print((f_splitted[0]))
# # # print((unique_values))
# # print(f_string.count("\n"))

