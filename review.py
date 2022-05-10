
from playsound import playsound

class Review:

    def __init__(self, words_df, fn, ite):
        self.word = words_df['word']
        self.chin = words_df['trans']
        self.ite = ite
        self.fn = fn


    def english_to_chinese(self):
        if (len(self.word) != 0):
            misW = []
            misC = []
            for i in range(len(self.chin)):
                critic = False
                print("-----(第{}个单词)-----".format(i + 1))
                print(self.word[i] + ":")
                self.word = self.word[i]
                playsound(r'./mp3/' + self.fn + r'/' + self.word[i] + '.mp3')
                trans = input()
                # 判断答案是否正确
                for j in range(len(self.chin[i])):
                    if (trans in self.chin[i][j] and trans != '' and trans != ' '):
                        critic = True
                        break
                # 根据答案判断进行不同的响应
                if (critic):
                    print("正确！！！")
                else:
                    print("很遗憾答错了")
                    print("正确答案（部分）:")
                    for j in range(len(self.chin[i])):
                        print(self.chin[i][j])
                    misW.append(self.word[i])
                    misC.append(self.chin[i])
            return misW, misC, False
        else:
            print("全部正确！！！")
            return True


    def chinese_to_english(self):
        if (len(self.word) != 0):
            misW = []
            misC = []
            for i in range(len(self.chin)):
                print("-----(第{}个单词)-----".format(i + 1))

                for j in range(len(self.chin[i])):
                    print(self.chin[i][j])

                playsound(r'./mp3/' + self.fn + r'/' + self.word[i] + '.mp3')
                word = input()
                if (word == self.word[i]):
                    print("正确！！！")  # 若回答正确移除
                else:
                    print("很遗憾答错了！")
                    print("正确答案：")
                    print(self.word[i])
                    misW.append(self.word[i])
                    misC.append(self.chin[i])
            return misW, misC, False
        else:
            print("全部正确！！！")
            return True
