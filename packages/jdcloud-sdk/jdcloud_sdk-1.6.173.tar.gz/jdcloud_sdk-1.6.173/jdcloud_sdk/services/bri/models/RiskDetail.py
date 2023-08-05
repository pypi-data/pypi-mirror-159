# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class RiskDetail(object):

    def __init__(self, meRisk=None, lowRisk=None, medLoRisk=None, medHiRisk=None, hiRisk=None, unknown=None):
        """
        :param meRisk: (Optional) 中风险
        :param lowRisk: (Optional) 低风险
        :param medLoRisk: (Optional) 中低风险
        :param medHiRisk: (Optional) 中高风险
        :param hiRisk: (Optional) 高风险
        :param unknown: (Optional) 未知
        """

        self.meRisk = meRisk
        self.lowRisk = lowRisk
        self.medLoRisk = medLoRisk
        self.medHiRisk = medHiRisk
        self.hiRisk = hiRisk
        self.unknown = unknown
