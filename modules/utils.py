"""
    - List of variables for this application
    - Base functions
"""
import math
from statistics import mean, stdev

HEAD_VALUE = []
DATAS = {}
ELEMENT_RATIO_DATA = {}

#
# Text
#
TEXT_ELEMENT_SI = 'si'
TEXT_ELEMENT_AL = 'al'
TEXT_ELEMENT_CA = 'ca'
TEXT_ELEMENT_P = 'p'
TEXT_ELEMENT_K = 'k'

TEXT_AVERAGE = 'average'
TEXT_STD_DEVIATION = 'std_deviation'
TEXT_RELATIVE_STD_DEVIATION = 'relative_std_deviation'

TEXT_RATIO_SI = 'Ca|Si'
TEXT_RATIO_AL = 'Ca|Al'

TEXT_AN_CONTENT_RATIO_SI = 'An Content Ca|Si'
TEXT_AN_CONTENT_RATIO_AL = 'An Content Ca|Al'
TEXT_CALIBRATION_AN_CONTENT = 'An Content'

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
COEF_SI_RATIO_B = (1.2592 * math.pow(10, -5))
COEF_SI_RATIO_C = (1.2 * math.pow(10, -4))
COEF_SI_RATIO_D = (2 * (3 * math.pow(10, -5)))

COEF_AL_RATIO_A = -0.0107
COEF_AL_RATIO_B = (1.21706 * math.pow(10, -4))
COEF_AL_RATIO_C = (1.6 * math.pow(10, -4))
COEF_AL_RATIO_D = (2 * (-4 * math.pow(10, -5)))

#
# Convertions Factors Oxyd To Element
#
CORRECTION_FACTORS = {
    'ag': 0.93101201,
    'al': 0.52924054,
    'as3': 0.75740362,
    'as5': 0.651932981,
    'au': 0.960984048,
    'b': 0.310539718,
    'ba': 0.895656068,
    'be': 0.360256503,
    'bi': 0.839348665,
    'c': 0.272895972,
    'ca': 0.714694111,
    'cd': 0.875426771,
    'ce2': 0.853752241,
    'ce': 0.814067079,
    'co': 0.78647267,
    'cr': 0.684228532,
    'cs': 0.943218261,
    'cu': 0.798849656,
    'dy': 0.871307833,
    'er': 0.874508089,
    'eu': 0.863632438,
    'fe': 0.777302759,
    'fe2': 0.699447437,
    'ga': 0.743936914,
    'gd': 0.867603679,
    'ge': 0.694058856,
    'hf': 0.847960655,
    'hg': 0.926097425,
    'ho': 0.872981231,
    'in': 0.827061451,
    'ir': 0.923190547,
    'k': 0.830151087,
    'la': 0.8526603,
    'li': 0.464532912,
    'lu': 0.879430129,
    'mg': 0.603063563,
    'mn': 0.774473358,
    'mn2': 0.631911532,
    'mo': 0.66653336,
    'n': 0.259396643,
    'na': 0.741839763,
    'nb': 0.699056274,
    'nd': 0.85733882,
    'ni': 0.785854617,
    'os': 0.922424131,
    'p': 0.436376331,
    'pb': 0.928332714,
    'pb2': 0.866250866,
    'pd': 0.869262865,
    'pr2': 0.854481757,
    'pr6': 0.827677537,
    'pt': 0.924214418,
    'rb': 0.914411119,
    're': 0.92089511,
    'rh': 0.642880103,
    'ru': 0.863334197,
    's': 0.400448502,
    'sb': 0.752785306,
    'sc': 0.651975486,
    'se': 0.621929224,
    'si': 0.467464473,
    'sm': 0.862366333,
    'sn': 0.787649653,
    'sr': 0.845594453,
    'ta': 0.818933748,
    'tb': 0.868809731,
    'tb4': 0.850195545,
    'te': 0.72663857,
    'th': 0.878811846,
    'ti': 0.599484443,
    'tl': 0.89493467,
    'tm': 0.875580072,
    'u': 0.881523272,
    'u1': 0.832154448,
    'u3': 0.848032564,
    'v3': 0.679851249,
    'v5': 0.560161326,
    'w': 0.793021412,
    'y': 0.78746358,
    'yb': 0.878194432,
    'zn': 0.803341902,
    'zr': 0.740302043
}


#
# Utils Functions
#
def remove_sample(sample_key, data):
    """
    ...
    :param sample_key:
    :param data:
    :return:
    """
    if len(data) != 0:
        data.pop(sample_key)
    else:
        print('Aucune données disponible')


def extract_elements(data):
    """
    Extract Si, Ca, Al value for each sample and create a dictionnary
    :param data: dictionnary of all dataset
    """
    extracted_elements = {}
    for sample in data:
        extracted_elements[sample] = {}
        for element in data[sample]:
            if element == TEXT_ELEMENT_SI or element == TEXT_ELEMENT_AL or element == TEXT_ELEMENT_CA:
                extracted_elements[sample][element] = data[sample][element]
    return extracted_elements


def calibration_sample_frequencies(dataset):
    """
    ...
    :param dataset:
    :return:
    """
    frequencies = {}
    for sample in dataset:
        frequencies[sample] = 0
        for _sample in dataset:
            if sample == _sample:
                frequencies[sample] += 1
    return frequencies


def correction_factor_params(dataset, params):
    """
    ...
    :param dataset:
    :param params:
    :return:
    """
    si_values, al_values, ca_values = [], [], []
    for sample_name in dataset:
        dataset[sample_name][params] = {}
        for analysis_id in dataset[sample_name]:
            if not analysis_id.isdigit():
                continue
            else:
                si_values.append(dataset[sample_name][analysis_id][TEXT_ELEMENT_SI])
                al_values.append(dataset[sample_name][analysis_id][TEXT_ELEMENT_AL])
                ca_values.append(dataset[sample_name][analysis_id][TEXT_ELEMENT_CA])

        if params == TEXT_AVERAGE:
            dataset[sample_name][params][TEXT_ELEMENT_SI] = mean(si_values)
            dataset[sample_name][params][TEXT_ELEMENT_AL] = mean(al_values)
            dataset[sample_name][params][TEXT_ELEMENT_CA] = mean(ca_values)
        elif params == TEXT_STD_DEVIATION:
            dataset[sample_name][params][TEXT_ELEMENT_SI] = stdev(si_values)
            dataset[sample_name][params][TEXT_ELEMENT_AL] = stdev(al_values)
            dataset[sample_name][params][TEXT_ELEMENT_CA] = stdev(ca_values)


pre_correction_fact = {
    'MG-BCP-1A': {
        1: {
            'si': 1.104,
            'al': 1.479,
            'ca': 1.241
        },
        2: {
            'si': 1.104,
            'al': 1.479,
            'ca': 1.241
        },
        3: {
            'si': 1.104,
            'al': 1.479,
            'ca': 1.241
        },
        'average': {
            'si': 1.095,
            'al': 1.458,
            'ca': 1.242
        },
        'std_deviation': {
            'si': 0.007,
            'al': 0.023,
            'ca': 0.002
        },
        'relative_std_deviation': {
            'si': 0.64,
            'al': 1.57,
            'ca': 0.16
        }
    }
}
