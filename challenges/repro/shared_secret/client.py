"""Thin HTTP client used by all partner tools."""

import requests

from config import PARTNER_API_KEY, PARTNER_API_URL


def call_partner(path: str, params: dict | None = None) -> dict:
    resp = requests.get(
        f"{PARTNER_API_URL}/{path}",
        params=params,
        headers={"X-Api-Key": PARTNER_API_KEY},
        timeout=10,
    )
    resp.raise_for_status()
    return resp.json()
