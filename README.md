Convert plist to xml readable file 

❯ plutil -convert xml1 ~/Library/Preferences/com.codeweavers.CrossOver.plist 


Create the LaunchAgent file


mkdir -p ~/Library/LaunchAgents

nano ~/Library/LaunchAgents/com.example.daily-task.plist

Paste to xml file in XML folder

Enable service

plutil -lint ~/Library/LaunchAgents/com.example.updateDate.plist

launchctl bootstrap gui/$(id -u) \
  ~/Library/LaunchAgents/com.example.updateDate.plist

  


