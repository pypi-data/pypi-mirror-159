"""
Module containing all api calls for interacting with the algoralabs' backtest_state framework
"""
import json
from typing import Dict, Any

import pandas as pd

from algoralabs.backtests import PortfolioStateRequest, CashPaymentRequest
from algoralabs.common.enum import Order
from algoralabs.common.functions import no_transform
from algoralabs.common.requests import (
    __put_request, __async_put_request, __get_request, __async_get_request
)
from algoralabs.decorators.data import data_request, async_data_request


def _get_all_portfolio_state_request_info(backtest_id: str, order: Order = Order.ASC, **kwargs) -> dict:
    config = {
        "endpoint": f"config/backtest/{backtest_id}/state/portfolio?order={order}"
    }
    kwargs.update(config)

    return kwargs


@data_request
def get_all_portfolio_state(backtest_id: str, order: Order = Order.ASC, **kwargs) -> pd.DataFrame:
    request_info = _get_all_portfolio_state_request_info(backtest_id, order, **kwargs)
    return __get_request(**request_info)


@async_data_request
async def async_get_all_portfolio_state(backtest_id: str, order: Order = Order.ASC, **kwargs) -> pd.DataFrame:
    request_info = _get_all_portfolio_state_request_info(backtest_id, order, **kwargs)
    return await __async_get_request(**request_info)


def _get_all_cash_payments_request_info(backtest_id: str, order: Order, **kwargs) -> dict:
    config = {
        "endpoint": f"config/backtest/{backtest_id}/state/cash_payment?order={order}"
    }
    kwargs.update(config)

    return kwargs


@data_request
def get_all_cash_payments(backtest_id: str, order: Order = Order.ASC, **kwargs) -> pd.DataFrame:
    request_info = _get_all_cash_payments_request_info(backtest_id, order, **kwargs)
    return __get_request(**request_info)


@async_data_request
async def async_get_all_cash_payments(backtest_id: str, order: Order = Order.ASC, **kwargs) -> pd.DataFrame:
    request_info = _get_all_cash_payments_request_info(backtest_id, order, **kwargs)
    return await __async_get_request(**request_info)


def _create_portfolio_state_request_info(request: PortfolioStateRequest) -> dict:
    return {
        "endpoint": "config/backtest/state/portfolio",
        "json": json.loads(request.json())
    }


@data_request(transformer=no_transform)
def create_portfolio_state(request: PortfolioStateRequest) -> Dict[str, Any]:
    request_info = _create_portfolio_state_request_info(request)
    return __put_request(**request_info)


@async_data_request(transformer=no_transform)
async def async_create_portfolio_state(request: PortfolioStateRequest) -> Dict[str, Any]:
    request_info = _create_portfolio_state_request_info(request)
    return await __async_put_request(**request_info)


def _create_cash_payment_request_info(request: CashPaymentRequest) -> dict:
    return {
        "endpoint": "config/backtest/state/cash_payment",
        "json": json.loads(request.json())
    }


@data_request(transformer=no_transform)
def create_cash_payment(request: CashPaymentRequest) -> Dict[str, Any]:
    request_info = _create_cash_payment_request_info(request)
    return __put_request(**request_info)


@async_data_request(transformer=no_transform)
async def async_create_cash_payment(request: CashPaymentRequest) -> Dict[str, Any]:
    request_info = _create_cash_payment_request_info(request)
    return await __async_put_request(**request_info)
