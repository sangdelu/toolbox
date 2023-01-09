import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="orgnize kreport (kraken2) result")
    parser.add_argument("kreport")
    args = parser.parse_args()

    with open(args.kreport, 'r') as in_handle, \
            open(args.kreport + '.processed', 'w') as out_handle:
        header = ['D', 'P', 'C', 'O', 'F', 'G']
        for line in in_handle.readlines():
            label = line[:-1].split("\t")[3]
            tage = line[:-1].split("\t")[-1]
            if label == "D":
                header = ['D', 'P', 'C', 'O', 'F', 'G']
                header[0] = tage.replace(" ", "")
            if label == "P":
                header[1] = tage.replace(" ", "")
            if label == "C":
                header[2] = tage.replace(" ", "")
            if label == "O":
                header[3] = tage.replace(" ", "")
            if label == "F":
                header[4] = tage.replace(" ", "")
            if label == "G":
                header[5] = tage.replace(" ", "")
            else:
                out_handle.write("\t".join(header) + "\t" + line)
