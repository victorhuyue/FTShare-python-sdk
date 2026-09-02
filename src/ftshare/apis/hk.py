"""Hong Kong market API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class HkApiMixin:
    """Endpoint methods for the hk ftshare-doc topic."""

    def hk_candlesticks(
        self,
        trade_code: Any | None = None,
        interval_unit: Any | None = None,
        until_date: Any | None = None,
        since_date: Any | None = None,
        interval_value: Any | None = None,
        limit: Any | None = None,
        adjust_kind: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """港股K线.

        Endpoint: ``api/v2/market/data/hk/hk-candlesticks``.
        Method: ``GET``.
        Documented endpoint: ``get_hk_candlesticks``.

        Args:
            trade_code: 港股代码，如 `00700.HK` 或 `700` (type: string; required: Y).
            interval_unit: 间隔单位：day / month / quarter / year (type: string; required: Y).
            until_date: 结束日期（YYYY-MM-DD） (type: date; required: Y).
            since_date: 开始日期（YYYY-MM-DD） (type: date; required: N).
            interval_value: 间隔数值（当前仅支持 1） (type: int; required: N).
            limit: 数量限制（保留最近 N 根） (type: int; required: N).
            adjust_kind: 复权类型：forward(默认/前复权) / none(不复权) (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code, 'interval_unit': interval_unit, 'until_date': until_date, 'since_date': since_date, 'interval_value': interval_value, 'limit': limit, 'adjust_kind': adjust_kind}
        request_params.update(kwargs)
        return self._call_endpoint(
            'hk_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
