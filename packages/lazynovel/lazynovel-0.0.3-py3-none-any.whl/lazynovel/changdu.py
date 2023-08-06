#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from lazysdk import lazyrequests
from lazysdk import lazymd5
import time


def get_sign(
        distributor_id,  # 分销商标识
        secret_key,  # 签名密钥
        ts=None  # 时间戳
):
    """
    生成签名
    :param distributor_id: 分销商标识
    :param secret_key: 签名密钥
    :param ts: 时间戳
    """
    if ts is None:
        ts = int(time.time())
    param_str = str(distributor_id) + str(secret_key) + str(ts)
    return lazymd5.md5_str(content=param_str)


def get_charge(
        distributor_id,
        secret_key,
        ts=None,
        begin=None,
        end=None,
        offset=None,
        limit=None,
        device_id=None,
        outside_trade_no=None,
        paid=None
):
    """
    获取用户充值事件
    参考文档：https://bytedance.feishu.cn/docs/doccnGv5N4JQLKbk3uqeAEHoPTd#ahAvg5
    :param distributor_id:
    :param secret_key:
    :param ts:
    :param begin:
    :param end:
    :param offset:
    :param limit:
    :param device_id:
    :param outside_trade_no:
    :param paid:
    """
    sign = get_sign(
        distributor_id=distributor_id,
        secret_key=secret_key
    )
    params = {
        'distributor_id': distributor_id,
        'sign': sign
    }

    url = 'https://www.changdunovel.com/novelsale/openapi/user/recharge/v1'
    if ts is None:
        params['ts'] = int(time.time())
    if begin is not None:
        params['begin'] = begin
    if end is not None:
        params['end'] = end
    if offset is not None:
        params['offset'] = offset
    if limit is not None:
        params['limit'] = limit
    if device_id is not None:
        params['device_id'] = device_id
    if outside_trade_no is not None:
        params['outside_trade_no'] = outside_trade_no
    if paid is not None:
        params['paid'] = paid

    return lazyrequests.lazy_requests(
        method='GET',
        url=url,
        params=params,
        return_json=True
    )
