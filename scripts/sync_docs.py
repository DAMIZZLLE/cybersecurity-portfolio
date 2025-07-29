import os
import json
import gspread
from google.oauth2.service_account import Credentials
from markdownify import markdownify as md

# Set up credentials
creds_json = json.loads(open("key.json").read())
creds = Credentials.from_service_account_info(
    creds_json,
    scopes=["https://www.googleapis.com/auth/documents.readonly"]
)

gc = gspread.authorize(creds)

# === CONFIG ===
DOCS_TO_SYNC = {
    # Format: "Google Doc Title": "Relative output path in repo"
    "Cisco - Introduction to Cybersecurity": "Cisco/introduction-to-cybersecurity.md",
    # Add more docs here if needed
}

# === MAIN ===
for title, path in DOCS_TO_SYNC.items():
    doc = gc.open(title).sheet1
    content = "\n".join(["# " + row[0] if i == 0 else row[0] for i, row in enumerate(doc.get_all_values())])
    markdown = md(content)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown)

print("✅ Docs synced successfully.")
