tell application "Terminal"
	do script "python3 /PATH/TO/ui.py" without waiting
end tell

delay 3 -- wait for 3 seconds

tell application "System Events"
	set isRunning to (count of (every process whose name is "Google Chrome")) > 0
end tell

if isRunning then
	tell application "Google Chrome"
		activate
		if (count of windows) > 0 then
			tell window 1 to make new tab with properties {URL:"http://127.0.0.1:7860"}
		else
			open location "http://127.0.0.1:7860"
		end if
	end tell
else
	tell application "Google Chrome"
		activate
		open location "http://127.0.0.1:7860"
	end tell
end if
