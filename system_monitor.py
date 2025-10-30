import psutil
import time
import os
import json
from datetime import datetime
import subprocess   

def check_system_stats():
    """Get Current System Performance Stats"""
    stats = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'cpu_%': psutil.cpu_percent(interval=1),
        'memory_%': psutil.virtual_memory()._asdict(),
        'disk_%': psutil.disk_usage('C:\\')._asdict(),
        'network': psutil.net_io_counters()._asdict(),
        'processes': len(psutil.pids())
    }

    return stats

def check_alerts(stats):
    """Check for any alerts """
    alerts =[]

    if stats['cpu_%'] > 80:
        alerts.append(f"High Cpu Usage: {stats['cpu_%']}%")

    if stats['memory_%']['percent'] > 80:
        alerts.append(f"High Memory Usage: {stats['memory_%']['percent']}%")   

    if stats['disk_%']['percent'] > 90:
        alerts.append(f"Low Disk Space: {stats['disk_%']['percent']}% used")

    return alerts       

def monitor_system():
    """Main monitoring function with updates"""

    print("Starting the monitor")
    print("Press ctrl+c to stop")

    try:
        while True:
            os.system ('cls')

            stats = check_system_stats()
            alerts = check_alerts(stats)

            print("SYSTEM PERFORMANCE MONITOR")
            print(f"Time: {stats['timestamp']}")
            print(f"cpu usage: {stats['cpu_%']}%")
            print(f"memory usage: {stats['memory_%']['percent']}%")
            print(f"disk usage: {stats['disk_%']['percent']}%")
            print(f"running processes: {stats['processes']}")

            print("\n=== Alerts ===")
            if alerts:
                for alert in alerts:
                    print(f"Warning: {alert}")
            else:
                print("All systems normal")

            print(f"\n refreshing in 5 sec")
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nMonitor stopped")

if __name__ == "__main__":
    monitor_system()