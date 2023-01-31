import pickle
import os

tablo = open("tablo.tex", "w+")
tablo.write("model & accuracy & f1 score\\\\ \n \\hline \n")

for file in os.listdir() :
    if "report" not in file or ".py" in file :
        continue
    with open(file, "rb") as f :
        report = pickle.load(f)
    line = file.replace("report_", "").replace(".pickle", "") + " & " + str(report["accuracy"])[:6] + " & " + str(report["macro avg"]["f1-score"])[:6] + "\\\\ \n \\hline \n"
    tablo.write(line)

tablo.close()