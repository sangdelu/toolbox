import xlrd
import xlsxwriter
import pandas as pd
import argparse
import regex as re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="csv/tsv converter")
    parser.add_argument("in_file_lst", help="Path of csv file,seperated by comma")
    parser.add_argument("out_file", help="Path of xlsx file")
    parser.add_argument("seperator", default="comma or tab",
                        help="seperator, STRING")
    args = parser.parse_args()

    in_lst = args.in_file_lst.split(",")
    writer = pd.ExcelWriter(args.out_file,
                            engine='xlsxwriter')
    for i in in_lst:
        df = pd.read_csv(i,header=None)
        df1 = df[0].str.split("\t",expand=True)
        df1.to_excel(writer, sheet_name=i.replace(".tsv",""), index=False,header=False)
    writer.close()
