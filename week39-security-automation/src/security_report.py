
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


suspicious_ips = set()

with open(IOC_FILE, "r", encoding="utf-8") as file:
    for line in file:
        ip = line.strip()

        if ip:
            suspicious_ips.add(ip)

ioc_matches = []

for ip in sorted(ip_counts):
    if ip in suspicious_ips:
        ioc_matches.append(ip)

print("\nIOC-MATCHNINGAR")

for ip in ioc_matches:
    print(ip, "- MATCHNING")


with open(ACCESS_FILE, "r", encoding="utf-8") as file:
    access_lines = file.readlines()

status_counts = {}
access_ips = set()

for line in access_lines:
    if "src=" in line:
        ip_parts = line.split("src=")[1].split()

        if ip_parts:
            access_ips.add(ip_parts[0])

    if "status=" in line:
        status_parts = line.split("status=")[1].split()

        if status_parts:
            status = status_parts[0]

            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

print("\nWEBBANALYS")
print("Antal loggrader:", len(access_lines))

for status in sorted(status_counts):
    print("HTTP", status, ":", status_counts[status])


with open(FIREWALL_FILE, "r", encoding="utf-8") as file:
    firewall_lines = file.readlines()

denied_connections = 0
firewall_ips = set()

for line in firewall_lines:
    if "src=" in line:
        ip_parts = line.split("src=")[1].split()

        if ip_parts:
            firewall_ips.add(ip_parts[0])

    if "DENY" in line.split():
        denied_connections += 1

print("\nBRANDVÄGGSANALYS")
print("Antal loggrader:", len(firewall_lines))
print("Nekade anslutningar:", denied_connections)


correlations = {}

print("\nKORRELATION MELLAN LOGGFILER")

for ip in sorted(ip_counts):
    sources = ["auth.log"]

    if ip in access_ips:
        sources.append("access.log")

    if ip in firewall_ips:
        sources.append("firewall.log")

    correlations[ip] = sources

    print(ip, "förekommer i:", ", ".join(sources))

    if ip in suspicious_ips:
        print("IOC-matchning:", ip)


OUTPUT_DIR.mkdir(exist_ok=True)

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.write("SECURITY AUTOMATION REPORT\n")
    file.write("==========================\n")
    file.write("Dataset: A - Basic\n\n")

    file.write("AUTENTISERINGSANALYS\n")
    file.write(f"Antal loggrader: {len(lines)}\n")
    file.write(f"Misslyckade inloggningar: {failed_logins}\n")

    for ip in sorted(ip_counts):
        file.write(f"{ip}: {ip_counts[ip]}\n")

    file.write("\nIOC-MATCHNINGAR\n")

    for ip in ioc_matches:
        file.write(f"{ip}: MATCHNING\n")

    file.write("\nWEBBANALYS\n")
    file.write(f"Antal loggrader: {len(access_lines)}\n")

    for status in sorted(status_counts):
        file.write(f"HTTP {status}: {status_counts[status]}\n")

    file.write("\nBRANDVÄGGSANALYS\n")
    file.write(f"Antal loggrader: {len(firewall_lines)}\n")
    file.write(f"Nekade anslutningar: {denied_connections}\n")

    file.write("\nKORRELATION MELLAN LOGGFILER\n")

    for ip in sorted(correlations):
        sources = correlations[ip]
        file.write(f"{ip}: {', '.join(sources)}\n")

        if ip in suspicious_ips:
            file.write(f"IOC-matchning: {ip}\n")

    file.write("\nDATAKVALITET\n")
    file.write(f"Rader med felaktig käll-IP: {invalid_lines}\n")

    file.write("\nOBSERVATION\n")

    if ioc_matches:
        file.write(
            f"Antal IP-adresser med IOC-matchning: {len(ioc_matches)}\n"
        )
    else:
        file.write("Inga IOC-matchningar hittades.\n")

    for ip in sorted(correlations):
        sources = correlations[ip]

        if len(sources) > 1:
            file.write(
                f"{ip} förekommer i {len(sources)} loggkällor: "
                f"{', '.join(sources)}.\n"
            )

    file.write("\nBEGRÄNSNING\n")
    file.write(
        "En IOC-matchning eller förekomst i flera loggar "
        "bevisar inte att en IP-adress tillhör en angripare.\n"
    )

print("\nRapport skapad:", REPORT_FILE)
