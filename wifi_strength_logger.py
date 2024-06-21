import subprocess
import re
import time

def get_wifi_signal(interface):
    try:
        cmd = f"awk 'NR==3 {{print \"WiFi Signal Strength = \" $3 \"00 %\"}}' /proc/net/wireless"
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode("utf-8")
        signal_strength = re.search(r"\d+", result).group()

        if int(signal_strength) >= 70:
            print("\033[92m" + result + "\033[0m", end='\r')  # Green for strong signal
        elif int(signal_strength) >= 50:
            print("\033[93m" + result + "\033[0m", end='\r')  # Yellow for moderate signal
        else:
            print("\033[91m" + result + "\033[0m", end='\r')  # Red for weak signal

    except subprocess.CalledProcessError:
        print("Error retrieving WiFi signal strength.", end='\r')

while True:
    get_wifi_signal("mlan0")
    time.sleep(1)  # Optional delay to avoid excessive updates

# Alternative: Run this cmd from Terminal: watch -n 1 "awk 'NR==3 {print \"WiFi Signal Strength = \" \$3 \"00 %\"}' /proc/net/wireless"
# ctrl + c -> Stop 