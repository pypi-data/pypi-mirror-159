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


class DescribeCcsIpListRequest(JDCloudRequest):
    """
    查询用户可设置为网站类规则回源 IP 的京东云托管区公网 IP 资源
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeCcsIpListRequest, self).__init__(
            '/regions/{regionId}/ccsIpResources', 'GET', header, version)
        self.parameters = parameters


class DescribeCcsIpListParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 区域 ID, 高防不区分区域, 传 cn-north-1 即可
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为 1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小, 默认为 10, 取值范围 [0, 100], 0 表示全量
        """
        self.pageSize = pageSize

