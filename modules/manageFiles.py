"""
Module for xls file manager
"""
from openpyxl import load_workbook, Workbook


class ManageFile:
    def __init__(self):
        """Init class"""
        super(ManageFile, self).__init__()

    @staticmethod
    def open_xlsx_file_(file_path):
        """
        Open xlsx file
        :param file_path: Location address of the xlsx file
        :return: workbook and first sheet name who contain all datas
        """
        # Address of the file on the local computer, i.e, path location
        loc_file = (str(file_path))
        # To open Workbook we declare a handling variable wb+
        w_book = load_workbook(loc_file)
        w_sheet = w_book.sheetnames
        # Extract all values
        return w_book, w_sheet[0]

    @staticmethod
    def compile_xlsx_to_dict(workbook, sheet_name):
        """
        Compile file into a dictionary
        :param sheet_name: active sheet_name of xlsx workbook file
        :param workbook: xlsx workbook file
        :return: First line of workbook and  a dictionary who contain all values
        """
        data_head = []
        datas = {}
        # Take first line like table Head
        for row in workbook[sheet_name].values:
            for value in row:
                data_head.append(value.lower())
            break

        # Compile values in a dictionary
        i = 0
        for row in workbook[sheet_name].values:
            if i == 0:  # Skip first line
                i += 1
                continue
            i += 1
            j = 0
            datas[str(row[0])] = {}  # Create dict for sample key
            for value in row:
                if j == 0:  # Skip first value line
                    j += 1
                    continue
                if type(value).__name__ == 'str':  # Replace non-analyse element by 0
                    datas[str(row[0])][data_head[j]] = 0
                else:
                    datas[str(row[0])][data_head[j]] = value
                j += 1

        return data_head, datas

    def create_xlsx_file(self):
        pass
