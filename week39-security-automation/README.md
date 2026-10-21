
# Security Automation Report – Dataset A

## 1. Syfte

Syftet med projektet är att använda Python för att automatisera en säkerhetsanalys av loggfiler.

Programmet analyserar inloggningsförsök, webbtrafik och brandväggshändelser. Det jämför även IP-adresser med en IOC-lista för att hitta händelser som kan behöva undersökas närmare.

Resultatet sparas i `output/security_report.txt`.

En IOC-träff betyder inte automatiskt att en attack har skett.

## 2. Datasetval

Jag har valt Dataset A (Basic) från kursen.

Datasetet innehåller syntetiska säkerhetsloggar från den 24 september 2026.

Filer som används:

- `data/auth.log` – 6 loggrader om inloggningar.
- `data/access.log` – 4 loggrader om HTTP-förfrågningar.
- `data/firewall.log` – 3 loggrader om brandväggshändelser.
- `data/suspicious_ips.txt` – 3 IP-adresser för IOC-matchning.

Totalt innehåller loggfilerna 13 loggrader.

## 3. Pythonversion

Projektet har utvecklats i Visual Studio Code på macOS.

Pythonversion: Python 3.14.7

## 4. Körinstruktion

Öppna projektmappen `week39-security-automation` i VS Code.

Öppna terminalen och kör:

`python3 src/security_report.py`

Programmet läser loggfilerna från mappen `data/` och skapar rapporten:

`output/security_report.txt`

För att visa rapporten i terminalen:

`cat output/security_report.txt`

Programmet kan köras igen med samma indata för att återskapa rapporten.

## 5. Projektstruktur

```text
week39-security-automation/
├── README.md
├── data/
│   ├── auth.log
│   ├── access.log
│   ├── firewall.log
│   └── suspicious_ips.txt
├── src/
│   └── security_report.py
├── output/
│   └── security_report.txt
└── docs/
    └── analysis.md
```

- `data/` innehåller datasetet.
- `src/` innehåller Pythonprogrammet.
- `output/` innehåller den genererade rapporten.
- `docs/` innehåller säkerhetsanalysen.

## 6. Testning och verifiering

Tre testfall har dokumenterats i `docs/analysis.md`.

### Test 1 – Positive test

Programmet kördes med originaldatasetet.

Förväntat resultat: 2 IOC-träffar.

Resultat: 2 IOC-träffar.

### Test 2 – Zero-match test

IOC-listan ändrades till en adress som inte matchade några misslyckade inloggningsförsök.

Förväntat resultat: 0 IOC-träffar.

Resultat: 0 IOC-träffar.

### Test 3 – Malformed data test

En extra loggrad med ett tomt `src=`-fält lades till i `auth.log`.

Förväntat resultat: 2 felaktiga loggrader.

Resultat: 2 felaktiga loggrader. Programmet fortsatte utan att krascha.

Efter testerna återställdes originalfilerna.

Jag jämförde också programmets resultat med manuellt räknade värden från loggfilerna.

Exempel:

- Misslyckade inloggningar: 4.
- HTTP 401: 2.
- DENY-händelser: 1.
- IOC-träffar: 2.
- Felaktiga loggrader: 1.

Resultaten stämde med den genererade rapporten.

## 7. Kända begränsningar

- Datasetet är litet och innehåller bara 13 loggrader.
- En IOC-träff är inte ett bevis på en attack.
- Programmet gör inte fullständig IP-adressvalidering.
- Korrelationen bygger på IP-adresser som förekommer i flera loggkällor.
- Programmet kontrollerar inte tidsavståndet mellan händelserna.
- IOC-matchningen utgår från IP-adresser med misslyckade inloggningar.
- Brandväggsanalysen räknar DENY men inte DROP.

Programmet används endast för defensiv analys av syntetiska loggar. Det kontaktar inga externa tjänster och ändrar inte brandväggsregler eller användarkonton.

## 8. AI-redovisning

Jag har använt ChatGPT som stöd under arbetet.

AI har hjälpt mig med att förstå uppgiften, få förslag på Pythonkod, felsöka och strukturera dokumentationen.

Jag har själv kört programmet i VS Code och jämfört resultaten med loggfilerna.

Jag har använt AI-förslag som stöd och kontrollerat resultaten genom att köra programmet och jämföra rapporten med loggfilerna.

Mer information om analys, evidens och tester finns i `docs/analysis.md`.

## 9. Möjliga förbättringar

Programmet fungerar med Dataset A, men det finns möjligheter att utveckla analysen vidare.

I framtiden skulle jag vilja:

- Validera IP-adresser mer noggrant.
- Jämföra tidsstämplar för att undersöka om händelser hänger ihop.
- Kontrollera IOC-adresser mot alla loggkällor.
- Utöka brandväggsanalysen så att både DENY och DROP räknas.

Dessa förbättringar skulle kunna göra analysen mer användbar för större dataset.

