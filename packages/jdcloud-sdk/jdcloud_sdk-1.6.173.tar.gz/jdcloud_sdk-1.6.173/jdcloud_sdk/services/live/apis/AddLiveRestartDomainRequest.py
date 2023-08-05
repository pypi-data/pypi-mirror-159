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


class AddLiveRestartDomainRequest(JDCloudRequest):
    """
    添加回看域名

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddLiveRestartDomainRequest, self).__init__(
            '/domains:restart', 'PUT', header, version)
        self.parameters = parameters


class AddLiveRestartDomainParameters(object):

    def __init__(self, playDomain, restartDomain):
        """
        :param playDomain: 直播的播放域名
- 回看域名所对应的原播放域名,新建的回看域名将绑定到此播放域名下

        :param restartDomain: 直播回看域名
- 直播域名必须已经备案完成

        """

        self.playDomain = playDomain
        self.restartDomain = restartDomain

