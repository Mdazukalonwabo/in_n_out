import csv
import argparse
from datetime import datetime


class CsvCreator(object):
    def __init__(self):
        self.data = []

    def read_csv_file(self, input_file):
        with open(input_file, 'r') as current_file:
            extracting_information = csv.reader(current_file)
            for line in extracting_information:
                self.data.append(line)
            return self.data

    def parse_in_content(self, data):
        today_date = datetime.now()
        today_date_formatted = today_date.strftime("%d/%m/%Y %H:%M:%S")
        data[0].append(" Parsed")
        for i in range(1, len(data)):
            data[i].append(today_date_formatted)
        return data

    def write_to_csv(self, output_file):
        with open(output_file, 'w') as new_file:
            adding_to_file = csv.writer(new_file)
            parsed_data = self.parse_in_content(self.data)
            for line in parsed_data:
                adding_to_file.writerow(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Read csv file and store values")
    parser.add_argument("-i", "--input_csv", type=str, help="Enter input csv dir")
    parser.add_argument("-o", "--output_csv", type=str, help="Enter output csv dir")
    args = parser.parse_args()
    run_csv = CsvCreator()
    run_csv.read_csv_file(args.input_csv)
    run_csv.write_to_csv(args.output_csv)
