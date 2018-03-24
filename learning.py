from bayesian import BayesianFilter
import json, sys







def Learning():
    bf = BayesianFilter("Learning")
    f = open("./learning_data/input.txt", "r")
    lines = f.readlines()
    for line in lines:
        s = line.rstrip().split('$')
        bf.Learning(s[0],s[1])
    bf.Save_data()


def Predict():
    bf = BayesianFilter("Predict")
    q = "지금 기상이 어때"
    print(q)
    print(">> ", bf.Predict(q))


def ptest():
    dic = {}

    w_data = open("./w_data/w_data.json").read()
    data = json.loads(w_data)


    l_data = data["label_cnt"]["오늘날씨"]

    dic = data["label_cnt"]
    print(dic)


if __name__ =="__main__":

    if sys.argv[1] == "test":
        Learning()
    else:
        Predict()
