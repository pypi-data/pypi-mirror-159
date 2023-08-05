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


class SendDataVO(object):

    def __init__(self, jobId, role, toRole, key, value, taskType, ):
        """
        :param jobId:  任务ID
        :param role:  数据源角色
        :param toRole:  数据目标角色
        :param key:  数据key
        :param value:  数据value
        :param taskType:  任务类型
        """

        self.jobId = jobId
        self.role = role
        self.toRole = toRole
        self.key = key
        self.value = value
        self.taskType = taskType
