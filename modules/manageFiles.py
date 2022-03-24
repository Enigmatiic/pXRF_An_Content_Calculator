"""
Module for xls file manager
"""
from openpyxl import load_workbook, Workbook


class manageFile():
    def __init__(self):
        """Init class"""
        super(manageFile, self).__init__()

    def open_xlsx_file_(self, file_path):
        """
        Open xlsx file
        :param file_path: Location address of the xlsx file
        :return: workbook and first sheetname who contain all datas
        """
        # Address of the file on the local computer, i.e, path location
        loc_file = (str(file_path))
        # To open Workbook we declare a hadling variable wb+
        wbook = load_workbook(loc_file)
        wsheet = wbook.sheetnames
        # Extract all values
        return wbook, wsheet[0]

    def compile_xlsx_to_dict(self, workbook, sheetname):
        """
        Compile file into a dictionnary
        :param workbook: xlsx workbook file
        :param sheetname: active sheetname of xlsx workbook file
        :return: First line of workbook and  a dictionnary who contain all values
        """
        data_head = []
        datas = {}
        # Take first line like table Head
        for row in workbook[sheetname].values:
            for value in row:
                data_head.append(value.lower())
            break

        # Compile values in a dictionnary
        i = 0
        for row in workbook[sheetname].values:
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
                if value == '< LOD':  # Replace non-analyse element by 0
                    datas[str(row[0])][data_head[j]] = 0
                else:
                    datas[str(row[0])][data_head[j]] = value
                j += 1

        return data_head, datas

    def create_xlsx_file(self):
        pass


mf = manageFile()

workbook, sheetfile = mf.open_xlsx_file_('../data/JTSS_PRCS.xlsx')

head_value, datas = mf.compile_xlsx_to_dict(workbook, sheetfile)

