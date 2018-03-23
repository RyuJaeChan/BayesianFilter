from konlpy.tag import Twitter

class BayesianFilter:
    def __init__(self):
        self.label_cnt = {}         #학습한 라벨의 종류와 횟수
        self.word_set = set()       #학습한 단어들 집합
        self.word_freq = {}         #특정 라벨에 나타난 단어의 빈도


    def __word_split(self, text):
        print('word split call')
        


    def leaning(self, text):
        word_list = self.__word_split(text)
