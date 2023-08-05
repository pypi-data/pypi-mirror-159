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


class CreateReplicationTaskCondition(object):

    def __init__(self, action, bucketName, bucketRegion, targetBucketName, targetBucketRegion, storageClass, prefixSet=None):
        """
        :param action:  是否覆盖
        :param bucketName:  bucket名称
        :param bucketRegion:  bucket所属区域
        :param targetBucketName:  目标bucket名称
        :param targetBucketRegion:  目标bucket所属区域
        :param storageClass:  存储类型
        :param prefixSet: (Optional) 
        """

        self.action = action
        self.bucketName = bucketName
        self.bucketRegion = bucketRegion
        self.targetBucketName = targetBucketName
        self.targetBucketRegion = targetBucketRegion
        self.storageClass = storageClass
        self.prefixSet = prefixSet
