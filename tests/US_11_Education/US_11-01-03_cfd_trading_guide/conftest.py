"""
-*- coding: utf-8 -*-
@Time    : 2023/09/13 10:00
@Author  : Alexander Tomelo
"""
import pytest


@pytest.fixture(
    scope="function",
    params=[
        "most_traded",
        "top_risers",
        "top_fallers",
        "most_volatile"
    ],
)
def cur_tab(request):
    """Fixture"""
    print(f"\n\n\nCurrent tab - {request.param}")
    return request.param
