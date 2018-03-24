from konlpy.tag import Twitter
import os, math, json
class BayesianFilter:
    """

    word_set 안써도 되는건가 모르겠네
    """
    def __init__(self, type):
        self.label_cnt = {}         #학습한 라벨의 종류와 횟수 Key : label name, Value : count
        #self.word_set = set()       #학습한 단어들 집합
        self.word_freq = {}         #특정 라벨에 나타난 단어의 빈도
        self.data_dir = "./w_data/"   #가중치(?) 데이터를 저장할 경로
        if type == "Learning":
            print('<< learing mode >>')
        elif type == "Predict":
            print('<< prediction mode >>')
            self.__load_data()

    # __word_split
    #   private
    #   @ 문장을 입력받아 단어들의 리스트로 변환
    #   input
    #       - text           : 입력 문자열
    #   return
    #       - word_list      : 단어를 담은 리스트
    def __word_split(self, text):
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
        if not label in self.label_cnt:                #라벨 추가
            self.label_cnt[label] = 0
        self.label_cnt[label] += 1
        if not label in self.word_freq:
            self.word_freq[label] = {}

        word_list = self.__word_split(text)
        for w in word_list:
            #self.word_set.add(w)                       #단어 집합에 추가
            if not w in self.word_freq[label]:         #해당 라벨에 속한 단어에 추가
                self.word_freq[label][w] = 0
            self.word_freq[label][w] += 1

        return 0

    # __calculate_label_cnt
    #   private
    #   @ 입력받은 라벨이 전체 학습 횟수 중 몇 번이나 나타났는지 비율
    #     해당 라벨을 학습한 횟수 / 라벨 전체를 학습한 횟수
    #   input
    #       - label : 라벨 문자열
    #   return
    #       - (해당 라벨을 학습한 횟수 / 전체 라벨의 학습 횟수)를 나타내는 실수
    def __calculate_label_cnt(self, label):
        return self.label_cnt[label] / sum(self.label_cnt.values())

    # __calculate_word_freq
    #   private
    #   @ 해당 단어가 해당 라벨에 나타난 비율
    #   input
    #       - word      : 검사할 단어의 문자열
    #       - label     : 검사할 라벨의 문자열
    #   return
    #       - 해당 단어가 라벨에서 나타난 횟수 / 해당 라벨에서 나타난 전체 단어의 빈도 수
    def __calculate_word_freq(self, word, label):
        val = 1;
        if word in self.word_freq[label]:
            val = self.word_freq[label][word]
        return val / sum(self.word_freq[label].values())

    # __calculate_score
    #   private
    #   @ 단어 리스트와 라벨을 입력받아 해당 라벨의 점수를 계산함
    #
    #   input
    #       - word_list     :
    #       - label         :
    #   return
    #       -
    def __calculate_score(self, word_list, label):
        score = math.log(self.__calculate_label_cnt(label))
        for w in word_list:
            score += math.log(self.__calculate_word_freq(w, label))
        return score

    def Predict(self, text):
        high_score = -9999
        result_label = ""
        word_list = self.__word_split(text)
        for label in self.label_cnt.keys():
            score = self.__calculate_score(word_list, label)
            if score > high_score :
                high_score = score
                result_label = label
        return result_label

    def __load_data(self):
        json_data = open(self.data_dir + "w_data.json").read()
        data = json.loads(json_data)
        self.label_cnt = data["label_cnt"]
        self.word_freq = data["word_freq"]

    def Save_data(self):
        #디렉토리 생성
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)

        result_data = "{ \"label_cnt\" : " + json.dumps(self.label_cnt, ensure_ascii=False) + ", \"word_freq\" : " + json.dumps(self.word_freq, ensure_ascii=False) + " }"
        with open(self.data_dir + "w_data.json", "w") as f:
            f.write(result_data)
