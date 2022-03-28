from modules.manageFiles import ManageFile
from modules.pxrfCalcul import PxrfCalcul
from modules.utils import *

if __name__ == '__main__':
    mf = ManageFile()
    pxrf = PxrfCalcul()

    workbook, file = mf.open_xlsx_file_('data/JTSS_PRCS.xlsx')
    HEAD_VALUE, DATAS = mf.compile_xlsx_to_dict(workbook, file)
    #print(DATAS)

    DATAS = pxrf.format_data(DATAS)

    ELEMENT_RATIO_DATA = extract_elements(DATAS)

    ratios = pxrf.calcul_ratios(ELEMENT_RATIO_DATA)

    print(ratios)

    print(pxrf.calcul_an_content(ratios))
