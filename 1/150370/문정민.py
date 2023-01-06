import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):

    p = 0

    term = {}
    private = {}
    raw = []
    rst = []

    date = datetime.datetime(int(today.split(".")[0]), int(today.split(".")[1]), int(today.split(".")[2]))

    for i in terms:
        term[i.split(" ")[0]] = i.split(" ")[1]

    for j in privacies:
        private[p] = j.split(" ")[0]

        raw.append(j.split(" ")[1])
        p += 1

    p = 0

    for k in private:
        s = term[raw[p]]
        z = datetime.datetime(int(private[p].split(".")[0]), int(private[p].split(".")[1]), int(private[p].split(".")[2]))

        aa = z + relativedelta(months=int(s))

        if aa <= date:
            rst.append(p+1)

        p += 1

    return rst

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))