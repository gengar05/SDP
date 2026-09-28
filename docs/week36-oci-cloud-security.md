1. Min OCI-miljö
  Tenancy (N/A): naimaromlin
  Compartment (Endast OCI): naimaromlin (root)
  Region (Endast OCI): eu-stockholm-1
  Availability Domain (Endast OCI): AD-1
  VM-namn/hostnamn/WSL-maskinnamn: itsx26-v36-naima
  Operativsystem: Ubuntu Linux
  Shape (Hårdvara, gäller alla): VM.Standard.E2.1.Micro
  Inloggningsmetod: SSH

2. Linux-kommandon (| Kommando | Vad visar det? | CIA-koppling |)
    whoami
   - Det visar vilken användare som är inloggad. Resulatatet var ubuntu.
   - Kopplas till konfidentialitet eftersom det visar vilken identitet som används

  hostname
  - Visar serverns namn och resultatet var itsx26-v36-naima
  - Kopplas till integritet och hjälper att identifiera rätt system

  pwd
  - Visar vilken katalog jag är i och resultatet var /home/ubuntu
  - Kopplas också till integritet och visar vart man befinner sig i filsystemet

  uname -a 
  - Information om Linux systemet och kernel. Det körde Ubuntu Linux på x86_64 med kernel 7.0.0-1009-oracle
  - Kopplas också till integritet och ger info angående systemets konfiguration

  uptime 
  - Hur länge systemet har varit igång samt systemets belastning. När jag körde det hade systemet varit iång i 30 min
  - Tillgängliget då den visar när systemet är igång och belastning


3. Hardening 
   Kontroll - Behörighet och identitet
   Risk - Fel användare kan få för mycket åtkomst
   Vad gjorde jag - Kontrollerade användare med whoami, id och groups
   Hur verifierade jag? - När jag kontrollerade såg jag att användare var ubuntu och att användare hade sudo behörighet
   CIA - Konfidentialitet

   Kontroll - Filrättigheter 
   Risk - Andra användare har tillgång till filer
   Vad gjorde jag - ag skapade filen med touch test.txt. Sedan använde jag ls -l test.txt för att se rättigheterna. Efter körde jag chmod 600 test.txt för att begränsa åtkomsten
   Hur verifierade jag? - Först visade ls -l test.txt -rw-rw-r--. Efter chmod 600 visade det -rw-------. Det betyder att bara användaren ubuntu kan läsa och skriva filen
   CIA - Konfidentialitet

   Kontroll - Systenuppdateringar
   Risk -  Gamla paket kan ha buggar eller säkerhetsproblem
   Vad gjorde jag - Körde sudo apt update för att updatera paketinformationen och sen apt list --upgradable för se vilka som kunde uppdateras
   Hur verifierade jag? - sudo apt update visade att 130 paket kunde uppgraderas, apt list --upgradable visade listan över paketen 
   CIA - Integritet

   Kontroll - Processer 
   Risk - Okänd eller oväntad process kan påverka systemet 
   Vad gjorde jag - Körde ps aux | head. ps aux visar processer som körs och head visar början av listan så att resultatet blir kortare
   Hur verifierade jag? - Fick en lista med processerna, där kunde jag se processer som kördes av root, exempelvis systemd
   CIA - Integritet

   Kontroll - Loggar
   Risk - Ifall något går fel kan det vara svårt att förstå problemet om man inte har loggar 
   Vad gjorde jag - Körde journalctl -n 20. journalctl visar systemets loggar och -n 20 betyder att de senaste 20 loggarna visas
   Hur verifierade jag? - Fick de 20 senaste loggmeddelandena och kunde se så de gick att läsa 
   CIA - Tillgänglighet

4. Recovery-plan
   1 Vad kan gå fel?
   Exempel på vad som kan gå fel är att SSH sluta fungerar, nätverket kan ha problem eller att ett systemfel har uppstått.
   
   2 Hur upptäcker jag problemet?
   Jag hade upptäckt problemet om SSH inte kan ansluta till VM, dessutom kan jag kontrollera status av mitt VM i OCI
   
   3 Vad kontrollerar jag först?
   Jag kontrollerar att
   VM status Running i OCI
   Vm har korrekt public IP
   Att jag använt rätt användarnamn och SSH-nyckel
   Letar efter felmeddelande eller loggar
   
   4 Hur återställer jag åtkomst?
   Kontrollerar VM och nätverksinställningarna i OCI. Går det att lösa problemet i OCI gör jag det och testar SSH igen. Skulle det inte gå att återställa skulle jag behöva göra om min miljö utifrån min dokumentation och inställningar jag använde mig av när jag skapade VM
   
  5 När behöver jag hjälp
  Jag skulle behöva hjälp om jag inte kan inte orsaken till problemet, eftersom då kan jag förlora viktig information.

5 Backup
Vad har jag sparat?
Min labbrapport i GitHub

Vad finns i GitHub?
Min dokumentation av labben

Vad kan jag återskapa?
Jag kan skapa en ny OCI VM, SSH anslutning, linux kommandon och hardening stegen ifall min VM hade försvunnit

Vad förloaras om VM försvinner?
Filer som har skapats i VM kan försvinna

Varför är backup viktigt?
Backup är viktigt eftersom det gör att man kan ha kvar viktig information även om min VM skulle försvinna

6 Cleanup
VM 
Jag stoppade min VM därefter terminerade jag den

Disk
Kontrollerade VM Boot Volume, där var 50 GB attached till VM, när jag terminated jag även bort Boot Volume så den inte ligger kvar

Backups
Jag kontrollerade Boot Volume Backups och det fanns inga backups att ta bort

Public IP
Min VM hade en Ephemeral Public IP, detta innebär at den är kopplad till min VM och behöver inte ta bort den separat

GitHub
Dokumentationen ligger sparad i docs/week36-oci-cloud-security.md
Den är inte kopplad til OCI och inget händer med den närjag terminated min OCI

7 CIA-reflektion
Konfidentialitet
Det handlar om att rätt personer har åtkomst till informationen. Labben innehåll arbete om användare, grupper och filrättigheter. I labben använde jag chmod 600 på test.txt som gjorde att endast ubntu kunde läsa eler skriva filen.

Integritet
Handlar om information och system ska vara korrekta och inte kunnas ändras av fel personer. Jag kontrollerade systemet, processer och uppdateringar med linux kommandon.

Tillgänglighet
Handlar om att systemet ska fungera när det behövs. Jag använde uptime för att kontrollera att min VM var igång samt journalctl för att kunna se loggar. 

8 Reflektion
Vad fungerade bra?
Jag tyckte det fungerade bra att skapa en VM i OCI och kunna ansluta den med SSH. Det var smidigt att köra olika Linux kommandon och använde de för att kunna se information om användare, filsystem samt systemets status. 

Vad var svårt? 
Jag tyckte det var svårt att få igång självaste arbetsmijön då det krånglade för mig i början. Efter arbetsmijön var igång hade jag lite svårigheter emellan åt att veta vad kommandon gjorde men ju mer jag läste på och gjorde det praktiskt ju mer logiskt blev det. Dessutom var det svårt med vilka resurser jag skulle kontrollera innan cleanup, ifall man missade något.

Vad lärde jag mig?
Jag har lärt mig hur man skapar samt använder en Linux VM i OCI. Jag fick lära mig några nya Linux kommandon då det var ett bra tag sen jag senast höll på med detta. Jag fick dessutom mer kunskap inom säkerhet då det är så mycket mer än bara ett lösenord det är användarbehörighet, uppdateringar, processer, loggar och varför backup och recovery är så viktigt. Samt att cleanup är en viktig del av en molnbaserad labb eftersom resurserna kan finnas kvar efteråt.
