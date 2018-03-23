from konlpy.tag import Twitter
import os, math, json
class BayesianFilter:
    def __init__(self):
        self.label_cnt = {}         #학습한 라벨의 종류와 횟수 Key : label name, Value : count
        self.word_set = set()       #학습한 단어들 집합
        self.word_freq = {}         #특정 라벨에 나타난 단어의 빈도
        self.data_dir = "./data/"   #가중치(?) 데이터를 저장할 경로


    # __word_split
    #   private
    #   @ 문장을 입력받아 단어들의 리스트로 변환
    #   input
    #       - text : 입력 문자열
    #   return
    #       - word_list : 단어를 담은 리스트
    def __word_split(self, text):
        print('word split call')
        word_list = []
        words = Twitter().pos(text, norm=True, stem=True)
        for word in words:
            if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                word_list.append(word[0])
        return word_list



    # Learning
    #   public
    #   @ 문장과 라벨을 입력받아 학습한다.
    #     문장에 포함된 단어를
    #   input
    #       - text      : 학습할 문장의 문자열
    #       - label     : 학습할 문장의 라벨을 나타내는 문자열
    def Learning(self, text, label):
        print('Learning call')
        if not label in self.label_cnt:                #라벨 추가
            self.label_cnt[label] = 0
        self.label_cnt[label] += 1
        word_list = self.__word_split(text)
        for w in word_list:
            self.word_set.add(w)                       #단어 집합에 추가
            if not w in self.word_freq[label]:         #해당 라벨에 속한 단어에 추가
                self.word_freq[label][w] = 0
            self.word_freq[label][w] += 1


    def __calculate_label_cnt(self, label):
        return self.label_cnt[label] / sum(self.label_cnt.values)
    def __calculate_word_freq(self, word, label):
        val = 1;
        if word in self.word_freq[label]:
            val = self.word_freq[label][word]
        return val / sum(self.word_freq[label].values())
    def __calculate_score(self, word_list, label):
        score = math.log(self.__calculate_label_cnt(label))
        for w in word_list:
            score += math.log(self.__calculate_word_freq(w, label))
        return score

    def predict(self, text):
        high_score = -9999
        result_label = ""
        for label in self.label_cnt.keys():
            word_list = self.__word_split(text)
            score = self.__calculate_score(word_list, label)
            if score > high_score :
                high_score = score
                result_label = label

        return label



    def __save_file(self):
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)
        with open(self.data_dir + "word_dict.json", "w") as f:
            f.write(json.dumps(self.word_dict, ensure_ascii=False))
        with open(self.data_dir + "category_dict.json", "w") as f:
            f.write(json.dumps(self.category_dict, ensure_ascii=False))
        with open(self.data_dir + "words.txt", "w") as f:
            f.write(str(self.words))
