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


class Page(object):

    def __init__(self, totalSize=None, totalPage=None, pageSize=None, nowPage=None):
        """
        :param totalSize: (Optional) 总数
        :param totalPage: (Optional) 总分页数
        :param pageSize: (Optional) 当前报分页大小
        :param nowPage: (Optional) 当前页码
        """

        self.totalSize = totalSize
        self.totalPage = totalPage
        self.pageSize = pageSize
        self.nowPage = nowPage
