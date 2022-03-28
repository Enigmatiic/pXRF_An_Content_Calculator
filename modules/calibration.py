"""

"""
import modules.utils as utils
from statistics import mean

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
    def convert_oxid_to_element(calibration_data):
        """
        ...
        :param calibration_data:
        :return:
        """
        calibration_chemical_element = {}
        non_convertible_oxid = {}
        for sample in calibration_data:
            calibration_chemical_element[sample] = {}
            for _oxide in calibration_data[sample]:
                if _oxide == utils.TEXT_CALIBRATION_AN_CONTENT:
                    continue
                element = _oxide.lower()
                if element in utils.CORRECTION_FACTORS:  # Took values from correction factor global variables and
                    # convert _oxide to element
                    calibration_chemical_element[sample][utils.ELEMENTS[element]] = calibration_data[sample][_oxide] * utils.CORRECTION_FACTORS[element]

        return calibration_chemical_element, non_convertible_oxid

    @staticmethod
    def extract_probe_calibration_pxrf_analysis(data):
        """
        Extract Si, Ca, Al value for each sample and create a dictionary
        :param data: dictionary of all dataset
        """
        extract_elements = {}
        for sample in data:
            extract_elements[sample] = {}
            for sample_id in data[sample]:
                extract_elements[sample][sample_id] = {}
                for element in data[sample][sample_id]:
                    if element == utils.TEXT_ELEMENT_SI or element == utils.TEXT_ELEMENT_AL or element == utils.TEXT_ELEMENT_CA or element == utils.TEXT_CALIBRATION_AN_CONTENT:
                        extract_elements[sample][sample_id][element] = data[sample][sample_id][element]
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
        for sample in pxrf:
            utils.CORRECTION_FACTOR_BY_SAMPLE[sample] = {}
            for sample_id in pxrf[sample]:
                utils.CORRECTION_FACTOR_BY_SAMPLE[sample][sample_id] = {}
                for element in pxrf[sample][sample_id]:
                    if sample in probe:
                        if element == utils.TEXT_ELEMENT_SI or element == utils.TEXT_ELEMENT_AL or element == utils.TEXT_ELEMENT_CA or element == utils.TEXT_CALIBRATION_AN_CONTENT:
                            utils.CORRECTION_FACTOR_BY_SAMPLE[sample][sample_id][element] = probe[sample][element] / pxrf[sample][sample_id][element]
                    else:
                        print('Les données de calibration n\'ont pas de reference d\'analyse de microsonde')
                        return
        # Average of correction factor
        utils.correction_factor_params(utils.TEXT_AVERAGE)
        # Standard Deviation of correction factor
        utils.correction_factor_params(utils.TEXT_STD_DEVIATION)
        # Relative Standard Deviation of correction factor
        utils.relative_std_deviation()

    @staticmethod
    def correction_factor(dataset):
        si_factor, al_factor, ca_factor = [], [], []
        for sample in dataset:
            si_factor.append(dataset[sample][utils.TEXT_AVERAGE][utils.TEXT_ELEMENT_SI])
            al_factor.append(dataset[sample][utils.TEXT_AVERAGE][utils.TEXT_ELEMENT_AL])
            ca_factor.append(dataset[sample][utils.TEXT_AVERAGE][utils.TEXT_ELEMENT_CA])

        utils.CORRECTION_FACTOR[utils.TEXT_ELEMENT_SI] = mean(si_factor)
        utils.CORRECTION_FACTOR[utils.TEXT_ELEMENT_AL] = mean(al_factor)
        utils.CORRECTION_FACTOR[utils.TEXT_ELEMENT_CA] = mean(ca_factor)
