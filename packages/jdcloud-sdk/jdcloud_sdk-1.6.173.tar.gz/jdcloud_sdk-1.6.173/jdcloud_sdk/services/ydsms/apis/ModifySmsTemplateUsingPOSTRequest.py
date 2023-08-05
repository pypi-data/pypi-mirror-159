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


class ModifySmsTemplateUsingPOSTRequest(JDCloudRequest):
    """
    编辑短信模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifySmsTemplateUsingPOSTRequest, self).__init__(
            '/smsTemplates/{templateId}', 'POST', header, version)
        self.parameters = parameters


class ModifySmsTemplateUsingPOSTParameters(object):

    def __init__(self, templateId, appId, templateContent, templateName, templateType):
        """
        :param templateId: 模板id
        :param appId: 应用id
        :param templateContent: 模板内容
        :param templateName: 模板名称
        :param templateType: 模板类型:0 验证码短信,1 通知短信,2 推广短信
        """

        self.templateId = templateId
        self.appId = appId
        self.applyExplanation = None
        self.templateContent = templateContent
        self.templateName = templateName
        self.templateType = templateType

    def setApplyExplanation(self, applyExplanation):
        """
        :param applyExplanation: (Optional) 申请说明
        """
        self.applyExplanation = applyExplanation

