import plistlib
import os

from datetime import datetime, timezone


file_path = os.path.expanduser(
    "~/Library/Preferences/com.codeweavers.CrossOver.plist"
)

with open(file_path, "rb") as file:
    data = plistlib.load(file)

# Set an ordinary date field to the current UTC time
data["FirstRunDate"] = datetime.now(timezone.utc)

# Save the plist
with open(file_path, "wb") as file:
    plistlib.dump(data, file)

print("Date updated successfully!")