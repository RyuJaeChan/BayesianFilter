from bayesian import BayesianFilter
import json, sys, os

def Learning():
    bf = BayesianFilter("Learning")
    f = open("./learning_data/input.txt", "r")
    lines = f.readlines()
    for line in lines:
        s = line.rstrip().split('$')
        bf.Learning(s[0],s[1])
    bf.Save_data()

def Predict(command):
    bf = BayesianFilter("Predict")
    res = bf.Predict(command)
    print('command : ' + command)
    print(">> result : ", res)
    return res

if __name__ =="__main__":
    if sys.argv[1] == "test":
        Learning()
    else:
        Predict(sys.argv[1])
