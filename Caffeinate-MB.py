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

class MenuBarApp(rumps.App):
    def __init__(self):
        super(MenuBarApp, self).__init__("Caffeinate")
        self.menu = ["Caffeinate", "Stop"]

    @rumps.clicked("Caffeinate")
    def caffeinate(self, _):
        prevent_sleep(0)
        print("0")

    @rumps.clicked("Stop")
    def stop(self, _):
        kill_caffeinate()
        print("1")

MenuBarApp().run()