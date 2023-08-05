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


class UpdateLogDownloadURLInternalRequest(JDCloudRequest):
    """
    设置日志文件的下载链接过期时间，重新生成 PostgreSQL 的日志文件下载地址
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateLogDownloadURLInternalRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/log/{logId}:updateLogDownloadURLInternal', 'POST', header, version)
        self.parameters = parameters


class UpdateLogDownloadURLInternalParameters(object):

    def __init__(self, regionId, instanceId, logId, seconds):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param logId: 日志文件ID
        :param seconds: 设置链接地址的过期时间，单位是秒，最长不能超过取值范围为 1 ~ 86400 秒
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.logId = logId
        self.seconds = seconds

