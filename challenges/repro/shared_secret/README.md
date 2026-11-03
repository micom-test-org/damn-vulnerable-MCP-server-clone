# Repro: shared hardcoded secret across MCP tools

One MCP server (port 9020) whose tools all call the same partner API through
`config.py`, which hardcodes a single API key. A separate tool uses a hardcoded
DB password in `promo/db.py`.

Expected posture gaps: 2 (one per secret, MCP server as affected entity),
not one gap per tool. All values are fake test data.
