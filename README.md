# Export Snippets from Cloudflare Workers
Turn Cloudflare Worker Snippets into Local Folder

# Configuration
1. Get Cloudflare Account ID
(Found on Your Cloudflare URL or Account -> Tripe Dots -> Copy Account ID)
2. Get Cloudflare Worker Name
(Exact name of worker)
3. Get Cloudflare API Token
(Manage Accounts -> Account Api Tokens -> Create Custom Token -> Permissions: Worker Scripts - Read)
4. Insert on main.py's CONFIGURATION

# Run
python main.py

# Output
Folder: output-script-ddmmyyyy-HM

# Cloudflare API
https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/content/
