from bayesian import BayesianFilter






def test():
    bf = BayesianFilter()
    bf.Learning("아무런 메시지가 없으면 성공적으로 깃이 추적을 할 수 있게 저장소에 추가된 겁니다.")


if __name__ =="__main__":
    #test()

    dic = {"f" : {"ff" : 1, "fff" : 2, "ffff" : 3}, "s":{"ss" : 123}}


    print(sum(dic["f"].values()))
