#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
获取基金名称
"""

import requests
import js2py


def fund_name_em(fund: str = "000002"):
    """
    东方财富网-天天基金网-基金数据
    :param fund: 基金代码
    :type fund: str
    :return: 指定基金名称
    :rtype: str
    """

    url = f"http://fund.eastmoney.com/pingzhongdata/{fund}.js"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    data_text = r.text
    context = js2py.EvalJs()
    context.execute(data_text)
    name = context['fS_name'] or ''
    return name
