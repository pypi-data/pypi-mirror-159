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


class GeneralAlterViewRequest(JDCloudRequest):
    """
    生成修改视图sql语句
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GeneralAlterViewRequest, self).__init__(
            '/regions/{regionId}/view:generalAlter', 'POST', header, version)
        self.parameters = parameters


class GeneralAlterViewParameters(object):

    def __init__(self, regionId,):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.dataSourceId = None
        self.dbName = None
        self.viewName = None
        self.originViewName = None
        self.viewAlgorithm = None
        self.definer = None
        self.viewSecurity = None
        self.viewCheckOption = None
        self.definitionSql = None

    def setDataSourceId(self, dataSourceId):
        """
        :param dataSourceId: (Optional) 数据源id
        """
        self.dataSourceId = dataSourceId

    def setDbName(self, dbName):
        """
        :param dbName: (Optional) 数据库名称。
        """
        self.dbName = dbName

    def setViewName(self, viewName):
        """
        :param viewName: (Optional) 视图名称。
        """
        self.viewName = viewName

    def setOriginViewName(self, originViewName):
        """
        :param originViewName: (Optional) 原始视图名称。
        """
        self.originViewName = originViewName

    def setViewAlgorithm(self, viewAlgorithm):
        """
        :param viewAlgorithm: (Optional) 视图算法，DEFAULT("DEFAULT", 1),UNDEFINED("UNDEFINED", 2), MERGE("MERGE", 3), TEMPTABLE("TEMPTABLE", 4);
        """
        self.viewAlgorithm = viewAlgorithm

    def setDefiner(self, definer):
        """
        :param definer: (Optional) 定义者。
        """
        self.definer = definer

    def setViewSecurity(self, viewSecurity):
        """
        :param viewSecurity: (Optional) 安全性，DEFAULT("DEFAULT", 1),DEFINER("DEFINER", 2), INVOKER("INVOKER", 3);
        """
        self.viewSecurity = viewSecurity

    def setViewCheckOption(self, viewCheckOption):
        """
        :param viewCheckOption: (Optional) 检查选项，DEFAULT("DEFAULT", 1),LOCAL("LOCAL", 2), CASCADED("CASCADED", 3);;
        """
        self.viewCheckOption = viewCheckOption

    def setDefinitionSql(self, definitionSql):
        """
        :param definitionSql: (Optional) 视图定义。
        """
        self.definitionSql = definitionSql

