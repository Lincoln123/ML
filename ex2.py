from pandas import read_csv

ifile = read_csv("выгрузка.csv", ",")

threshold = 0.5

p = []
thlist = []

def check (threshold,f):

    p.clear()
    fp, fn, tp, tn = 0, 0, 0, 0
    global ifile
    for ES in [ifile.p1_Fraud, ifile.p2_Fraud, ifile.p3_Fraud, ifile.p4_Fraud, ifile.p5_Fraud]:
        for chance, it in zip(ES, ifile.CLASS):
            if chance > threshold:
                if it == "F":
                    tp += 1
                else:
                    fn += 1
            else:
                if it != "F":
                    tn += 1
                else:
                    fp += 1

        p.append([tp/len(ifile), tn/len(ifile), fp/len(ifile), fn/len(ifile)])
        if threshold == 0.5 and f == 1:
            recall = tp / (tp + fn)
            precision = tp / (tp + fp)
            print("recall =", recall, "precision =", precision)
        else:
            continue

    return


if __name__ == "__main__":

    check(threshold, 1)

    i = 0
    while i != 5:
        a = p[i][2]
        if a > 0.201:
            if a >= 0.3:
                threshold -= 0.05
                check(round(threshold,3),0)
            else:
                threshold -= 0.01
                check(round(threshold,3),0)
        else:
            if a > 0.199:
                thlist.append(round(threshold,3))
                i += 1
            else:
                threshold += 0.001
                check(round(threshold,3),0)

    print("threshold =", thlist)





