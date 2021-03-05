# SPDX-License-Identifier: GPL-2.0-only
# Copyright (c) 2019-2020 NITK Surathkal

"""APIs to check the types of attributes"""

import re

class TypeChecker:
    """ Checks for proper type of parameter and units"""
    def __init__(self):
        print("checking types")
    def match_string(self, data_str):
        """
        Check if the given string matches the regex expression

        parameter
        ---------
        data_str : str
            string to match
        """
        match = re.fullmatch(r'[0-9]+(\.[0-9]+)?[A-Za-z]+', data_str)
        return match

    def check_delay_type(self, delay_str):
        """
        check for proper unit for delay

        parameters
        ----------
        delay_str : str
            delay attribute to be checked
        """
        delay_match = self.match_string(delay_str)
        if not delay_match:
            raise Exception(
                "Provide a proper value and unit for delay attribute. "
            )

        index = 0
        for i in delay_str:
            if i.isalpha():
                index = delay_str.index(i)
                break
        delay_type =['s','sec','secs','ms','msec','msecs','us','usec','usecs']
        unit = delay_str[index:]
        if unit not in delay_type:
            raise Exception(
                "Invalid unit for delay attribute"
                "Provide a valid unit for delay attribute. "
            )


    def check_bandwidth_type(self, bandwidth_str):
        """
        check for proper unit for bandwidth

        parameters
        ----------
        bandwidth_str : str
            bandwidth attribute to be checked
        """
        bandwidth_match = self.match_string(bandwidth_str)
        if not bandwidth_match:
            raise Exception(
                    "Provide a proper value and unit for bandwidth attribute. "
                )
        index = 0
        for i in bandwidth_str:
            if i.isalpha():
                index = bandwidth_str.index(i)
                break
        bandwidth_type = ['bit', 'kbit', 'kibit', 'mbit', 'mibit', 'gbit',
                            'gibit', 'tbit', 'tibit','bps', 'kbps', 'kibps',
                            'mbps', 'mibps', 'gbps', 'gibps', 'tbps', 'tibps']
        unit = bandwidth_str[index:]
        if unit not in bandwidth_type:
            raise Exception(
                "Invalid unit for bandwidth attribute"
                "Provide a valid unit. "
            )
