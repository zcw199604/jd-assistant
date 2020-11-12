#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    sku_ids = '100016129294'  # 商品id
    area = '1_2800_2850'  # 区域id
    asst = Assistant()  # 初始化

    asst.login_by_QRcode()  # 扫码登陆
    # 定时启动任务
    #asst.start_submit_order('2020-11-10 23:59:59.830')
    # 根据库存自动下单商品
    #asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    #asst.setSystemTime()
    # 抢购商品-> 整点放出抢购链接，根据抢购链接进行下单
    #asst.exec_seckill(sku_ids)
    asst.exec_seckill_by_time(sku_ids,'2020-11-12 15:06:00.000')
    #print(asst._get_seckill_init_info(sku_ids))
    #print(asst.if_item_can_be_ordered(sku_ids=sku_ids, area=area))
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
