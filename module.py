from bayesian import BayesianFilter
import os, sys

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
    file_path = os.path.dirname(__file__)+ "/learning_data"
    label = ""
    bf = BayesianFilter("Learning");
    files = os.listdir(file_path)
    print(file_path)

    if len(sys.argv) < 2:
        print(">> input directory")


    for file in files :
        full_name = os.path.join(file_path, file)
        label = file.split('.')[0]
        print(label)
        bf.ReadFile_And_Learn(label, full_name)
    bf.Save_data(sys.argv[1])
    #bf.Learning(label, file_path)
