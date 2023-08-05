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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeInstancesRequest(JDCloudRequest):
    """
    套餐实例列表信息查询
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstancesRequest, self).__init__(
            '/regions/{regionId}/instances', 'GET', header, version)
        self.parameters = parameters


class DescribeInstancesParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.pageSize = None
        self.pageNumber = None
        self.instanceName = None

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 页容量，默认10, 范围（1-100）
        """
        self.pageSize = pageSize

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页序号，默认1，不能小于1
        """
        self.pageNumber = pageNumber

    def setInstanceName(self, instanceName):
        """
        :param instanceName: (Optional) 实例名称
        """
        self.instanceName = instanceName

