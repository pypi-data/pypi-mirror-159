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


class RestoreLogicalBackupRequest(JDCloudRequest):
    """
    根据逻辑备份进行全量恢复
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(RestoreLogicalBackupRequest, self).__init__(
            '/regions/{regionId}/backupPlans/{backupPlanId}:restoreLogicalBackup', 'POST', header, version)
        self.parameters = parameters


class RestoreLogicalBackupParameters(object):

    def __init__(self, regionId,backupPlanId,backupId, sourceEndpoint, createNewEndpoint):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》]
        :param backupPlanId: 备份计划ID
        :param backupId: 用于恢复的备份Id，仅限于本备份计划生成的备份
        :param sourceEndpoint: 备份实例的数据源信息
        :param createNewEndpoint: 是否是新建数据源；true：是；false：不是
        """

        self.regionId = regionId
        self.backupPlanId = backupPlanId
        self.backupId = backupId
        self.sourceEndpoint = sourceEndpoint
        self.createNewEndpoint = createNewEndpoint

