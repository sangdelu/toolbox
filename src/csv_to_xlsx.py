import xlrd
import xlsxwriter
import pandas as pd
import argparse
import regex as re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="csv/tsv converter")
    parser.add_argument("in_file", help="Path of csv file")
    parser.add_argument("seperator", default="comma or tab",
                        help="seperator, STRING")
    args = parser.parse_args()

    df = pd.read_csv(args.in_file,sep=args.seperator,engine="python")
    writer = pd.ExcelWriter(re.sub(r"\.\w+", ".xlsx", args.in_file),
                            engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1', index=False, freeze_panes=(0, 1))
    writer.close()
