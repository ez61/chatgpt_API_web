tell application "Terminal"
	do script "python3 /PATH/TO/ui.py" without waiting
end tell

delay 3 -- wait for 3 seconds

tell application "System Events"
	set isRunning to (count of (every process whose name is "Safari")) > 0
end tell

if isRunning then
	tell application "Safari"
		activate
		tell window 1 to set current tab to (make new tab with properties {URL:"http://127.0.0.1:7860"})
	end tell
else
	tell application "Safari"
		activate
		open location "http://127.0.0.1:7860"
	end tell
end if
