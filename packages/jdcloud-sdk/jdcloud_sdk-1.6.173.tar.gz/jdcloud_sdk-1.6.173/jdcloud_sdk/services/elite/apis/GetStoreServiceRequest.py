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


class GetStoreServiceRequest(JDCloudRequest):
    """
    获取云存服务信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetStoreServiceRequest, self).__init__(
            '/regions/{regionId}/getStoreService', 'GET', header, version)
        self.parameters = parameters


class GetStoreServiceParameters(object):

    def __init__(self, regionId, buyerPin, businessData, ):
        """
        :param regionId: 地域ID
        :param buyerPin: 购买用户pin
        :param businessData: 业务数据，与下单时的业务数据一致
        """

        self.regionId = regionId
        self.buyerPin = buyerPin
        self.businessData = businessData
        self.queryAll = None

    def setQueryAll(self, queryAll):
        """
        :param queryAll: (Optional) 是否查询全部，如果传入false，则只查询当前时间有效的，否则查询所有的
        """
        self.queryAll = queryAll

