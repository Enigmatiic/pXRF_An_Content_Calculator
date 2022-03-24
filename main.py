from modules.manageFiles import manageFile
from modules.pxrfCalcul import pxrfCalcul
from modules.utils import *


if __name__ == '__main__':
    mf = manageFile()
    workbook, sheetfile = mf.open_xlsx_file_('data/JTSS_PRCS.xlsx')
    HEAD_VALUE, DATAS = mf.compile_xlsx_to_dict(workbook, sheetfile)

    pxrf = pxrfCalcul()

    DATAS = pxrf.format_data(DATAS)

    ELEMENT_RATIO_DATA = pxrf.extract_elements(DATAS)

    print(ELEMENT_RATIO_DATA)

    ratios = pxrf.calcul_ratios(ELEMENT_RATIO_DATA)

    #print(pxrf.calcul_an_content(ratios))