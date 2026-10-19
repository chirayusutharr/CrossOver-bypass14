

### 1. Convert plist to XML
```bash
plutil -convert xml1 ~/Library/Preferences/com.codeweavers.CrossOver.plist
```

### 2. Create LaunchAgent
```bash
mkdir -p ~/Library/LaunchAgents
nano ~/Library/LaunchAgents/com.example.updateDate.plist
```
Paste your XML configuration and save.

### 3. Validate the plist
```bash
plutil -lint ~/Library/LaunchAgents/com.example.updateDate.plist
```

### 4. Enable the service
```bash
launchctl bootstrap gui/$(id -u) \
~/Library/LaunchAgents/com.example.updateDate.plist
```

### 5. Stop the service
```bash
launchctl bootout gui/$(id -u)/com.example.updateDate
```

**Note:** The `Label` inside the plist must match `com.example.updateDate`. Configure the correct script path and schedule in the XML.
