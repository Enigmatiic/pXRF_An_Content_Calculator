"""
    - List of variables for this application
    - Base functions
"""
import math

HEAD_VALUE = []
DATAS = {}
ELEMENT_RATIO_DATA = {}

#
# Text
#
ELEMENT_SI = 'si'
ELEMENT_AL = 'al'
ELEMENT_CA = 'ca'
ELEMENT_P = 'p'
ELEMENT_K = 'k'

RATIO_SI = 'Ca|Si'
RATIO_AL = 'Ca|Al'

AN_CONTENT_RATIO_SI = 'An Content Ca|Si'
AN_CONTENT_RATIO_AL = 'An Content Ca|Al'

#
# Element And Total Limit for Sample Verification
#
TOTAL_LIMIT = 98.5
ELEMENT_P_LIMIT = 0.5
ELEMENT_K_LIMIT = 2

#
# Formulas Coef for An Content Calcul From Ratio
#
COEF_SI_RATIO_A = -0.0038
COEF_SI_RATIO_B = (1.2592 * math.pow(10. - 5))
COEF_SI_RATIO_C = (1.2 * math.pow(10. - 4))
COEF_SI_RATIO_D = (2 * (3 * math.pow(10. - 5)))


COEF_AL_RATIO_A = -0.0107
COEF_AL_RATIO_B = (1.21706 * math.pow(10. - 4))
COEF_AL_RATIO_C = (1.6 * math.pow(10. - 4))
COEF_AL_RATIO_D = (2 * (-4 * math.pow(10. - 5)))

#
# Convertions Factors Oxyd To Element
#
CORRECTION_FACTORS = {
    'Ag2O': 0.93101201,
    'Al2O3': 0.52924054,
    'As2O3': 0.75740362,
    'As2O5': 0.651932981,
    'Au2O': 0.960984048,
    'B2O3': 0.310539718,
    'BaO': 0.895656068,
    'BeO': 0.360256503,
    'Bi2O5': 0.839348665,
    'CO2': 0.272895972,
    'CaO': 0.714694111,
    'CdO': 0.875426771,
    'Ce2O3': 0.853752241,
    'CeO2': 0.814067079,
    'CoO': 0.78647267,
    'Cr2O3': 0.684228532,
    'Cs2O': 0.943218261,
    'CuO': 0.798849656,
    'Dy2O3': 0.871307833,
    'Er2O3': 0.874508089,
    'Eu2O3': 0.863632438,
    'FeO': 0.777302759,
    'Fe2O3': 0.699447437,
    'Ga2O3': 0.743936914,
    'Gd2O3': 0.867603679,
    'GeO2': 0.694058856,
    'HfO2': 0.847960655,
    'HgO': 0.926097425,
    'Ho2O3': 0.872981231,
    'In2O3': 0.827061451,
    'IrO': 0.923190547,
    'K2O': 0.830151087,
    'La2O3': 0.8526603,
    'Li2O': 0.464532912,
    'Lu2O3': 0.879430129,
    'MgO': 0.603063563,
    'MnO': 0.774473358,
    'MnO2': 0.631911532,
    'MoO3': 0.66653336,
    'N2O5': 0.259396643,
    'Na2O': 0.741839763,
    'Nb2O5': 0.699056274,
    'Nd2O3': 0.85733882,
    'NiO': 0.785854617,
    'OsO': 0.922424131,
    'P2O5': 0.436376331,
    'PbO': 0.928332714,
    'PbO2': 0.866250866,
    'PdO': 0.869262865,
    'Pr2O3': 0.854481757,
    'Pr6O11': 0.827677537,
    'PtO': 0.924214418,
    'Rb2O': 0.914411119,
    'ReO': 0.92089511,
    'RhO': 0.642880103,
    'RuO': 0.863334197,
    'SO3': 0.400448502,
    'Sb2O5': 0.752785306,
    'Sc2O3': 0.651975486,
    'SeO3': 0.621929224,
    'SiO2': 0.467464473,
    'Sm2O3': 0.862366333,
    'SnO2': 0.787649653,
    'SrO': 0.845594453,
    'Ta2O5': 0.818933748,
    'Tb2O3': 0.868809731,
    'Tb4O7': 0.850195545,
    'TeO3': 0.72663857,
    'ThO2': 0.878811846,
    'TiO2': 0.599484443,
    'Tl2O3': 0.89493467,
    'Tm2O3': 0.875580072,
    'UO2': 0.881523272,
    'UO3': 0.832154448,
    'U3O8': 0.848032564,
    'V2O3': 0.679851249,
    'V2O5': 0.560161326,
    'WO3': 0.793021412,
    'Y2O3': 0.78746358,
    'Yb2O3': 0.878194432,
    'ZnO': 0.803341902,
    'ZrO2': 0.740302043
}

#
# Utils Functions
#
def remove_sample(sample_key, data):
    if len(data) != 0:
        data.pop(sample_key)
    else:
        print('Aucune données disponible')
