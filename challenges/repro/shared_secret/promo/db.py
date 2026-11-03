"""Promo code storage."""

import psycopg2

DB_HOST = "promo-db.internal.example.com"
DB_USER = "promo_admin"
DB_PASSWORD = "Pr0mo-Adm1n-Pa55w0rd-2024!"


def find_promo(code: str):
    conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, dbname="promo")
    with conn, conn.cursor() as cur:
        cur.execute("SELECT discount FROM promo_codes WHERE code = %s", (code,))
        return cur.fetchone()
