from bayesian import BayesianFilter






def test():
    bf = BayesianFilter()
    bf.Learning("오늘 날씨 어때", "오늘날씨")
    bf.Learning("오늘 기상정보", "오늘날씨")
    bf.Learning("기상정보", "오늘날씨")
    bf.Learning("오늘 기상", "오늘날씨")
    bf.Learning("오늘 기온이 어때", "오늘날씨")
    bf.Learning("지금 몇시야", "오늘날씨")
    bf.Learning("몇시지", "오늘날씨")
    bf.Learning("현재 시간", "현재시간")
    bf.Learning("현재 몇시 몇분이야", "현재시간")

    q = "오늘 날씨가 어떨까"
    result = bf.predict(q)
    print(q)
    print(result)

def ptest():
    dic = {"f" : {"ff" : 1, "fff" : 2}}
    if not "ffff" in dic["f"]:
        dic["f"]["ffff"] = 0

if __name__ =="__main__":
    test()
