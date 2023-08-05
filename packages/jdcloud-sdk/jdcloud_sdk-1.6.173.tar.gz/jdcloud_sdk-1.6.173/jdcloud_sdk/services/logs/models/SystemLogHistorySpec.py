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


class SystemLogHistorySpec(object):

    def __init__(self, appName, instance, logType, time, exactMatch=None, keyword=None, order=None, page=None, size=None):
        """
        :param appName:  
        :param exactMatch: (Optional) 精确匹配，true 或者 false
        :param instance:  
        :param keyword: (Optional) 查询关键字
        :param logType:  
        :param order: (Optional) 排序，取值"ASC"或"DESC"，默认"ASC"
        :param page: (Optional) 页数，从1开始
        :param size: (Optional) 每页日志条数
        :param time:  
        """

        self.appName = appName
        self.exactMatch = exactMatch
        self.instance = instance
        self.keyword = keyword
        self.logType = logType
        self.order = order
        self.page = page
        self.size = size
        self.time = time
