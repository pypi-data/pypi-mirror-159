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


class StartMigrationJobRequest(JDCloudRequest):
    """
    启动迁移job，开始迁移数据
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(StartMigrationJobRequest, self).__init__(
            '/regions/{regionId}/instance/{instanceId}:migrate', 'POST', header, version)
        self.parameters = parameters


class StartMigrationJobParameters(object):

    def __init__(self, regionId,instanceId,):
        """
        :param regionId: 迁移任务所在区域的Region ID。华北-北京(cn-north-1)，华东-上海(cn-east-2)，华南-广州(cn-south-1)
        :param instanceId: 迁移任务的唯一标识
        """

        self.regionId = regionId
        self.instanceId = instanceId

