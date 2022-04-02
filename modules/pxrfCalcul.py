"""
Module for pXRF Calculation
"""
import modules.utils as utils
import math


class PxrfCalcul:

    def __init__(self):
        super(PxrfCalcul, self).__init__()

    @staticmethod
    def is_plag(sample_data):
        """
        Verify if data for sample given is plagioclase
        :param sample_data: element values for sample
        :return: True or False
        """
        element_k_verif, element_p_verif, total_verif = False, False, False
        total = 0
        for element in sample_data:
            total += sample_data[element]

        if total > utils.TOTAL_LIMIT:
            total_verif = True
            for element in sample_data:
                if element == utils.TEXT_ELEMENT_K:
                    if sample_data[element] < utils.ELEMENT_K_LIMIT:
                        element_k_verif = True
                if element == utils.TEXT_ELEMENT_P:
                    if sample_data[element] < utils.ELEMENT_P_LIMIT:
                        element_p_verif = True

        if total_verif and element_p_verif and element_k_verif:
            return True
        elif total_verif and not element_k_verif:
            if element_p_verif:
                return True
            else:
                return False
        else:
            return False

    def format_data(self, data):
        data_values = data
        sample_to_remove = []
        removed_sample_data = {}
        # Verify if sample has correct data to be a plagioclase else he will be removed
        for sample in data_values:
            if not self.is_plag(data_values[sample]):
                removed_sample_data[sample] = data_values[sample]
                sample_to_remove.append(sample)
        # Remove sample
        for sample in sample_to_remove:
            utils.remove_sample(sample, data_values)
        return data_values

    def calcul_ratios(self, data):
        """
        Calcul Si ans Al ratio for all dataset
        :param data: dataset formatted
        :return:
        """
        data_ratio = {}
        for sample in data:
            data_ratio[str(sample)] = {}
            data_ratio[str(sample)][utils.TEXT_RATIO_SI] = self.calcul_si_ratio(data[sample])
            data_ratio[str(sample)][utils.TEXT_RATIO_AL] = self.calcul_al_ratio(data[sample])

        return data_ratio

    @staticmethod
    def calcul_si_ratio(sample_data):
        """
        Calcul ratio [Ca/Si]
        :param sample_data: sample element value {Si, Al, Ca}
        :return: ratio in float value
        """
        return sample_data[utils.TEXT_ELEMENT_CA] / sample_data[utils.TEXT_ELEMENT_SI]

    @staticmethod
    def calcul_al_ratio(sample_data):
        """
        Calcul ratio [Ca/Al]
        :param sample_data: sample element value {Si, Al, Ca}
        :return: ratio in float value
        """
        return sample_data[utils.TEXT_ELEMENT_CA] / sample_data[utils.TEXT_ELEMENT_AL]

    def calcul_an_content(self, data):
        """
        Calcul An Content for all dataset
        :param data: dataset formatted
        :return:
        """
        data_an_content = {}
        for sample in data:
            data_an_content[str(sample)] = {}
            data_an_content[str(sample)][utils.TEXT_AN_CONTENT_RATIO_SI] = self.calcul_an_content_from_si_ratio(data[sample][utils.TEXT_RATIO_SI])
            data_an_content[str(sample)][utils.TEXT_AN_CONTENT_RATIO_AL] = self.calcul_an_content_from_al_ratio(data[sample][utils.TEXT_RATIO_AL])

        return data_an_content

    @staticmethod
    def calcul_an_content_from_si_ratio(si_ratio):
        """
        Calcul An Content from ratio (Si/Ca)
        :param si_ratio:
        :return:
        """
        return (utils.COEF_SI_RATIO_A + math.sqrt(utils.COEF_SI_RATIO_B + utils.COEF_SI_RATIO_C * si_ratio)) / utils.COEF_SI_RATIO_D

    @staticmethod
    def calcul_an_content_from_al_ratio(al_ratio):
        """
        Calcul An Content from ratio (Si/Ca)
        :param al_ratio:
        :return:
        """
        if utils.COEF_AL_RATIO_B - (utils.COEF_AL_RATIO_C * al_ratio) < 0:
            return 0
        else:
            return (utils.COEF_AL_RATIO_A + math.sqrt(utils.COEF_AL_RATIO_B - utils.COEF_AL_RATIO_C * al_ratio)) / utils.COEF_AL_RATIO_D


    @staticmethod
    def correct_data(dataset):
        corrected_data = {}
        for sample in dataset:
            corrected_data[sample] = {}
            corrected_data[sample][utils.TEXT_ELEMENT_SI] = dataset[sample][utils.TEXT_ELEMENT_SI] * utils.CORRECTION_FACTOR[utils.TEXT_ELEMENT_SI]
            corrected_data[sample][utils.TEXT_ELEMENT_AL] = dataset[sample][utils.TEXT_ELEMENT_AL] * utils.CORRECTION_FACTOR[utils.TEXT_ELEMENT_AL]
            corrected_data[sample][utils.TEXT_ELEMENT_CA] = dataset[sample][utils.TEXT_ELEMENT_CA] * utils.CORRECTION_FACTOR[utils.TEXT_ELEMENT_CA]

        return corrected_data
