import os
import csv
import pandas as pd


def find_data_row(csv_file_path):
    with open(csv_file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Iterate through rows
        for index, row in enumerate(csv_reader):
            # Check if [DATA] is in the row
            if '[DATA]' in row:
                return index  # Return the index of the row containing [DATA]

    # If [DATA] is not found, return -1
    return -1


def read_csv_from_index(csv_file_path, start_index, clm_name):
    df = pd.read_csv(csv_file_path, skiprows=start_index+1, delimiter=';',names=clm_name)
    return df


def load_single_file(csv_file_path,clm_name):
    start_index = find_data_row(csv_file_path)
    df = read_csv_from_index(csv_file_path, start_index, clm_name)
    return df


def get_all_files_with_extension(directory, extension):
    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(os.path.join(directory, file))
    return files


