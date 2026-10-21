from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

AUTH_FILE = PROJECT_DIR / "data" / "auth.log"
ACCESS_FILE = PROJECT_DIR / "data" / "access.log"
FIREWALL_FILE = PROJECT_DIR / "data" / "firewall.log"
IOC_FILE = PROJECT_DIR / "data" / "suspicious_ips.txt"

OUTPUT_DIR = PROJECT_DIR / "output"
REPORT_FILE = OUTPUT_DIR / "security_report.txt"


with open(AUTH_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

failed_logins = 0
ip_counts = {}
invalid_lines = 0

for line_number, line in enumerate(lines, start=1):
    if "src=" not in line:
        invalid_lines += 1
        print("Rad", line_number, "saknar käll-IP:", line.strip())
        continue

    ip_parts = line.split("src=")[1].split()

    if not ip_parts:
        invalid_lines += 1
        print("Rad", line_number, "har tom käll-IP:", line.strip())
        continue

    if "Failed login" in line:
        failed_logins += 1
        ip = ip_parts[0]

        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

print("\nAUTENTISERINGSANALYS")
print("Antal loggrader:", len(lines))
print("Misslyckade inloggningar:", failed_logins)

for ip in sorted(ip_counts):
    print(ip, ":", ip_counts[ip])

print("Rader med felaktig käll-IP:", invalid_lines)
