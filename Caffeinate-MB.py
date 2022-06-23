import rumps, os, subprocess, signal, time

def prevent_sleep(length):
    global caffeinate
    if length == 0:
        caffeinate = subprocess.Popen("caffeinate")
    else:
        command = "caffeinate -t " + length
        caffeinate = subprocess.Popen(command)

prevent_sleep(0)
time.sleep(5)
caffeinate.send_signal(signal.SIGINT)