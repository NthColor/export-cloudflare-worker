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

# My Story on Making This Exportation
I am using Cloudflare Worker's Quick Editor without Wrangler to make API and Full Stack Apps. 
However, when I want to migrate to another workers, it does not work by Downloading the script. 
Thus, I made a Python Script to Download from it directly, and drag folders to another workers.
