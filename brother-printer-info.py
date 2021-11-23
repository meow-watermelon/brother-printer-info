#!/usr/bin/env python3

import argparse
import csv
import io
import requests
import sys

if __name__ == '__main__':
    # set up initial variables
    printer_info_fields = None
    printer_info_data = None
    printer_info = {}

    # set up command arguments
    parser = argparse.ArgumentParser(description='Brother Printer Information Collector')
    parser.add_argument('--printer', type=str, required=True, help='Printer IP or Hostname')
    args = parser.parse_args()

    resp = requests.get('http://%s/etc/mnt_info.csv' %(args.printer))

    if resp.status_code == 200:
        with io.StringIO(resp.text, newline='') as resp_stream:
            csv_data = csv.reader(resp_stream)

            for index, item in enumerate(csv_data):
                if index == 0:
                    printer_info_fields = item
                else:
                    printer_info_data = item

        # remove the last empty record
        if printer_info_fields[-1] == "" and printer_info_data[-1] == "":
            printer_info_fields.pop(-1)
            printer_info_data.pop(-1)

        printer_info = dict(zip(printer_info_fields, printer_info_data))

        for k,v in printer_info.items():
            print('%s: %s' %(k, v))
    else:
        print('ERROR: Failed to acquire printer %s maintenance information: RC: %d - %s' %(args.printer, resp.status_code, resp.reason))
        sys.exit(2)
