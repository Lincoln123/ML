from pandas import read_csv

def es(data, threshold):

    return [1 if x >= threshold else 0 for x in data]

def summ(systems, i):

    ans = 0
    for j in range(0, len(systems)):
        ans += systems[j][i]
    return ans

def vote(systems):

    return ['F' if int(0.5 + ((float(summ(systems, i)) - 0.5)/float(len(systems)))) == 1 else 'G' for i,x in enumerate(systems[0])]

def TN_rate(data, check):

    tn = len([x for i,x in enumerate(data) if (check[i] == 'F' and data[i] == 'F')])
    fp = len([x for i,x in enumerate(data) if (check[i] == 'F' and data[i] == 'G')])
    return float(tn) / float(tn+fp)

def FP_rate (data, check):

    return float(1) - TN_rate(data, check)

if __name__ == '__main__':
    data = read_csv('выгрузка.csv', ',')

    threshold = 0.5


    majority = vote([es(data['p' + str(i) + '_Fraud'], threshold) for i in range(1, 4)])


    print FP_rate(majority, data['CLASS'])


    threshold = 0.8

    majority = vote([es(data['p' + str(i) + '_Fraud'], threshold) for i in range(1, 4)])

    print FP_rate(majority, data['CLASS'])
