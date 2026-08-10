"""Futures endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'china_futures_base_data': {
        'path': 'api/v1/market/data/futures/futures-base-data',
        'title': '中国期货基础数据',
        'doc_file': '中国期货基础数据.md',
        'original_api': 'get_china_futures_base_data_handler',
        'params': ('trade_date', 'symbol'),
    },
    'china_futures_lists': {
        'path': 'api/v1/market/data/futures/futures-lists',
        'title': '中国期货列表',
        'doc_file': '中国期货列表.md',
        'original_api': 'get_china_futures_lists_handler',
        'params': ('trade_date',),
    },
    'eastmoney_futures_position': {
        'path': 'api/v1/market/data/eastmoney-futures-position',
        'title': '东方财富期货持仓',
        'doc_file': '东方财富期货持仓.md',
        'original_api': 'get_eastmoney_futures_position',
        'params': ('exchange', 'variety_code', 'contract_code', 'trade_date', 'start_date', 'end_date', 'member_name_abbr', 'page', 'page_size'),
    },
    'eastmoney_futures_strange': {
        'path': 'api/v1/market/data/eastmoney-futures-strange',
        'title': '东方财富期货龙虎榜',
        'doc_file': '东方财富期货龙虎榜.md',
        'original_api': 'eastmoney_futures_strange',
        'params': ('exchange', 'variety', 'contract', 'trade_date'),
    },
    'futures_contract_kline': {
        'path': 'api/v1/market/data/futures/kline',
        'title': '期货合约K线',
        'doc_file': '期货合约K线.md',
        'original_api': 'futures_contract_kline',
        'params': ('symbol', 'interval', 'start', 'end', 'limit'),
    },
    'futures_kline': {
        'path': 'api/v1/market/data/futures/kline',
        'title': '期货合约K线',
        'doc_file': '期货合约K线.md',
        'original_api': 'futures_contract_kline',
        'params': ('symbol', 'interval', 'start', 'end', 'limit'),
    },
    'futures_kline_intraday': {
        'path': 'api/v1/market/data/futures/kline/intraday',
        'title': '期货日内K线',
        'doc_file': '期货日内K线.md',
        'original_api': 'futures_kline_intraday',
        'params': ('symbol', 'interval', 'start', 'end', 'limit'),
    },
    'futures_kline_latest': {
        'path': 'api/v1/market/data/futures/kline/latest',
        'title': '期货最新K线',
        'doc_file': '期货最新K线.md',
        'original_api': 'futures_kline_latest',
        'params': ('symbol', 'interval'),
    },
    'futures_eod_price': {
        'path': 'api/v1/market/data/futures/eod-price',
        'title': '期货日终行情',
        'doc_file': '期货日终行情.md',
        'original_api': 'futures_eod_price',
        'params': ('exchange', 'symbol', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 200,
    },
    'major_contract': {
        'path': 'api/v1/market/data/corporate/contract',
        'title': '重大合同',
        'doc_file': '重大合同.md',
        'original_api': 'major_contract',
        'params': ('start_date', 'end_date'),
        'max_page_size': 3,
    },
    'major_contract_by_symbol': {
        'path': 'api/v1/market/data/corporate/contract/by-symbol',
        'title': '重大合同按标的',
        'doc_file': '重大合同按标的.md',
        'original_api': 'major_contract_by_symbol',
        'params': ('symbol', 'page', 'page_size'),
    },
    'major_contract_summary': {
        'path': 'api/v1/market/data/corporate/contract/summary',
        'title': '重大合同汇总',
        'doc_file': '重大合同汇总.md',
        'original_api': 'major_contract_summary',
        'params': ('page', 'page_size'),
    },
    'member_build_process': {
        'path': 'api/v1/market/data/member-build-process',
        'title': '会员建仓过程',
        'doc_file': '会员建仓过程.md',
        'original_api': 'member_build_process',
        'params': ('exchange', 'member_name', 'instrument_id', 'start_date', 'end_date', 'contract_multiplier', 'page', 'page_size'),
        'max_page_size': 200,
    },
    'member_position_ranking': {
        'path': 'api/v1/market/data/member-position-ranking',
        'title': '会员持仓排名',
        'doc_file': '会员持仓排名.md',
        'original_api': 'member_position_ranking',
        'params': ('exchange', 'instrument_id', 'trade_date', 'direction', 'page', 'page_size'),
        'max_page_size': 200,
    },
})
