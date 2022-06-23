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

