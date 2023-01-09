import xlrd
import xlsxwriter
import pandas as pd
import argparse
import regex as re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="csv/tsv converter for kraken/bracken result")
    parser.add_argument("in_file_lst", help="Path of csv file,seperated by comma")
    parser.add_argument("out_file", help="Path of xlsx file")
    parser.add_argument("seperator", default="comma or tab",
                        help="seperator, STRING")
    args = parser.parse_args()

    COLS = ["Ratio of covered fragments", "Domain", "Kingdom", "Phylum", "Class", 
            "Order", "Family", "Genus ", "Number of covered fragments", 
            "Number of assigned fragment", "NCBI-taxID", "Scientific name"]
    in_lst = args.in_file_lst.split(",")
    writer = pd.ExcelWriter(args.out_file,
                            engine='xlsxwriter')
    for i in in_lst:
        df = pd.read_csv(i,sep=args.seperator,engine="python",names=COLS,index_col=None)
        df.to_excel(writer, sheet_name=i.replace("_bracken_species.finished.tsv",""), index=False)
    writer.close()
