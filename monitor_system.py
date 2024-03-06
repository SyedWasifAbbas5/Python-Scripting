#!/usr/bin/python

import psutil
import time

def monitor_system(interval=1):
    while True:
        # CPU Usage
        cpu_percent = psutil.cpu_percent(interval=interval)
        print(f"CPU Usage: {cpu_percent}%")

        # Memory Usage
        mem = psutil.virtual_memory()
        print(f"Memory Usage: {mem.percent}%")

        # Disk Usage
        disk = psutil.disk_usage('/')
        print(f"Disk Usage: {disk.percent}%")

        # Network Usage
        net = psutil.net_io_counters()
        print(f"Network Usage (bytes sent/received): {net.bytes_sent}/{net.bytes_recv}")

        # Sensor Temperature (if available)
        try:
            temps = psutil.sensors_temperatures()
            for name, entries in temps.items():
                for entry in entries:
                    print(f"{name} Temperature ({entry.label}): {entry.current}°C")
        except AttributeError:
            print("Sensor temperature information not available on this system.")

        time.sleep(interval)

if __name__ == "__main__":
    monitor_system()