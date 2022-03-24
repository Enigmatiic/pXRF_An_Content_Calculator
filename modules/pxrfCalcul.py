"""
Module for pXRF Calculation
"""

class pxrf_calcul():
    def __init__(self):
        super(pxrf_calcul, self).__init__()

    def is_plag(self, sample_data):
        """
        Verify if data for sample given is plagioclase
        :param sample_data: element values for sample
        :return: True or False
        """
        pass

    def extract_elements(self, data):
        """
        Extract Si, Ca, Al value for each sample and create a dictionnary
        :param data: dictionnary of all dataset
        """
        pass

    def calcul_ratio(self, elements):
        """
        Calcul ratio (Si/Ca)
        :param elements:
        :return:
        """
        pass

    def calcul_an_content(self, ratio):
        """
        Calcul An Content from ratio (Si/Ca)
        :param ratio:
        :return:
        """
        pass