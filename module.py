from bayesian import BayesianFilter
import os

def Learning():
    bf = BayesianFilter("Learning");
    bf.ReadFile_And_Learn("./learning_data/input.txt")
    bf.Save_data()


def Predict(command):
    bf = BayesianFilter("Predict")
    res = bf.Predict(command)
    print('command : ' + command)
    print(">> result : ", res)
    return res

if __name__ =="__main__":
    file_path = ""
    label = ""
    bf = BayesianFilter("Learning");
    files = os.listdir("./learning_data")
    for file in files :
        full_name = os.path.join("./learning_data", file)
        label = file.split('.')[0]
        print(label)
        bf.ReadFile_And_Learn(label, full_name)
    bf.Save_data()
    #bf.Learning(label, file_path)
