"""Hong Kong market endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'hk_candlesticks': {
        'path': 'api/v3/market/data/hk/hk-candlesticks',
        'title': '港股K线',
        'doc_file': '港股K线.md',
        'original_api': 'get_hk_candlesticks',
        'params': ('trade_code', 'interval_unit', 'until_date', 'since_date', 'interval_value', 'limit', 'adjust_kind'),
    },
    'hk_stock_info_all': {
        'path': 'api/v4/market/data/hk-stock-info-all',
        'title': '港股实时行情',
        'doc_file': '港股实时行情.md',
        'original_api': 'hk_stock_info_all',
        'params': (),
    },
})
