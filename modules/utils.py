"""
    - List of variables for this application
    - Base functions
"""
import math
from statistics import mean, stdev

HEAD_DATAS_VALUE, HEAD_PROBE_REFERENCE_DATA_VALUE, HEAD_CALIBRATION_PXRF_DATA_VALUE = [], [], []
UNKNOWN_DATA, PROBE_REFERENCE_DATA, CALIBRATION_PXRF_DATA = {}, {}, {}
CORRECTION_FACTOR, CORRECTION_FACTOR_BY_SAMPLE, UNKNOWN_DATA_ELEMENTS = {}, {}, {}

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
# Error message
#
IMPORTED_ERROR_MSG_BOX_TITLE = 'Erreur import'
FILE_SELECT_ERROR_MSG_BOX_TITLE = 'Erreur import fichier'
ALREADY_FORMAT_ERROR_MSG_BOX_TITLE = 'Erreur formatage de données'
FILE_ALREADY_IMPORTED_ERROR_MSG_BOX_TITLE = 'Erreur Fichier déjà importé'
PROBE_OR_PXRF_NOT_FORMAT_ERROR_MSG_BOX_TITLE = 'Erreur facteur de correction'
LUNCH_START_VERIFY_ERROR_MSG_BOX_TITLE = 'Erreur rencontée lors du lancement'
#
ERROR_MESSAGE_FILE_IMPORTED = 'Ce type de donnee a déja ete importé.'
ERROR_MESSAGE_NOT_SELECT_TYPE_FILE_OR_CHOOSE_IMPORTED_FILE = 'Veuillez selectionner le type de donnee a importer puis importer le fichier correspondant.'
ERROR_MESSAGE_ALREADY_PROBE_FORMAT = 'Les données de reférence de microsonde ont déja été formatées.'
ERROR_MESSAGE_ALREADY_PXRF_FORMAT = 'Les données de calibration analysé au pXRF ont déja été formatées.'
ERROR_MESSAGE_FILE_ALREADY_IMPORTED = 'Le fichier choisi a déjà été importé précédement.'
ERROR_MESSAGE_PROBE_OR_PXRF_NOT_FORMAT = 'Vous devez tout d\'abord inclure le fichier des données de calcicité inconnue analysées au pXRF.\nPar la suite, vous devez formater les données de reférence (microsonde) ainsi que les données de calibration (pXRF) avant de pouvoir calculer le facteur de correction.'
ERROR_MESSAGE_LUNCH_START_VERIFY = 'Verifiez que toute la procédure a été respectée avant de lancer le l\'analyse'
#
# HEADER
#
CORRECTION_FACTOR_TOTAL = 'FACTEUR DE CORRECTION'
HEAD_CORRECTION_DATA_VALUE = ['Si', 'Al', 'Ca']
VERTICAL_ADDTIONNAL_HEAD_CORRECTION_DATA_VALUE = ['Moyenne', 'Écart-type', 'Écart-type Relatif']
HEAD_ANALYSIS_RESULT = ['Ca|Si', 'An Content Ca|Si', 'Ca|Al', 'An Content Ca|Al']
#
# Element And Total Limit for Sample Verification
#
TOTAL_LIMIT = 98.0
ELEMENT_P_LIMIT = 1.0
ELEMENT_K_LIMIT = 2.0

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
    'ag2o': 0.93101201,
    'al2o3': 0.52924054,
    'as2o3': 0.75740362,
    'as2o5': 0.651932981,
    'au2o': 0.960984048,
    'b2o3': 0.310539718,
    'bao': 0.895656068,
    'beo': 0.360256503,
    'bi2o5': 0.839348665,
    'co2': 0.272895972,
    'cao': 0.714694111,
    'cdo': 0.875426771,
    'ce2o3': 0.853752241,
    'ceo2': 0.814067079,
    'coo': 0.78647267,
    'cr2o3': 0.684228532,
    'cs2o': 0.943218261,
    'cuo': 0.798849656,
    'dy2o3': 0.871307833,
    'er2o3': 0.874508089,
    'eu2o3': 0.863632438,
    'feo': 0.777302759,
    'fe2o3': 0.699447437,
    'ga2o3': 0.743936914,
    'gd2o3': 0.867603679,
    'geo2': 0.694058856,
    'hfo2': 0.847960655,
    'hgo': 0.926097425,
    'ho2o3': 0.872981231,
    'in2o3': 0.827061451,
    'iro': 0.923190547,
    'k2o': 0.830151087,
    'la2o3': 0.8526603,
    'li2o': 0.464532912,
    'lu2o3': 0.879430129,
    'mgo': 0.603063563,
    'mno': 0.774473358,
    'mno2': 0.631911532,
    'moo3': 0.66653336,
    'n2o5': 0.259396643,
    'na2o': 0.741839763,
    'nb2o5': 0.699056274,
    'nd2o3': 0.85733882,
    'nio': 0.785854617,
    'oso': 0.922424131,
    'p2o5': 0.436376331,
    'pbo2': 0.928332714,
    'pbo': 0.866250866,
    'pdo': 0.869262865,
    'pr2o3': 0.854481757,
    'pr6o11': 0.827677537,
    'pto': 0.924214418,
    'rb2o': 0.914411119,
    'reo': 0.92089511,
    'rho': 0.642880103,
    'ruo': 0.863334197,
    'so3': 0.400448502,
    'sb2o5': 0.752785306,
    'sc2o3': 0.651975486,
    'seo3': 0.621929224,
    'sio2': 0.467464473,
    'sm2o3': 0.862366333,
    'sn02': 0.787649653,
    'sro': 0.845594453,
    'ta2o5': 0.818933748,
    'tb2o3': 0.868809731,
    'tb4o7': 0.850195545,
    'teo3': 0.72663857,
    'tho2': 0.878811846,
    'tio2': 0.599484443,
    'tl2o3': 0.89493467,
    'tm2o3': 0.875580072,
    'uo2': 0.881523272,
    'uo3': 0.832154448,
    'u3o8': 0.848032564,
    'v2o3': 0.679851249,
    'v5o5': 0.560161326,
    'wo3': 0.793021412,
    'y2o3': 0.78746358,
    'yb2o3': 0.878194432,
    'zno': 0.803341902,
    'zr2o5': 0.740302043
}

ELEMENTS = {
    'ag2o': 'ag',
    'al2o3': 'al',
    'as2o3': 'as',
    'as2o5': 'as',
    'au2o': 'au',
    'b2o3': 'b',
    'bao': 'ba',
    'beo': 'be',
    'bi2o5': 'bi',
    'co2': 'co',
    'cao': 'ca',
    'cdo': 'cd',
    'ce2o3': 'ce',
    'ceo2': 'ce',
    'coo': 'co',
    'cr2o3': 'cr',
    'cs2o': 'cs',
    'cuo': 'cu',
    'dy2o3': 'dy',
    'er2o3': 'er',
    'eu2o3': 'eu',
    'feo': 'fe',
    'fe2o3': 'fe',
    'ga2o3': 'ga',
    'gd2o3': 'gd',
    'geo2': 'ge',
    'hfo2': 'hf',
    'hgo': 'hg',
    'ho2o3': 'ho',
    'in2o3': 'in',
    'iro': 'ir',
    'k2o': 'k',
    'la2o3': 'la',
    'lu2o3': 'lu',
    'mgo': 'mg',
    'mno': 'mn',
    'mno2': 'mn',
    'moo3': 'mo',
    'n2o5': 'n',
    'na2o': 'na',
    'nb2o5': 'nb',
    'nd2o3': 'nd',
    'nio': 'ni',
    'oso': 'os',
    'p2o5': 'p2',
    'pbo2': 'pb',
    'pbo': 'pb',
    'pdo': 'pd',
    'pr2o3': 'pr',
    'pr6o11': 'pr',
    'pto': 'pt',
    'rb2o': 'rb',
    'reo': 're',
    'rho': 'ru',
    'ruo': '',
    'so3': 's',
    'sb2o5': 'sb',
    'sc2o3': 'sc',
    'seo3': 'se',
    'sio2': 'si',
    'sm2o3': 'sm',
    'sn02': 'sn',
    'sro': 'sr',
    'ta2o5': 'ta',
    'tb2o3': 'tb',
    'tb4o7': 'tb',
    'teo3': 'te',
    'tho2': 'th',
    'tio2': 'ti',
    'tl2o3': 'tl',
    'tm2o3': 'tm',
    'uo2': 'u',
    'uo3': 'u',
    'u3o8': 'u',
    'v2o3': 'v',
    'v5o5': 'v',
    'wo3': 'w',
    'y2o3': 'y',
    'yb2o3': 'yb',
    'zno': 'zn',
    'zr2o5': 'zr'
}

TYPE_FILE_IMPORTED = {
    'Microsonde - Données de reférence': 1,
    'Analyses pXRF - Données de calibration': 2,
    'Analyses pXRF - Données inconnues': 3
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
    Extract Si, Ca, Al value for each sample and create a dictionary
    :param data: dictionary of all dataset
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


def correction_factor_params(params):
    """
    ...
    :param params:
    :return:
    """
    si_values, al_values, ca_values = [], [], []
    for sample_name in CORRECTION_FACTOR_BY_SAMPLE:
        CORRECTION_FACTOR_BY_SAMPLE[sample_name][params] = {}
        for analysis_id in CORRECTION_FACTOR_BY_SAMPLE[sample_name]:
            if not str(analysis_id).isdigit():
                continue
            else:
                si_values.append(CORRECTION_FACTOR_BY_SAMPLE[sample_name][analysis_id][TEXT_ELEMENT_SI])
                al_values.append(CORRECTION_FACTOR_BY_SAMPLE[sample_name][analysis_id][TEXT_ELEMENT_AL])
                ca_values.append(CORRECTION_FACTOR_BY_SAMPLE[sample_name][analysis_id][TEXT_ELEMENT_CA])

        if params == TEXT_AVERAGE:
            CORRECTION_FACTOR_BY_SAMPLE[sample_name][params][TEXT_ELEMENT_SI] = mean(si_values)
            CORRECTION_FACTOR_BY_SAMPLE[sample_name][params][TEXT_ELEMENT_AL] = mean(al_values)
            CORRECTION_FACTOR_BY_SAMPLE[sample_name][params][TEXT_ELEMENT_CA] = mean(ca_values)
        elif params == TEXT_STD_DEVIATION:
            CORRECTION_FACTOR_BY_SAMPLE[sample_name][params][TEXT_ELEMENT_SI] = stdev(si_values)
            CORRECTION_FACTOR_BY_SAMPLE[sample_name][params][TEXT_ELEMENT_AL] = stdev(al_values)
            CORRECTION_FACTOR_BY_SAMPLE[sample_name][params][TEXT_ELEMENT_CA] = stdev(ca_values)


def relative_std_deviation():
    for sample in CORRECTION_FACTOR_BY_SAMPLE:
        CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_RELATIVE_STD_DEVIATION] = {}
        for analysis_id in CORRECTION_FACTOR_BY_SAMPLE[sample]:
            if not str(analysis_id).isdigit():
                continue
            else:
                CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_RELATIVE_STD_DEVIATION][TEXT_ELEMENT_SI] = (CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_STD_DEVIATION][TEXT_ELEMENT_SI] / CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_AVERAGE][TEXT_ELEMENT_SI]) * 100
                CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_RELATIVE_STD_DEVIATION][TEXT_ELEMENT_AL] = (CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_STD_DEVIATION][TEXT_ELEMENT_AL] / CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_AVERAGE][TEXT_ELEMENT_AL]) * 100
                CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_RELATIVE_STD_DEVIATION][TEXT_ELEMENT_CA] = (CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_STD_DEVIATION][TEXT_ELEMENT_CA] / CORRECTION_FACTOR_BY_SAMPLE[sample][TEXT_AVERAGE][TEXT_ELEMENT_CA]) * 100


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
