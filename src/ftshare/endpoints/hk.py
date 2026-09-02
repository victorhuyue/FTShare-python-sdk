"""Hong Kong market endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'hk_candlesticks': {
        'path': 'api/v2/market/data/hk/hk-candlesticks',
        'title': '港股K线',
        'doc_file': '港股K线.md',
        'original_api': 'get_hk_candlesticks',
        'params': ('trade_code', 'interval_unit', 'until_date', 'since_date', 'interval_value', 'limit', 'adjust_kind'),
    },
})
