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


class CreateWafBlackRuleRequest(JDCloudRequest):
    """
    新增一条黑名单规则
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateWafBlackRuleRequest, self).__init__(
            '/domain/{domain}/wafBlackRule', 'POST', header, version)
        self.parameters = parameters


class CreateWafBlackRuleParameters(object):

    def __init__(self, domain,):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.ruleType = None
        self.matchOp = None
        self.val = None
        self.atOp = None
        self.atVal = None

    def setRuleType(self, ruleType):
        """
        :param ruleType: (Optional) 黑名单类型， uri ip geo
        """
        self.ruleType = ruleType

    def setMatchOp(self, matchOp):
        """
        :param matchOp: (Optional) 匹配模式,uri类型有效，0=完全匹配  1=前缀匹配 2=包含 3=正则 4=大于 5=后缀
        """
        self.matchOp = matchOp

    def setVal(self, val):
        """
        :param val: (Optional) 匹配值
        """
        self.val = val

    def setAtOp(self, atOp):
        """
        :param atOp: (Optional) 1：forbidden，493封禁并返回自定义页面 2：redirect，302跳转 3： verify@captcha 4： verify@jscookie
        """
        self.atOp = atOp

    def setAtVal(self, atVal):
        """
        :param atVal: (Optional) action为1时为自定义页面名称,空值或缺省值default为默认页面，2时为跳转url，其他时无效
        """
        self.atVal = atVal

