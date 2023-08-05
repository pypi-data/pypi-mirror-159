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


class Forward(object):

    def __init__(self, forwardId=None, userPin=None, userName=None, deviceCollectorType=None, frequency=None, endPoint=None, queueUrl=None, ak=None, sk=None, createdTime=None, updatedTime=None):
        """
        :param forwardId: (Optional) 消息转发唯一标识
        :param userPin: (Optional) 用户PIN
        :param userName: (Optional) 用户名称
        :param deviceCollectorType: (Optional) 设备类型
        :param frequency: (Optional) 频度(分钟/次)
        :param endPoint: (Optional) 接入点地址，长度限制1~100
        :param queueUrl: (Optional) 队列URL，长度限制1~255
        :param ak: (Optional) Access Key ID，长度限制1~50
        :param sk: (Optional) Access Key Secret，长度限制1~50
        :param createdTime: (Optional) 创建时间，时间为东八区（UTC/GMT+08:00）
        :param updatedTime: (Optional) 修改时间，时间为东八区（UTC/GMT+08:00）
        """

        self.forwardId = forwardId
        self.userPin = userPin
        self.userName = userName
        self.deviceCollectorType = deviceCollectorType
        self.frequency = frequency
        self.endPoint = endPoint
        self.queueUrl = queueUrl
        self.ak = ak
        self.sk = sk
        self.createdTime = createdTime
        self.updatedTime = updatedTime
