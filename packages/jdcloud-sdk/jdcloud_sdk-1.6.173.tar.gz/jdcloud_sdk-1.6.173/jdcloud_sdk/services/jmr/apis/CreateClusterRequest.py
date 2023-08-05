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


class CreateClusterRequest(JDCloudRequest):
    """
    创建集群
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateClusterRequest, self).__init__(
            '/regions/{regionId}/cluster:create', 'POST', header, version)
        self.parameters = parameters


class CreateClusterParameters(object):

    def __init__(self, regionId, clusterSpec, ):
        """
        :param regionId: 地域ID
        :param clusterSpec: 描述集群配置
        """

        self.regionId = regionId
        self.clusterSpec = clusterSpec
        self.clientToken = None

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 用于保证请求的幂等性。由客户端生成，长度不能超过64个字符。

        """
        self.clientToken = clientToken

