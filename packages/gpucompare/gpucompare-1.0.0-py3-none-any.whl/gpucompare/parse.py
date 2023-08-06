"""Parse input data"""

import csv

from .compare import compare_gpus


def parse_csv(csv_path: str) -> str:
    """Print GPU name.

    Args:
        csv_path (str): path to CSV file containing row-wise GPU data

    Returns:
        str: dictionary as string containing performance comparison of GPUs

    Examples:
        .. code:: python

            >>> parse_csv("/path/to/gpu_data.csv")
                        "{'A10/A2': '3.0x', 'A30/A2': '4.67x'}"
    """
    # list containing dicts having gpus specs
    gpu_spec_list = []
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = []
        for i, row in enumerate(csv_reader):
            # set first row as header
            if i == 0:
                csv_header = row
            # append rest rows' data as dictionary in a list
            else:
                gpu_spec = {}
                for spec, col_val in zip(csv_header, row):
                    gpu_spec[spec] = col_val
                gpu_spec_list.append(gpu_spec)
    # compare gpus
    return compare_gpus(gpu_spec_list)
