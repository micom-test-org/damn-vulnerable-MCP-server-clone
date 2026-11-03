"""
Repro: shared hardcoded secret
Port: 9020

Every partner tool goes through client.call_partner, which sends the single
hardcoded PARTNER_API_KEY from config.py. apply_promo_code uses a separate
hardcoded DB password in promo/db.py.
"""

from mcp.server.fastmcp import FastMCP

from client import call_partner
from promo.db import find_promo

mcp = FastMCP("Repro - Shared Hardcoded Secret", host="0.0.0.0", port=9020)


@mcp.tool()
def search_flights(origin: str, destination: str, date: str) -> dict:
    """Search flights between two airports on a date."""
    return call_partner("flights", {"from": origin, "to": destination, "date": date})


@mcp.tool()
def get_booking(booking_id: str) -> dict:
    """Get a booking by id."""
    return call_partner(f"bookings/{booking_id}")


@mcp.tool()
def hold_offer(offer_id: str) -> dict:
    """Place a temporary hold on a fare offer."""
    return call_partner(f"offers/{offer_id}/hold")


@mcp.tool()
def get_seat_map(flight_id: str) -> dict:
    """Get the seat map for a flight."""
    return call_partner(f"flights/{flight_id}/seats")


@mcp.tool()
def get_loyalty_balance(member_id: str) -> dict:
    """Get a loyalty member's points balance."""
    return call_partner(f"loyalty/{member_id}")


@mcp.tool()
def get_flight_status(flight_id: str) -> dict:
    """Get the live status of a flight."""
    return call_partner(f"flights/{flight_id}/status")


@mcp.tool()
def apply_promo_code(code: str) -> dict:
    """Look up the discount for a promo code."""
    row = find_promo(code)
    return {"code": code, "discount": row[0] if row else None}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
