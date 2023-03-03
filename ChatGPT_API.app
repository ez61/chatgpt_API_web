tell application "Terminal"
	do script "/PATH/TO/ui.py" without waiting
end tell

delay 3 -- wait for 3 seconds

tell application "Safari"
	activate
	tell window 1 to set current tab to (make new tab with properties {URL:"REPLACE THIS WITH YOUR LOCAL HOST URL"})
end tell
