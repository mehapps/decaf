import rumps, subprocess, signal

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
class MenuBarApp(rumps.App):
    def __init__(self):
        super(MenuBarApp, self).__init__("Caffeinate")
        self.menu = ["Forever", "Time", "Stop"]

    @rumps.clicked("Forever")
    def caffeinate(self, _):
        prevent_sleep(0)
    
    @rumps.clicked("Time")
    def time_based(self, _):
        self.title = "Title"

    @rumps.clicked("Stop")
    def stop(self, _):
        kill_caffeinate()

MenuBarApp().run()