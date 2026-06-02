# clariBI MCP Server

[![PyPI](https://img.shields.io/pypi/v/claribi-mcp.svg)](https://pypi.org/project/claribi-mcp/)
[![npm](https://img.shields.io/npm/v/@claribicom/mcp.svg)](https://www.npmjs.com/package/@claribicom/mcp)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-com.claribi%2Fmcp--server-blue)](https://registry.modelcontextprotocol.io/v0.1/servers?search=com.claribi)

Public reference for the **clariBI** Model Context Protocol server, a
hosted MCP endpoint that lets LLM clients sign users up, upload data,
connect cloud sources via OAuth, run natural-language analyses, and
generate reports.

This repo holds the public manifest, examples, and reference
documentation. The clariBI platform itself is a commercial hosted
service; the hosted MCP endpoint is documented here so any
spec-compliant MCP client can connect.

## Endpoint

| Transport | URL | Protocol version |
| --- | --- | --- |
| Streamable HTTP | `https://claribi.com/mcp/v1/` | 2025-03-26 |
| SSE (legacy) | `https://claribi.com/mcp/v1/sse` | 2024-11-05 |

## Authentication

OAuth 2.1 with Dynamic Client Registration (RFC 7591). Discovery
endpoints:

- Authorization Server Metadata (RFC 8414): `https://claribi.com/mcp/v1/.well-known/oauth-authorization-server`
- Protected Resource Metadata (RFC 9728): `https://claribi.com/mcp/v1/.well-known/oauth-protected-resource`

Public clients use PKCE S256. Confidential clients receive a client
secret on registration.

Alternative for single-user installations: bearer token
`Authorization: Bearer claribi_mcp_<key>`. Mint a key inside the
clariBI web app under Settings > Developer > MCP Server.

## Surface

19 tools, 3 resources, 2 prompts. Tool names and JSON schemas are
published live at the tool catalog endpoint:

```bash
curl https://claribi.com/mcp/v1/  # returns server metadata
curl https://claribi.com/api/mcp-server/tool-catalog/  # full catalog
```

Tools include `register_account`, `verify_email`, `check_pricing`
(all unauthenticated for sign-up from chat), `upload_data_source`,
`ingest_url_data_source`, `request_oauth_integration_url`,
`run_analysis`, `generate_report`, `get_usage`, `get_billing_status`,
`create_checkout_session`, and dashboard/report list/get tools.

## Official SDKs

Both SDKs are MIT-licensed and codegen-driven from the live tool
catalog so the typed method surface never drifts from the server.

### Python

```bash
pip install claribi-mcp
```

```python
from claribi_mcp import Client

with Client(api_key="claribi_mcp_...") as client:
    client.initialize()
    result = client.run_analysis(
        question="What was revenue by region last quarter?",
        wait_seconds=30,
    )
    print(result.text)
```

Source on PyPI: <https://pypi.org/project/claribi-mcp/>

### TypeScript

```bash
npm install @claribicom/mcp
```

```ts
import { Client } from '@claribicom/mcp';

const client = new Client({ apiKey: 'claribi_mcp_...' });
await client.initialize();
const r = await client.callTool('run_analysis', {
  question: 'What was revenue by region last quarter?',
  wait_seconds: 30,
});
console.log(r.text());
```

Source on npm: <https://www.npmjs.com/package/@claribicom/mcp>

## MCP Server Registry

Listed in the official Model Context Protocol Server Registry under
the namespace `com.claribi/mcp-server`:

```bash
curl 'https://registry.modelcontextprotocol.io/v0.1/servers?search=com.claribi'
```

Manifest: [`server.json`](server.json).

## Pricing and tier gating

MCP Server access is gated by the `mcp_server_access` feature flag on
the clariBI subscription. It ships with Trial (free, 14 days),
Starter ($99/mo), Professional ($199/mo), and Enterprise ($999/mo).
Excluded from Free and Lite. Tool error responses indicate which
quota was hit.

Sign-up tools (`register_account`, `verify_email`, `check_pricing`)
do not require a subscription, so a new user can provision a Trial
workspace from inside their LLM client without any prior account.

## Documentation

- Overview: <https://claribi.com/docs/mcp/overview>
- Connecting from Claude Desktop: <https://claribi.com/knowledge-base/mcp-connect-claude-desktop/>
- Connecting from Cursor: <https://claribi.com/knowledge-base/mcp-connect-cursor/>
- Sign-up via LLM walkthrough: <https://claribi.com/knowledge-base/mcp-signup-via-llm/>
- API reference: <https://claribi.com/knowledge-base/mcp-api-reference/>

## Security

Vulnerability disclosure: `security@claribi.com`. See [SECURITY.md](SECURITY.md).

## License

This repository (README, manifest, examples, SDK code) is MIT.

The hosted clariBI platform that the server fronts is a commercial
service; using the MCP server endpoint requires a clariBI account.
