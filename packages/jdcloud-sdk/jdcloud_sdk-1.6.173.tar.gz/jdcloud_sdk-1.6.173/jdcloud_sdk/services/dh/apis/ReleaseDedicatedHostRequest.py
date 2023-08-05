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


class ReleaseDedicatedHostRequest(JDCloudRequest):
    """
    释放按配置计费、或包年包月已到期的单个专有宿主机。不能释放没有计费信息的专有宿主机。<br>
专有宿主机状态必须为可用<b>available</b>、不可用<b>unavailable</b>、维护中<b>under-assessment</b>，同时专有宿主机上必须没有云主机实例才可删除。<br>
 [MFA enabled]
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ReleaseDedicatedHostRequest, self).__init__(
            '/regions/{regionId}/dedicatedHost/{dedicatedHostId}', 'DELETE', header, version)
        self.parameters = parameters


class ReleaseDedicatedHostParameters(object):

    def __init__(self, regionId,dedicatedHostId,):
        """
        :param regionId: 地域ID
        :param dedicatedHostId: 专有宿主机ID
        """

        self.regionId = regionId
        self.dedicatedHostId = dedicatedHostId

