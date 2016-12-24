# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:50:03 2016

@author: Евгений
"""
import csv
import os
from collections import OrderedDict

import pandas as pd

from .folders import ParsedCSV
from .common import pipe, print_elapsed_time
from .inspect_columns import Columns
from .remote import RawDataset
from .row_parser import parse_row, get_parsed_colnames, get_colname_dtypes

COLUMNS = Columns.COLUMNS
RAW_CSV_FORMAT = dict(enc='windows-1251', sep=";")

#
# file location wrappers
#

def get_parsed_csv_path(year):
    return ParsedCSV(year).filepath()


def get_raw_csv_path(year):
    return RawDataset(year).get_filename()

#
# column names wrappers
#

def emit_raw_colnames():
    """Column names corresponding to emit_raw_rows()."""
    return ['year'] + COLUMNS


def emit_parsed_colnames():
    return get_parsed_colnames()

#
# row validation
#

VALID_ROW_WIDTH = len(COLUMNS)
INN_POSITION = COLUMNS.index('inn')

def is_valid(row):
    """Return True if row is valid."""
    if len(row) != VALID_ROW_WIDTH:
        # todo: may use Logger
        # reason = "Invalid row length {}".format(str(len(row)))
        return False
    elif not row[INN_POSITION]:
        # reason = "Skipped row with empty INN field"
        return False
    else:
        return True



#
# read, filter and parse raw csv
#

def csv_stream(filename, enc='utf-8', sep=','):
    """Emit CSV rows by filename."""
    if enc not in ['utf-8', 'windows-1251']:
        raise ValueError("Encoding not supported: " + str(enc))
    with open(filename, 'r', encoding=enc) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=sep)
        for row in spamreader:
            yield row


def emit_raw_rows(year):
    """Emit raw rows by year."""
    fn = get_raw_csv_path(year)
    raws = filter(is_valid, csv_stream(fn, **RAW_CSV_FORMAT))
    add_year = lambda row: [year] + row
    return map(add_year, raws)


def emit_raw_dicts(year):
    columns = emit_raw_colnames()
    as_dict = lambda row: OrderedDict(zip(columns, row))
    return map(as_dict, emit_raw_rows(year))


def emit_rows(year):
    gen = emit_raw_dicts(year)
    return map(parse_row, gen)


def emit_dicts(year):
    columns = emit_parsed_colnames()
    # lambda func allow to make inline fucntion with one arguement
    as_dict = lambda row: OrderedDict(zip(columns, row))
    return map(as_dict, emit_rows(year))


#
# output to csv file, read dataframe functions
#
@print_elapsed_time
def to_csv(path, stream, cols=None):
    with open(path, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\n",
                            quoting=csv.QUOTE_MINIMAL)
        if cols:
            writer.writerow(cols)
        writer.writerows(stream)
    print("Saved file:", path)
    return path


def custom_df_reader(file):
    """Read dataset as pandas dataframe using dtypes for faster import."""
    if os.path.exists(file):
        print("Reading file:", file)
        # dtype on all columns shortens reading time
        return pd.read_csv(file, dtype=get_colname_dtypes())
    else:
        raise FileNotFoundError(file)


#
# end user class for dataset access
#

class Dataset():

    def __init__(self, year):
        self.year = year
        self.output_csv = get_parsed_csv_path(year)

    def __colnames__(self):
        return get_parsed_colnames()

    def __get_stream__(self):
        return pipe(emit_rows(self.year))

    def to_csv(self, force=False):
        if not os.path.exists(self.output_csv) or force is True:
            msg = "\nSaving %s dataset..." % self.year
            print(msg)
            to_csv(path=self.output_csv,
                   stream=self.__get_stream__(),
                   cols=self.__colnames__())
        else:
            print('{} dataset'.format(self.year),
                  'already saved as:', self.output_csv, "\n")

    @print_elapsed_time
    def read_df(self):
        print("Reading {} dataframe...".format(self.year))
        return custom_df_reader(self.output_csv)

if __name__ == "__main__":
    Dataset(2015).to_csv()
    z = next(emit_raw_rows(2015))