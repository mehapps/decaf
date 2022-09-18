import rumps, subprocess, signal, sys, datetime
if 'darwin' not in sys.platform:
    sys.exit("This program only runs on computers running macOS.")

clock_icon = "/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/Clock.icns"

def prevent_sleep(length):
    global caffeinate
    if length == 0:
        caffeinate = subprocess.Popen("caffeinate")
        rumps.notification("Decaf", "―", "Keeping your Mac awake forever!", sound=True, icon = clock_icon)
    else:
        command = "caffeinate -t" + str(length)
        caffeinate = subprocess.Popen(command, shell = True)
        hms = str(datetime.timedelta(seconds=length))
        notification_text = "Not sleeping for " + hms + "!"
        rumps.notification("Decaf", "―", notification_text, sound=True, icon = clock_icon)

def kill_caffeinate():
    caffeinate.send_signal(signal.SIGINT)
    rumps.notification("Decaf", "―", "Your Mac can sleep now!", sound=True, icon=clock_icon)

@rumps.clicked("Forever")
def about(sender):
    prevent_sleep(0)

@rumps.clicked("Time")
def about(sender):
    window = rumps.Window("Please enter the time to sleep.", "Time Input", dimensions=(200,25))
    window.title = 'Time Input'
    window.message = 'Please enter the time to sleep.'
    window.default_text = '00:00:00'
    window.icon = clock_icon
    response = window.run()
    time = str(response.text).split(':')
    seconds = ((int(time[0])) * 3600) + ((int(time[1]))*60) + (int(time[2]))
    prevent_sleep(seconds)


@rumps.clicked("Stop")
def about(sender):
    kill_caffeinate()

app = rumps.App("Caffeinater", title='', icon=clock_icon)
app.run()