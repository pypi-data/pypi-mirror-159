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


class Instance(object):

    def __init__(self, id=None, name=None, region=None, type=None, ipCount=None, aclLimit=None, basicBandwidth=None, elasticBandwidth=None, expireTime=None, createTime=None, protectedObjects=None, onTrial=None, resourceId=None, tags=None):
        """
        :param id: (Optional) 防护包实例 Id
        :param name: (Optional) 防护包实例名称
        :param region: (Optional) 防护包实例地域
        :param type: (Optional) 套餐类型. <br>- 1: 独享 IP<br>- 2: 共享 IP
        :param ipCount: (Optional) 可防护 IP 个数
        :param aclLimit: (Optional) 可添加的访问控制规则数量
        :param basicBandwidth: (Optional) 保底带宽, 单位 Gbps
        :param elasticBandwidth: (Optional) 弹性带宽, 单位 Gbps
        :param expireTime: (Optional) 实例过期时间
        :param createTime: (Optional) 实例创建时间
        :param protectedObjects: (Optional) 防护对象
        :param onTrial: (Optional) 是否为试用防护包
        :param resourceId: (Optional) 资源 Id
        :param tags: (Optional) Tag信息
        """

        self.id = id
        self.name = name
        self.region = region
        self.type = type
        self.ipCount = ipCount
        self.aclLimit = aclLimit
        self.basicBandwidth = basicBandwidth
        self.elasticBandwidth = elasticBandwidth
        self.expireTime = expireTime
        self.createTime = createTime
        self.protectedObjects = protectedObjects
        self.onTrial = onTrial
        self.resourceId = resourceId
        self.tags = tags
