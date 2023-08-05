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


class UpdateAlarmSpec(object):

    def __init__(self, name=None, metric=None, period=None, statisticMethod=None, operator=None, threshold=None, times=None, noticePeriod=None, status=None, noticeMethod=None, userId=None, groupId=None):
        """
        :param name: (Optional) 规则名称
        :param metric: (Optional) 监控项，bandwidthTrafficIn:上行实时流量 bandwidthTrafficOut:下行实时流量
        :param period: (Optional) 统计周期（单位：分钟）
        :param statisticMethod: (Optional) 统计方法：平均值=avg、最大值=max、最小值=min
        :param operator: (Optional) 计算方式 >=、>、<、<=、=、！=
        :param threshold: (Optional) 阈值
        :param times: (Optional) 连续多少次后报警
        :param noticePeriod: (Optional) 通知周期 单位：小时
        :param status: (Optional) 规则状态 disabled:禁用 enabled:启用
        :param noticeMethod: (Optional) 通知方式 all:全部 sms：短信 email:邮件
        :param userId: (Optional) 通知对象用户ID,若多个用逗号分隔
        :param groupId: (Optional) 通知对象组ID
        """

        self.name = name
        self.metric = metric
        self.period = period
        self.statisticMethod = statisticMethod
        self.operator = operator
        self.threshold = threshold
        self.times = times
        self.noticePeriod = noticePeriod
        self.status = status
        self.noticeMethod = noticeMethod
        self.userId = userId
        self.groupId = groupId
