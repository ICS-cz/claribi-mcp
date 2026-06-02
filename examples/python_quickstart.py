"""Sign up a new user and run an analysis from the clariBI MCP server.

This script exercises the full happy-path flow:
  1. register_account + verify_email to create a Trial workspace.
  2. upload_data_source to ingest a CSV.
  3. run_analysis against the uploaded data.

Run: `pip install claribi-mcp && python python_quickstart.py`.
"""
from __future__ import annotations

import base64
from pathlib import Path

from claribi_mcp import Client


def main() -> None:
    # The first two tools are unauthenticated. No API key needed yet.
    client = Client()
    client.initialize()

    print("Available tiers:")
    for tier in client.check_pricing().structured.get("tiers", []):
        print(f"  - {tier['name']}: ${tier['price_monthly_usd']}/mo")

    # Real registration would happen here. For a CI smoke test, stop
    # before sending an email.
    #
    # pending = client.register_account(
    #     email="you@example.com",
    #     organization_name="Acme",
    #     accept_terms=True,
    # ).structured
    # code = input("Enter the code emailed to you: ")
    # auth = client.verify_email(
    #     pending_id=pending["pending_id"],
    #     code=code,
    #     password="strong-password-here",
    # ).structured
    # api_key = auth["api_key"]
    #
    # # Reconnect with the new API key for authenticated tools.
    # client.close()
    # client = Client(api_key=api_key)
    # client.initialize()
    #
    # csv_bytes = Path("sales.csv").read_bytes()
    # client.upload_data_source(
    #     name="Q3 sales",
    #     format="csv",
    #     data_base64=base64.b64encode(csv_bytes).decode(),
    #     wait_seconds=30,
    # )
    #
    # result = client.run_analysis(
    #     question="What was total revenue by region?",
    #     wait_seconds=30,
    # )
    # print(result.text)


if __name__ == "__main__":
    main()
