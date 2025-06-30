import os
import re
from datetime import datetime
import requests

# ==== CONFIGURATION ====
account_id = "your_account_id"
script_name = "your_script_name"
bearer_token = "your_bearer_token"

url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{script_name}/content/v2"
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

# ==== Step 1: Fetch the script content ====
print("📡 Fetching script content...")
response = requests.get(url, headers=headers)

if not response.ok:
    raise Exception(f"Failed to fetch script content: {response.status_code} {response.text}")

content_type = response.headers.get("Content-Type", "")
boundary_match = re.search(r'boundary=([a-zA-Z0-9\'()+_,-./:=?]+)', content_type)
if not boundary_match:
    raise ValueError("Could not detect multipart boundary.")
boundary = boundary_match.group(1)

# ==== Step 2: Split by boundary ====
raw = response.text
parts = raw.split(f"--{boundary}")
parts = [p.strip() for p in parts if p.strip() and not p.strip().endswith("--")]

output_dir = f"output-script-{datetime.now().strftime('%d%m%Y-%H%M')}"
os.makedirs(output_dir, exist_ok=True)

# ==== Step 3: Save each file ====
for part in parts:
    # Split headers and body
    if "\r\n\r\n" in part:
        headers_part, body = part.split("\r\n\r\n", 1)
    elif "\n\n" in part:
        headers_part, body = part.split("\n\n", 1)
    else:
        continue

    # Parse headers
    headers = {}
    for line in headers_part.splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            headers[key.strip().lower()] = val.strip()

    disposition = headers.get("content-disposition", "")
    filename_match = re.search(r'name="([^"]+)"; filename="([^"]+)"', disposition)
    if not filename_match:
        continue

    file_path = filename_match.group(1)
    full_path = os.path.join(output_dir, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Save to file
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(body.strip())

    print(f"✅ Saved: {file_path}")

print(f"\n🎉 All files written to: {output_dir}")
