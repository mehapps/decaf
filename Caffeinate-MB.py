import rumps, subprocess, signal, sys, os

if 'darwin' not in sys.platform:
    sys.exit("This program only runs on computers running macOS.")

def prevent_sleep(length):
    global caffeinate
    if length == 0:
        caffeinate = subprocess.Popen("caffeinate")
    else:
        command = "caffeinate -t " + length
        caffeinate = subprocess.Popen(command)

def kill_caffeinate():
    caffeinate.send_signal(signal.SIGINT)

rumps.debug_mode(True)
@rumps.clicked("Forever")
def about(sender):
    prevent_sleep(0)

@rumps.clicked("Stop")
def about(sender):
    kill_caffeinate()

app = rumps.App("Caffeinater", title='Caffeinate')
app.run()