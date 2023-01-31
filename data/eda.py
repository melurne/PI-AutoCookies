import os

outputfile = open("eda.txt", "w+")

for file in os.listdir("dataset_raw") :
    with open("dataset_raw/" + file, 'r') as f:
        for l in f.readlines() :
            outputfile.write(file + "\t" + l)

outputfile.close()