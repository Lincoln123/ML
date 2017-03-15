from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc



def getData(data, check):

    actual = list()
    predictions = list()
    for i,x in enumerate(data):
        if check[i] != 'U':
            predictions.append(x)
            if check[i] == 'F':
                actual.append(1)
            else:
                actual.append(0)

    return actual, predictions

def summ(systems, i):

    ans = 0
    for j in range(0, len(systems)):
        ans += systems[j][i]
    return ans

def func(systems):
    return [float(summ(systems, i)) / float(3) for i,x in enumerate(systems[0])]

if __name__ == '__main__':
    data = read_csv('выгрузка.csv', ',')


    P = func([data['p' + str(i) + '_Fraud'] for i in range(1, 4)])

    plt.figure()

    actual, predictions = getData(P, data['CLASS'])
    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)

    plt.plot(false_positive_rate, true_positive_rate, label='%s ROC, AUC = %0.2f, Gini = %0.2f' % ('p_Fraud', roc_auc, (roc_auc * 2) - 1))

    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right', fontsize='small')
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.0])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()