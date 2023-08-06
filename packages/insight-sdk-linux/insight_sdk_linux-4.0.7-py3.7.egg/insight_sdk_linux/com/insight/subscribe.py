#!/usr/bin/python3
# -*- coding: utf-8 -*-
from .. import data_handle
from ..interface.mdc_gateway_base_define import ESubscribeActionType


# 根据证券数据来源订阅行情数据,由三部分确定行情数据
# 行情源(SecurityIdSource):XSHG(沪市)|XSHE(深市)|...
# 证券类型(SecurityType):BondType(债)|StockType(股)|FundType(基)|IndexType(指)|OptionType(期权)|...
# 数据类型(MarketDataTypes):MD_TICK(快照)|MD_TRANSACTION(逐笔成交)|MD_ORDER(逐笔委托)|...
def subscribe_by_type(dictmarketdatatypes, MDSubscribe=ESubscribeActionType.COVERAGE):
    # element
    # params1: ESecurityIDSource枚举值 --行情源
    # params2: ESecurityType的枚举值 --证券类型
    # params3: EMarketDataType的枚举值集合 --数据类型
    listmarketdatatype = []
    for dictmarketdatatype in iter(dictmarketdatatypes):
        listmarketdatatype.append(dictmarketdatatype)
    data_handle.get_interface().subscribebytype(MDSubscribe, listmarketdatatype)
    sync()


# 根据证券ID来源订阅行情数据
def subscribe_by_id(dictHTSCSecurityIDs, MDSubscribe=ESubscribeActionType.COVERAGE):
    listHTSCSecurityIDs = []
    for dictHTSCSecurityID in iter(dictHTSCSecurityIDs):
        listHTSCSecurityIDs.append(dictHTSCSecurityID)
    data_handle.get_interface().subscribebyid(MDSubscribe, listHTSCSecurityIDs)
    sync()


# 阻塞当前线程，防止本模块执行退出操作
def sync():
    print("input any key to exit >>>")
    line = input()
    if len(str(line)) > 0:
        print("sync: input-->>" + str(line) + ",then exit this sync.")
