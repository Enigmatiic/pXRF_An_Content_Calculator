"""

"""
import modules.utils as utils


class Calibration:
    def __init__(self):
        super(Calibration, self).__init__()

    def verify_data(self):
        """
        ...
        :return:
        """
        pass

    def format_data(self, data):
        """
        ...
        :param data:
        :return:
        """
        pass

    @staticmethod
    def convert_oxyd_to_element(calibration_data):
        """
        ...
        :param calibration_data:
        :return:
        """
        calibration_chemical_element = {}
        non_convertible_oxyde = {}
        for sample in calibration_data:
            calibration_chemical_element[sample] = {}
            for oxyde in calibration_data[sample]:
                if oxyde == utils.TEXT_CALIBRATION_AN_CONTENT:
                    continue
                element = oxyde[:1].lower()
                if element in utils.CORRECTION_FACTORS:  # Took values from correction factor global variables and
                    # convert oxyde to element
                    calibration_chemical_element[sample][element] = calibration_data[sample][oxyde] * utils.CORRECTION_FACTORS[element]
                else:
                    non_convertible_oxyde[sample][oxyde] = calibration_data[sample][oxyde]

        return calibration_chemical_element, non_convertible_oxyde

    @staticmethod
    def extract_probe_calibration_pxrf_analysis(data):
        """
        Extract Si, Ca, Al value for each sample and create a dictionnary
        :param data: dictionnary of all dataset
        """
        extract_elements = {}
        frequency_sample = utils.calibration_sample_frequencies(data)
        for sample in data:
            extract_elements[sample] = {}
            for sample_id in range(1, frequency_sample[sample]):
                extract_elements[sample][sample_id] = {}
                for element in data[sample]:
                    if element == utils.TEXT_ELEMENT_SI or element == utils.TEXT_ELEMENT_AL or element == utils.TEXT_ELEMENT_CA or element == utils.TEXT_CALIBRATION_AN_CONTENT:
                        extract_elements[sample][sample_id][element] = data[sample][element]
        return extract_elements

    def calcul_correction_factor_for_each_sample(self, calibration_probe_dataset, calibration_pxrf_dataset):
        """
        ...
        :param calibration_probe_dataset:
        :param calibration_pxrf_dataset:
        :return:
        """
        data_correction_fact = {}
        probe = utils.extract_elements(calibration_probe_dataset)
        pxrf = self.extract_probe_calibration_pxrf_analysis(calibration_pxrf_dataset)
        frequencies_sample = utils.calibration_sample_frequencies(calibration_pxrf_dataset)
        for sample in pxrf:
            data_correction_fact[sample] = {}
            # Correction factor for each pxrf analysis
            for sample_id in range(1, frequencies_sample[sample]):
                data_correction_fact[sample][sample_id] = {}
                for element in pxrf[sample][sample_id]:
                    if element == utils.TEXT_ELEMENT_SI or element == utils.TEXT_ELEMENT_AL or element == utils.TEXT_ELEMENT_CA or element == utils.TEXT_CALIBRATION_AN_CONTENT:
                        data_correction_fact[sample][sample_id][element] = probe[sample][element] / pxrf[sample][sample_id][element]

        # Average of correction factor
        utils.correction_factor_params(data_correction_fact, utils.TEXT_AVERAGE)
        # Standart Deviation of correction factor
        utils.correction_factor_params(data_correction_fact, utils.TEXT_STD_DEVIATION)
