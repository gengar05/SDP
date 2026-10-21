
# Säkerhetsanalys – Dataset A

## 1. Rådata

Jag genomförde analysen med Dataset A (Basic), som innehåller syntetiska säkerhetsloggar. Syftet var att undersöka hur Python kan användas för att automatisera analysen av flera olika loggkällor.

### Filer som användes

- **data/auth.log**  
  6 loggrader med information om lyckade och misslyckade inloggningar.

- **data/access.log**  
  4 loggrader med HTTP-förfrågningar och statuskoder.

- **data/firewall.log**  
  3 loggrader med brandväggshändelser.

- **data/suspicious_ips.txt**  
  3 IP-adresser som användes som IOC (Indicators of Compromise).

Totalt analyserades 13 loggrader från 3 loggfiler.

Alla logghändelser i datasetet är från den 24 september 2026.

### Exempel från autentiseringsloggen

`2026-09-24T08:15:03Z auth Failed login user=admin src=203.0.113.15`

Raden visar ett misslyckat inloggningsförsök för användaren `admin` från käll-IP-adressen `203.0.113.15`.

### Exempel från webbloggen

`2026-09-24T08:21:02Z src=203.0.113.15 method=GET path=/login status=401`

Raden visar en HTTP-förfrågan till `/login` som resulterade i statuskoden 401.

### Exempel från brandväggsloggen

`2026-09-24T08:16:22Z DENY src=203.0.113.15 dst=10.0.0.10 port=22`

Raden visar att brandväggen nekade en anslutning från samma käll-IP-adress till port 22.

Genom att analysera dessa loggar kan programmet undersöka om samma IP-adress förekommer i flera olika typer av säkerhetshändelser.

## 2. Observation

Programmet gav följande resultat:

### Authentication

Av 6 loggrader i `auth.log` innehöll 4 misslyckade inloggningar.

- `203.0.113.15` hade 3 misslyckade inloggningar.
- `198.51.100.44` hade 1 misslyckad inloggning.

Programmet upptäckte dessutom 1 felaktig loggrad som saknade käll-IP-adress.

### Web traffic

I `access.log` identifierades:

- 1 HTTP 200
- 2 HTTP 401
- 1 HTTP 404

Båda HTTP 401-svaren kom från `203.0.113.15` och gällde `/login`.

IP-adressen `198.51.100.44` gjorde en HTTP-förfrågan till `/admin` som gav statuskoden HTTP 404.

### Firewall

I `firewall.log` fanns totalt 3 loggrader.

Programmet räknade 1 händelse med åtgärden `DENY`. Den var kopplad till IP-adressen `203.0.113.15` och port 22.

Det fanns dessutom en `DROP`-händelse från `203.0.113.99`, men programmets räknare för nekade anslutningar omfattar endast `DENY`.

### IOC matches

Programmet hittade två IOC-träffar bland IP-adresserna med misslyckade inloggningsförsök:

- `203.0.113.15`
- `198.51.100.44`

### Korrelation mellan loggkällor

Programmet visar att `203.0.113.15` förekom i alla 3 loggkällor.

IP-adressen `198.51.100.44` förekom i 2 loggkällor: `auth.log` och `access.log`.

Detta innebär att flera säkerhetshändelser kan kopplas till samma käll-IP-adress.


### Evidens från loggfilerna

För att kunna kontrollera observationerna jämförde jag resultaten med originalfilerna i Dataset A.

#### Misslyckade inloggningar:

- `auth.log`, rad 1–3: Tre misslyckade inloggningar från `203.0.113.15`.
- `auth.log`, rad 5: En misslyckad inloggning från `198.51.100.44`.
- `auth.log`, rad 6: En felaktig loggrad som saknar käll-IP-adress.

Det ger totalt 4 misslyckade inloggningar och 1 felaktig loggrad.

#### Webbhändelser:

- `access.log`, rad 1: HTTP 401 från `203.0.113.15`.
- `access.log`, rad 3: HTTP 401 från `203.0.113.15`.
- `access.log`, rad 4: HTTP 404 från `198.51.100.44`.

#### Brandväggshändelser:

- `firewall.log`, rad 2: DENY från `203.0.113.15` till port 22.
- `firewall.log`, rad 3: DROP från `203.0.113.99` till port 3389.

Programmet räknar bara DENY i sin DENY-räknare. DROP-händelsen finns i rådata men ingår inte i det resultatet.

#### IOC-listan:

- `suspicious_ips.txt`, rad 1: `203.0.113.15`.
- `suspicious_ips.txt`, rad 2: `198.51.100.44`.
- `suspicious_ips.txt`, rad 3: `203.0.113.99`.

Båda IP-adresserna med misslyckade inloggningar finns i IOC-listan.

Evidensen visar att `203.0.113.15` förekommer i tre olika loggkällor. Det gör adressen relevant för vidare analys, men är inte ett bevis på att ett intrång har skett.


## 3. Slutsats

Utifrån observationerna går det att dra slutsatsen att `203.0.113.15` är den IP-adress som bör prioriteras för vidare undersökning.

Adressen förekommer vid 3 misslyckade inloggningsförsök, 2 HTTP 401-svar och 1 nekad brandväggsanslutning. Den finns dessutom i IOC-listan.

Eftersom IP-adressen förekommer i flera olika händelser är den mer intressant att granska än om den bara hade förekommit i en enskild loggrad.

Även `198.51.100.44` är relevant eftersom adressen förekommer i 2 loggkällor och matchar IOC-listan.

En begränsad slutsats är att IP-adresserna är relevanta för fortsatt säkerhetsanalys. Resultatet bevisar däremot inte att adresserna tillhör angripare eller att ett intrång har genomförts.

## 4. Osäkerhet

Det finns flera begränsningar i både datasetet och programmet.

Datasetet innehåller endast 13 loggrader. Det är ett väldigt litet underlag och ger inte en fullständig bild av aktiviteterna i ett verkligt nätverk.

Loggarna visar vad som registrerades, men inte avsikten bakom händelserna. Programmet kan identifiera misslyckade inloggningsförsök, men inte avgöra varför de misslyckades.

En IOC-träff är inte heller ett bevis på att en IP-adress är skadlig. IOC-listan kan innehålla uppgifter som behöver verifieras.

Programmet jämför IP-adresser mellan loggkällorna, men kontrollerar inte om händelserna ligger tillräckligt nära varandra i tid för att säkert kunna kopplas samman.

Programmet utför inte heller en fullständig validering av IP-adresser. Det kontrollerar vissa saknade eller tomma `src`-fält, men kan inte upptäcka alla typer av felaktiga loggdata.

Dessutom använder programmet IP-adresser från misslyckade inloggningsförsök som utgångspunkt för IOC-jämförelser och korrelation. Därför visas inte alla möjliga IOC-träffar från övriga loggkällor i rapporten.

## 5. Alternativ förklaring

Det som programmet visar kan ha flera rimliga förklaringar.

Tre misslyckade inloggningsförsök från samma IP-adress kan exempelvis bero på att en riktig användare har glömt sitt lösenord eller skrivit fel flera gånger.

HTTP 401 innebär att en HTTP-förfrågan saknade giltig autentisering. Detta kan uppstå vid vanliga inloggningsproblem och behöver inte vara ett attackförsök.

En HTTP 404-händelse för `/admin` kan bero på att någon försökte öppna en sida som inte finns. Det kan exempelvis handla om ett felaktigt bokmärke, en gammal länk eller ett automatiserat skript.

En nekad brandväggsanslutning till port 22 kan bero på att en användare eller ett system försökte ansluta till en tjänst utan att ha tillstånd enligt brandväggsreglerna.

Samma IP-adress kan också användas av flera enheter bakom exempelvis Network Address Translation (NAT). Det innebär att alla händelser från adressen inte behöver komma från samma person.

Därför är det viktigt att inte dra för snabba slutsatser om att återkommande IP-adresser eller IOC-träffar är bevis på skadlig aktivitet. Det kan annars leda till falska positiva resultat.

## 6. Säkerhetsbetydelse

Resultatet är relevant eftersom automatiserad logganalys kan hjälpa till att identifiera händelser som bör undersökas närmare.

Om en IP-adress förekommer i flera säkerhetsloggar kan det vara mer intressant än om den bara förekommer i en enskild händelse.

I detta dataset är `203.0.113.15` extra relevant eftersom adressen förekommer i autentiseringsloggen, webbloggen och brandväggsloggen.

Det gör att adressen kan prioriteras vid en fortsatt säkerhetsundersökning.

En säkerhetsanalytiker kan exempelvis undersöka om det finns fler händelser från samma IP-adress, om aktiviteterna fortsätter över tid och om anslutningarna kan kopplas till riktiga användare eller system.

Analysen visar också varför flera loggkällor kan ge ett bättre underlag än en enda loggfil.

Den viktigaste säkerhetsbetydelsen är att programmet hjälper till att prioritera vilka händelser som bör granskas manuellt. Det ersätter däremot inte en fullständig säkerhetsundersökning.

## 7. Tester och verifiering

För att kontrollera programmets funktion genomfördes 3 tester.

### Positive test

#### Genomförande

Programmet kördes med originaldatasetet.

#### Resultat

2 IOC-träffar identifierades.

### Zero-match test

#### Genomförande

IOC-listan ändrades till en IP-adress som inte matchade några misslyckade inloggningsförsök.

#### Resultat

Programmet rapporterade inga IOC-träffar och fortsatte att fungera.

### Malformed data test

#### Genomförande

En extra loggrad med ett tomt `src=`-fält lades till i `auth.log`.

#### Resultat

Programmet identifierade 2 felaktiga loggrader utan att krascha.

Efter testerna återställde jag originalfilerna och körde programmet igen.

Slutrapporten visade återigen:

- 6 loggrader i autentiseringsloggen.
- 4 misslyckade inloggningsförsök.
- 2 IOC-träffar.
- 1 felaktig loggrad.

Detta visar att programmet gav samma resultat när det kördes med samma indata och att de testade felaktiga loggraderna kunde hanteras utan att körningen avbröts.

### Manuell verifiering

Jag jämförde resultatet från `output/security_report.txt` med en manuell genomgång av originalfilerna i Dataset A.

I `auth.log` finns misslyckade inloggningar på rad 1, 2, 3 och 5. Det ger totalt 4 misslyckade inloggningar.

Tre av dessa kommer från `203.0.113.15` och en från `198.51.100.44`.

I `access.log` finns två HTTP 401-händelser på rad 1 och 3.

I `firewall.log` finns en DENY-händelse på rad 2 och en DROP-händelse på rad 3.

### Manuella kontrollvärden

| Kontroll | Manuellt räknat | Programresultat | Stämmer |
|---|---:|---:|---|
| Antal rader i auth.log | 6 | 6 | Ja |
| Misslyckade inloggningar | 4 | 4 | Ja |
| Misslyckade inloggningar från 203.0.113.15 | 3 | 3 | Ja |
| Antal rader i access.log | 4 | 4 | Ja |
| HTTP 401 | 2 | 2 | Ja |
| Antal rader i firewall.log | 3 | 3 | Ja |
| DENY-händelser | 1 | 1 | Ja |
| IOC-träffar | 2 | 2 | Ja |
| Felaktiga loggrader | 1 | 1 | Ja |

Alla kontrollvärden i tabellen stämmer med den genererade rapporten.

Det visar att programmet ger samma antal som den manuella genomgången av originaldatasetet.

Kontrollen gäller de resultat som visas i rapporten. Den bevisar inte att programmet fungerar korrekt för alla möjliga loggformat eller större dataset.


## 8. AI-användning

Jag har använt AI som stöd för Pythonkod, felsökning och dokumentationens struktur. AI har hjälpt mig med förslag på hur programmet kan struktureras, hur felhanteringen kan förbättras och hur olika testfall kan genomföras.

Jag har själv kört programmet i VS Code, genomfört testerna och kontrollerat resultaten mot loggfilerna. AI har också varit ett stöd för att strukturera analysen utifrån uppgiftens krav.


## 9. Förslag på fortsatt utveckling

Utifrån analysen och testerna finns det några förbättringar som skulle kunna göra programmet mer tillförlitligt.

### Bättre datavalidering

Programmet identifierar vissa saknade eller tomma käll-IP-adresser. En förbättring vore att även kontrollera att IP-adresserna har ett giltigt format.

### Tidsbaserad korrelation

Programmet jämför IP-adresser mellan loggkällor men undersöker inte hur nära händelserna ligger varandra i tid.

Genom att jämföra tidsstämplar skulle det bli lättare att bedöma om händelserna kan höra ihop.

### Utökad IOC-matchning

I den nuvarande versionen utgår IOC-matchningen från IP-adresser med misslyckade inloggningar.

En förbättring vore att även kontrollera samtliga IP-adresser i webb- och brandväggsloggarna.

### Utökad brandväggsanalys

Programmet räknar DENY-händelser men inte DROP-händelser i samma räknare.

En framtida version skulle kunna redovisa båda händelsetyperna separat.

