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


class ActivityLog(object):

    def __init__(self, timestamp=None, firewallAction=None, country=None, ip=None, host=None, httpMethod=None, httpProtocol=None, requestUri=None, firewallSource=None, userAgent=None, ruleId=None):
        """
        :param timestamp: (Optional) 
        :param firewallAction: (Optional) 
        :param country: (Optional) 
        :param ip: (Optional) 
        :param host: (Optional) 
        :param httpMethod: (Optional) 
        :param httpProtocol: (Optional) 
        :param requestUri: (Optional) 
        :param firewallSource: (Optional) 
        :param userAgent: (Optional) 
        :param ruleId: (Optional) 
        """

        self.timestamp = timestamp
        self.firewallAction = firewallAction
        self.country = country
        self.ip = ip
        self.host = host
        self.httpMethod = httpMethod
        self.httpProtocol = httpProtocol
        self.requestUri = requestUri
        self.firewallSource = firewallSource
        self.userAgent = userAgent
        self.ruleId = ruleId
