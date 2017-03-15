from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc


infile = read_csv("выгрузка.csv", ",")

actual = []
prediction = []

for i in range(1, 6):
    for c, p in zip(infile["CLASS"], infile["p"+str(i)+"_Fraud"]):
        if c != "U":
            prediction.append(p)
            if c == "F":
                actual.append(1)
            else:
                actual.append(0)

    fp, tp, thresholds = roc_curve(actual, prediction)
    roc_auc = auc(fp, tp)
    plt.plot(fp, tp, label="p"+str(i)+"_Fraud AUC = %0.2f, Gini = %0.2f"%(roc_auc,roc_auc*2-1))
    actual.clear()
    prediction.clear()


plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.grid()
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

