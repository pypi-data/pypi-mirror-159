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


class OrderReq(object):

    def __init__(self, region, buyType, timeSpan, timeUnit, startTime, packageType, extraDomainsNum, returnURL, extraBitsLimit, wafInstanceId=None, nickName=None, appCode=None, serviceCode=None, buyScenario=None, needPay=None):
        """
        :param region:  地域信息, hb_bgp, hn, hd_bgp 企业版支持两个，旗舰版支持3个，多个以 , 分隔
        :param buyType:  购买类型, 1:创建 2:续费 3:升配
        :param timeSpan:  购买时长
        :param timeUnit:  时间单位，month, year
        :param startTime:  创建时间
        :param wafInstanceId: (Optional) 实例id，除新建必传
        :param packageType:  套餐类型 1:高级版, 2:企业版 3:旗舰版 4:基础版(仅支持新用户)
        :param extraDomainsNum:  额外的域名扩展包
        :param nickName: (Optional) 实例名，新建订单时必传，只能包含汉字、英文字母、下划线、破折号、数字，且长度不能超过16
        :param returnURL:  下单成功后返回的url, eg:http://abc.com
        :param extraBitsLimit:  额外的qps扩展包,单位为M 该值为50M的倍数
        :param appCode: (Optional) 云鼎的appCode
        :param serviceCode: (Optional) 云鼎的serviceCode
        :param buyScenario: (Optional) 购物车活动参数
        :param needPay: (Optional) true表示支持autoPay
        """

        self.region = region
        self.buyType = buyType
        self.timeSpan = timeSpan
        self.timeUnit = timeUnit
        self.startTime = startTime
        self.wafInstanceId = wafInstanceId
        self.packageType = packageType
        self.extraDomainsNum = extraDomainsNum
        self.nickName = nickName
        self.returnURL = returnURL
        self.extraBitsLimit = extraBitsLimit
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.buyScenario = buyScenario
        self.needPay = needPay
