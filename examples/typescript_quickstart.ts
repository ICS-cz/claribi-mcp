/**
 * Sign up a new user and run an analysis from the clariBI MCP server.
 *
 * Run: `npm install @claribicom/mcp && tsx typescript_quickstart.ts`.
 */
import { Client } from '@claribicom/mcp';

async function main(): Promise<void> {
  // check_pricing is unauthenticated.
  const client = new Client({});
  await client.initialize();

  const pricing = await client.callTool('check_pricing', {});
  const tiers = pricing.structured?.tiers ?? [];
  console.log('Available tiers:');
  for (const t of tiers) {
    console.log(`  - ${t.name}: $${t.price_monthly_usd}/mo`);
  }

  // Real signup would continue here; left as a comment so the example
  // is safe to run without sending an email:
  //
  // const pending = (await client.callTool('register_account', {
  //   email: 'you@example.com',
  //   organization_name: 'Acme',
  //   accept_terms: true,
  // })).structured;
  // const code = '...'; // pasted from the email
  // const auth = (await client.callTool('verify_email', {
  //   pending_id: pending.pending_id,
  //   code,
  //   password: 'strong-password',
  // })).structured;
  //
  // // Reconnect with the new API key.
  // const authed = new Client({ apiKey: auth.api_key });
  // await authed.initialize();
  // const r = await authed.callTool('run_analysis', {
  //   question: 'What was total revenue by region?',
  //   wait_seconds: 30,
  // });
  // console.log(r.text());
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
