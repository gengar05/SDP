# Case A – AI-phishing mot en kommun

> Scenario En kommunal förvaltning har fått flera välformulerade mejl som ser ut att komma från intern IT-support. Mottagarna uppmanas att logga in via en länk för att behålla åtkomsten till ett internt system. En i personalen har klickat på länken men uppger att inga uppgifter lämnades. Organisationen vet ännu inte om mejlen skapats med AI. Det finns inga bekräftade uppgifter om intrång.

## 1.0 Executive Summary

Denna rapport analyserar misstänkta och välformulerade mejl som har skickats till flera i personalen inom en kommunal förvaltning. Mejlen ser ut att komma från intern IT-support och uppmanar mottagarna att logga in via en länk för att behålla åtkomsten till ett internt system. En mottagare har öppnat länken men uppger att inga inloggningsuppgifter lämnades. Det finns inga bekräftade intrång eller incidenter.

Analysen identifierar användarkonton, inloggningsuppgifter, interna system och information som viktiga tillgångar. Den kvalitativa riskbedömningen är medel eftersom flera mottagare har fått mejlet och en mottagare har öppnat länken, samtidigt som inget intrång har bekräftats. Ett möjligt intrång skulle kunna påverka konfidentialitet, integritet och tillgänglighet.

Rapporten använder CIS 6 – Access Control Management, CIS 8 – Audit Log Management och CIS 14 – Security Awareness and Skills Training. De prioriterade åtgärderna är att granska loggar och användarkonton, stärka åtkomstkontrollen samt utbilda personalen i hur misstänkta mejl kan identifieras och hanteras.

Det är osäkert om AI har använts för att skapa mejlen. Därför behandlas AI som en möjlighet och inte som ett faktum. Ytterligare undersökning av bland annat loggar, användarkonton och länken behövs för att kunna minska den kvarvarande osäkerheten.

## 2.0 Fakta, antaganden och scope

### 2.1 Givna fakta

Vi vet att flera i personalen inom en kommunal förvaltning har fått välformulerade mejl som ser ut att komma från intern IT-support. Mejlen uppmanar mottagarna att logga in via en länk för att behålla åtkomsten till ett internt system. En mottagare har öppnat länken men uppger att hen inte har lämnat några uppgifter. Det finns ingen bekräftad incident i dagsläget. Det är inte heller fastställt om AI har använts. AI-användning är en möjlighet, inte ett faktum.

### 2.2 Antaganden

- Mejlet kan vara ett phishingmejl som försöker få mottagarna att lämna ut sina inloggningsuppgifter.
- AI kan ha använts för att skapa mejlet.
- Länken kan leda till en falsk inloggningssida som efterliknar kommunens riktiga sida.
- Om inloggningsuppgifter lämnas ut kan en obehörig få tillgång till mottagarens konto och interna system.

### 2.3 Frågor som behöver verifieras

Några frågor som behöver verifieras är:

- Finns det någon misstänkt aktivitet på användarkontona efter att mejlen skickades?
- Vart leder länken?
- Visar loggarna några ovanliga eller obehöriga inloggningsförsök?
- Har fler mottagare klickat på länken eller lämnat ut inloggningsuppgifter?
- Vilken mejladress skickades mejlet från och tillhör den verkligen kommunens interna IT-support?
- Har AI faktiskt använts för att skapa mejlen?

### 2.4 Scope

Rapporten fokuserar på de misstänkta och välformulerade mejl som ser ut att komma från intern IT-support och som har skickats till flera mottagare inom en kommunal förvaltning. Analysen undersöker vilka säkerhetsrisker mejlen kan innebära för mottagarnas konton, inloggningsuppgifter och åtkomst till det interna systemet. Rapporten kommer även att undersöka möjliga konsekvenser och vilka säkerhetsåtgärder som kan användas för att minska riskerna. Det är inte heller fastställt om AI har använts för att skapa mejlen. Därför kommer AI-användning att behandlas som en möjlighet och inte som ett bekräftat faktum.

## 3.0 Tillgångar och händelsekedja

### 3.1 Tillgångar

Användarkonton: Personalens användarkonton är viktiga att skydda eftersom obehöriga annars kan få tillgång till information och interna system.

Inloggningsuppgifter: Inloggningsuppgifter behöver skyddas eftersom de används för att identifiera användaren och få åtkomst till ett konto.

Internt system: Det interna systemet är en viktig tillgång eftersom personalen behöver ha säker åtkomst till systemet samtidigt som obehöriga inte ska kunna få tillgång till det.

Information: Informationen som finns i interna system behöver skyddas från att obehöriga får åtkomst till eller förändrar den, eftersom detta kan leda till att man inte längre kan lita på informationen.

Förtroende för intern IT-support: Det är viktigt att personalen kan lita på mejl från intern IT-support. Falska mejl som ser äkta ut kan göra det svårare att veta vilka mejl de kan lita på.

### 3.2 Händelsekedja

1 **Mejl skickas** – Mottagarna får mejl som ser ut att komma från intern IT-support.

->

2 **Uppmaning** – Mottagarna uppmanas att logga in via en länk för att behålla åtkomsten till ett internt system.

->

3 **Länken öppnas** – En mottagare öppnar länken men uppger att inga uppgifter lämnades.

->

4 **Hypotetiskt nästa steg** – Om länken leder till en falsk inloggningssida skulle mottagaren kunna lämna ut sina inloggningsuppgifter i tron att sidan är äkta.

->

5 **Hypotetisk konsekvens** – Om inloggningsuppgifterna lämnas ut skulle en obehörig kunna försöka få åtkomst till användarkontot och interna system.

## 4.0 CIA och enkel riskbedömning

### 4.1 CIA

#### C – Confidentiality

Konfidentialitet handlar om att informationen ska skyddas från obehöriga och endast vara tillgänglig för personer med behörighet.

I detta case kan konfidentialiteten påverkas ifall en mottagare skulle lämna ut sina inloggningsuppgifter via länken i mejlet. Om en obehörig skulle få tillgång till uppgifterna skulle personen kunna försöka logga in på mottagarens konto för att få åtkomst till information och interna system. Detta kan i sin tur innebära att informationen blir sedd av någon som saknar behörighet att se den.

#### I – Integrity

Integritet handlar om att informationen ska vara korrekt och inte ändras av obehöriga.

I detta case kan integriteten påverkas ifall en obehörig skulle få tillgång till mottagarens konto eller interna system. I så fall skulle den obehöriga kunna ändra eller ta bort information som finns i systemet. Detta skulle kunna leda till att man inte längre kan vara säker på att informationen är korrekt och går att lita på.

#### A – Availability

Tillgänglighet handlar om att system och information ska vara tillgängliga för behöriga användare när de är i behov av dem.

I detta case kan tillgängligheten påverkas ifall en obehörig skulle få tillgång till ett användarkonto eller internt system. Den obehöriga skulle exempelvis kunna göra förändringar som gör att mottagaren inte längre kan få åtkomst till sitt konto eller information som behövs för arbetet. Detta kan påverka mottagarens möjlighet att ha tillgång till system och information.

#### Sammanfattning av CIA

Konsekvenserna som beskrivs ovan för CIA är möjliga konsekvenser och inte något som är bekräftat i nuläget. Det finns ingen bekräftad incident eller något bekräftat intrång, och mottagaren som öppnade länken uppger att inga uppgifter lämnades. Därför är konsekvenserna som beskrivs ovan hypotetiska.

### 4.2 Kvalitativ riskbedömning

Utifrån informationen i detta case skulle jag bedöma risken som medel. Mejlet har skickats till flera mottagare inom en kommunal förvaltning och det finns en bekräftad mottagare som har öppnat länken. Detta visar att mejlet har lyckats få åtminstone en mottagare att agera på innehållet. Samtidigt följde mottagaren inte uppmaningen fullt ut eftersom inga uppgifter lämnades. Det finns inte heller något bekräftat intrång eller någon bekräftad incident i nuläget.

Ifall en mottagare däremot hade lämnat ut sina inloggningsuppgifter skulle konsekvenserna kunna bli större. En obehörig hade i så fall kunnat försöka få åtkomst till användarkontot och interna system. Detta skulle i sin tur kunna påverka konfidentialiteten genom att obehöriga får tillgång till information, integriteten genom att information kan förändras och tillgängligheten genom att behöriga användare kan få problem med att komma åt sina konton och system.

Risken skulle jag därför bedöma som medel istället för låg, eftersom flera mottagare har fått mejlet och en person har öppnat länken. Jag skulle inte klassificera risken som hög, eftersom inget intrång har bekräftats. Bedömningen kan självklart ändras om ny information framkommer. Därför är det viktigt att exempelvis granska loggar och användarkonton.

AI kan möjligtvis ha använts för att skapa eller formulera mejlen. Eftersom detta inte är bekräftat påverkar det inte riskbedömningen direkt. Risknivån bedöms istället utifrån de bekräftade omständigheterna i caset, exempelvis att flera mottagare har fått mejlet och att en mottagare har öppnat länken.

## 5.0 CIS-mappning

### 5.1 CIS 6 – Access Control Management

CIS 6 – Access Control Management handlar om att hantera samt kontrollera vilka användare som har åtkomst till olika system, konton och information. Användare bör endast ha de behörigheter och den åtkomst de behöver för att kunna utföra sitt arbete.


CIS 6 är relevant i detta case eftersom de misstänkta mejlen uppmanar mottagarna att logga in via en länk. Ifall mottagarens inloggningsuppgifter skulle lämnas ut och en obehörig får tillgång till användarkontot kan stark åtkomstkontroll hjälpa till att begränsa vad den obehöriga kan få åtkomst till. Om användarkontot endast har de behörigheter som behövs för arbetet kan konsekvenserna av ett kapat konto begränsas.

En åtgärd kan därför vara att kontrollera användarnas behörigheter och säkerställa att de inte har mer åtkomst än nödvändigt. Organisationen kan även använda starkare inloggningsskydd för att minska risken att endast stulna inloggningsuppgifter leder till åtkomst. Detta skulle exempelvis kunna vara multifaktorautentisering (MFA) som ett extra skydd vid inloggning. MFA innebär att användaren behöver verifiera sig på mer än ett sätt. Om en mottagare skulle lämna ut sina inloggningsuppgifter kan MFA ge ett ytterligare skydd och minska risken för obehörig åtkomst.

Verifiering: Åtgärden kan verifieras genom att kontrollera användarnas behörigheter och säkerställa att de endast har åtkomst till de system och den information som behövs för deras arbete. Man kan även kontrollera att MFA är aktiverat och fungerar vid inloggning.

### 5.2 CIS 8 – Audit Log Management

CIS 8 – Audit Log Management handlar om att samla in, granska och hantera loggar från konton och system. Loggarna kan användas för att kontrollera vad som har hänt och hjälpa till att upptäcka misstänkt aktivitet.

CIS 8 är relevant i detta case eftersom en mottagare har öppnat länken i det misstänkta mejlet, samtidigt som det inte finns något bekräftat intrång. Genom att granska relevanta loggar kan man undersöka om det exempelvis har skett ovanliga eller obehöriga inloggningsförsök på användarkontot efter att mejlet skickades. Loggarna kan vara till hjälp för att avgöra om händelsen stannade vid att länken öppnades eller om det finns annan misstänkt aktivitet.

En åtgärd kan vara att säkerställa att relevanta säkerhets- och inloggningshändelser loggas och att loggarna granskas vid misstänkt aktivitet. På detta sätt har man bättre förutsättningar att snabbt upptäcka, spåra och utreda möjliga säkerhetsincidenter.

Verifiering: Man kan verifiera åtgärden genom att kontrollera att relevanta loggar faktiskt skapas och att de innehåller relevant information för att kunna undersöka en sådan händelse. Man kan även kontrollera att loggarna går att använda för att identifiera misslyckade eller ovanliga inloggningsförsök.

### 5.3 CIS 14 – Security Awareness and Skills Training

CIS 14 – Security Awareness and Skills Training handlar om att utbilda personalen inom IT-säkerhet och ge dem kunskap om hur de ska hantera och agera vid olika säkerhetshot. Exempelvis behöver de kunna känna igen phishingmejl och veta hur de ska hantera dem.

CIS 14 är relevant i detta case eftersom flera i personalen har fått ett mejl som misstänks vara phishing och som ser ut att komma från intern IT-support. En mottagare har även öppnat länken i mejlet. Utbildning kan hjälpa personal att bli mer uppmärksamma på phishingmejl och kontrollera att ett mejl verkligen kommer från den avsändare som det påstår sig komma från innan de klickar på länkar eller agerar på innehållet.

En åtgärd kan vara att utbilda personal i hur de kan identifiera och hantera phishingmejl. Det är även bra om det finns en tydlig rutin för hur de ska verifiera och rapportera misstänkta mejl till IT-support. Som ett kompletterande tekniskt skydd skulle spamkontroll i mejlsystemet kunna användas. Spamkontrollen kan hjälpa till att filtrera misstänkta mejl innan de når mottagaren. Att kombinera detta med utbildning är viktigt eftersom personalen fortfarande behöver veta hur de ska agera om ett misstänkt mejl når inkorgen. Utbildningen kan även ta upp att misstänkta mejl kan vara välformulerade och se trovärdiga ut. AI kan möjligtvis användas för att skapa eller förbättra mejl men det är inte bekräftat att AI har använts i detta case. Därför bör personalen inte försöka avgöra om ett mejl är AI-genererat utan istället fokusera på att kontrollera avsändaren, länkar och andra tecken på phishing.

Verifiering: Åtgärden kan verifieras genom att kontrollera att personalen har genomfört utbildningen och testa deras kunskap om säkerhetshot och hur de ska hanteras. Spamkontrollen kan verifieras genom att kontrollera att den är aktiv och att mejl filtreras enligt organisationens inställningar.

## 6.0 Prioriterade åtgärder

### 6.1 Prioritet 1 – Granska loggar och konton

Den åtgärd jag hade prioriterat först är att granska loggar och användarkonton. Anledningen till att jag hade lagt detta som prioritet ett är att det finns en mottagare som vi vet har öppnat länken i mejlet. Däremot finns det inget bekräftat intrång eller någon bekräftad incident. Därför är det viktigt att ta reda på ifall det har skett någon ytterligare aktivitet efter att länken öppnades.

Genom att granska relevanta loggar kan man undersöka ifall det finns ovanliga eller obehöriga inloggningsförsök kopplade till det berörda kontot. Det hjälper till att ge en bättre bild av händelsen och man kan undersöka ifall den stannade vid att mottagaren öppnade länken eller om det finns tecken på annan ovanlig aktivitet. Loggar är viktiga för att upptäcka, spåra och utreda möjliga säkerhetsincidenter, vilket även kopplar åtgärden till CIS 8 – Audit Log Management.

Det är också viktigt att kontrollera det berörda användarkontot för att undersöka om det finns aktivitet som användaren inte känner igen. Mottagaren som öppnade länken uppger att inga uppgifter lämnades, men detta betyder inte att man ska utgå från att ingenting har hänt. Kontrollen genomförs därför för att undersöka om det finns tecken på obehörig eller misstänkt aktivitet.

Man kan verifiera åtgärden genom att dokumentera att loggar och användarkonton har granskats samt vilket resultat granskningen gav. Man kan exempelvis kontrollera om det finns ovanliga eller obehöriga inloggningsförsök eller annan aktivitet som sticker ut. Om granskningen inte visar någon misstänkt aktivitet är även det ett resultat som kan dokumenteras. Om misstänkt aktivitet upptäcks kan informationen istället användas för att avgöra vilka ytterligare åtgärder som behöver genomföras.

### 6.2 Prioritet 2 – Stärka åtkomstkontrollen

Åtgärden jag hade prioriterat som tvåa är att stärka åtkomstkontrollen för användarkonton. Anledningen är att mejlet uppmanar mottagarna att logga in via en länk. Skulle en mottagare i detta fall lämna ut sina inloggningsuppgifter finns det en risk att en obehörig försöker använda uppgifterna för att få åtkomst till användarens konto samt interna system.Därför är det viktigt att kontrollera användarnas behörigheter och säkerställa att de endast har behörighet och åtkomst till det som behövs för att utföra deras arbete. Ifall ett konto skulle bli kapat kan begränsade behörigheter hjälpa till att minska hur mycket information samt vilka system den obehöriga kan komma åt.

Något man kan implementera är MFA (multifaktorautentisering), som fungerar som ett extra skydd vid inloggning. Detta innebär att användaren behöver verifiera sin identitet på mer än ett sätt. Ifall en användares inloggningsuppgifter skulle lämnas ut kan MFA ge ett ytterligare skydd mot obehörig åtkomst. Däremot vet vi inte utifrån caset ifall organisationen redan använder MFA, så detta behandlas som ett förslag till säkerhetsåtgärd och inte som ett befintligt skydd.

Denna åtgärd kopplas till CIS 6 – Access Control Management, eftersom CIS 6 handlar om att stärka åtkomstkontrollen och begränsa behörigheter för att kunna minska konsekvenserna av obehörig åtkomst.

Man kan verifiera åtgärden genom att kontrollera användarnas behörigheter och säkerställa att de endast har tillgång till de system och den information de behöver för att utföra sitt arbete. Ifall MFA införs eller redan används kan man säkerställa att det är aktiverat samt testa att det fungerar korrekt vid inloggning.

### 6.3 Prioritet 3 – Utbildning och skydd mot phishingmejl

Den tredje åtgärden jag hade prioriterat är att utbilda personalen i hur de kan identifiera och hantera säkerhetshot, i detta fall misstänkta phishingmejl. Detta är relevant eftersom flera i personalen har fått det misstänkta mejlet samt att en mottagare har öppnat länken som fanns i mejlet. Genom utbildning kan personalen få bättre kunskap om vilka tecken de bör vara uppmärksamma på samt hur de ska agera innan de klickar på länkar eller lämnar ut information. Utbildningen bör även göra personalen medveten om att misstänkta mejl kan vara välformulerade och trovärdiga, oavsett om AI har använts eller inte.

Det är viktigt att man har en tydlig rutin för hur misstänkta mejl ska verifieras och rapporteras. Ifall någon i personalen får ett mejl som ser ut att komma från intern IT-support bör det finnas ett tydligt sätt att kontrollera att avsändaren verkligen är den som den utger sig för att vara. Som ett kompletterande tekniskt skydd hade jag rekommenderat att man implementerar ett spamfilter i e-postsystemet. Spamfilter kan hjälpa till att filtrera misstänkta mejl innan de når mottagarnas inkorgar. Det är däremot viktigt att man inte ser spamfilter som en ersättning för utbildning, eftersom det kan finnas misstänkta mejl som inte filtreras bort.

Åtgärden kopplas till CIS 14 – Security Awareness and Skills Training, eftersom utbildning samt tydliga rutiner kan hjälpa personalen att känna igen och hantera misstänkta mejl på ett säkrare sätt. Det stämmer också med uppgiftens beskrivning av CIS 14, där just utbildning och verifieringsrutiner lyfts fram.

Man kan verifiera åtgärden genom att kontrollera att personalen har genomfört utbildningen och testa deras kunskap med simulerade phishingmejl för att se hur de hanterar och rapporterar dem. Det är även viktigt att kontrollera att rutinen för rapportering finns tillgänglig för personalen. Spamfiltret kan verifieras genom att kontrollera att det är aktiverat och att filtreringen fungerar enligt organisationens inställningar.

## 7.0 Teknisk koppling

En teknisk koppling till tidigare kursmoment är arbetet med Linux och loggar. Vi har tidigare arbetat med Linux och fått förståelse för hur loggar kan användas för att registrera och undersöka olika händelser i ett system. Loggar innehåller information som gör det enklare att förstå vad som har hänt och kan vara användbara när man behöver undersöka misstänkt aktivitet.

Det går att koppla detta till caset eftersom en mottagare av mejlet öppnade länken, men samtidigt finns det inget bekräftat intrång eller någon bekräftad incident. Genom att använda kunskapen från tidigare kursmoment skulle man kunna granska relevanta inloggnings- och säkerhetsloggar för att undersöka ifall det finns aktivitet som är utöver det vanliga.

Loggar är därför en viktig del av undersökningen då de kan bidra med mer information om vad som har hänt efter att länken öppnades. Ifall det finns misstänkt aktivitet kan loggarna hjälpa till att identifiera och spåra den. Ifall granskningen inte visar någon misstänkt aktivitet är även det ett resultat som kan dokumenteras. Däremot ska man inte dra slutsatsen att ingenting har hänt enbart för att en viss logg inte visar något. Resultatet behöver bedömas utifrån vilken information som faktiskt har loggats.

Detta hänger ihop med CIS 8 – Audit Log Management, där loggar används för att stödja upptäckt, spårbarhet och utredning. Kunskapen som vi har fått från tidigare kursmoment kan därför användas praktiskt i detta case för att undersöka en möjlig säkerhetshändelse. Detta stämmer även överens med hur CIS 8 beskrivs i examinationsuppgiften.

En annan teknisk koppling är användarkonton och åtkomstkontroll. I caset är användarkonton viktiga eftersom mejlet uppmanar mottagarna att logga in via en länk. Ifall inloggningsuppgifterna skulle hamna hos en obehörig blir det viktigt hur kontots behörigheter och åtkomst är konfigurerade. Genom att begränsa behörigheter kan man minska vilka system och vilken information ett konto har åtkomst till. Detta kopplas till CIS 6 – Access Control Management, där stark åtkomstkontroll och begränsade behörigheter kan användas för att begränsa konsekvenserna av obehörig åtkomst.

All denna kunskap från tidigare kursmoment går att koppla till säkerhetsscenariot i detta case. Arbetet med Linux och loggar har gett en förståelse för hur man kan undersöka misstänkt aktivitet, medan kunskapen om användarkonton och åtkomst hjälper till att förstå hur obehörig åtkomst kan förebyggas och begränsas.

## 8.0 English Security Summary

This report analyses suspicious emails sent to several employees within a municipal administration. The emails appears to come from an internal IT-support, which asks recipients to log in through a link. The overall risk is assessed as medium because one recipient opened the link, yet no security incident or intrusion has been confirmed.

The main assets at risk are user accounts, login credentials, internal systems and information. Unauthorised access could affect confidentiality, integrity and availability. The report applies CIS controls 6, 8 and 14 to reduce the risks. The highest priority is to review logs and user accounts for suspicious activity, followed by stronger access controls such as MFA and improved security awareness training.

AI may have been used to create or improve the emails but this remains unconfirmed. Therefore the report treats AI involvement as a possibility rather than a fact.

## 9.0 AI- och källredovisning

Under arbetet har jag använt AI som ett hjälpmedel. Främst har jag använt det för att få hjälp med rapportens struktur och förklaringar av vissa begrepp. Jag har även använt AI för att få hjälp med att hitta källor med relevant information. Informationen jag har fått från AI har jag inte använt som fakta direkt, utan jag har kontrollerat innehållet och de källor som använts. Jag har även använt ytterligare källor för att kontrollera att informationen stämmer. Om information eller formuleringar från AI inte har stämt överens med informationen i caset har jag inte använt dem.

Källorna som har använts i arbetet är hänvisade i docs/references.md.

## 10.0 Slutsats

Utifrån analysen bedömer jag risken som medel. Flera i personalen har fått mejlet som kan vara ett phishingmejl och en mottagare har öppnat länken. Mottagaren uppger däremot att inga inloggningsuppgifter lämnades och det finns inget bekräftat intrång eller någon bekräftad incident. Därför finns det en säkerhetsrisk som behöver undersökas och hanteras, men inte tillräckligt med information för att kunna dra slutsatsen att det har skett ett intrång. Detta gör att en riskbedömning på medelnivå är proportionerlig utifrån informationen som har givits.

De prioriterade åtgärderna är att granska loggar och användarkonton, stärka åtkomstkontrollen samt utbilda personalen. Dessa åtgärder kan både hjälpa till att undersöka den nuvarande händelsen och förebygga framtida incidenter.

Däremot finns det flera kvarvarande osäkerheter. Bland annat behöver man verifiera vart länken leder, ifall loggarna visar ovanlig eller obehörig aktivitet och ifall fler mottagare har klickat på länken eller lämnat ut inloggningsuppgifter.

Det är inte heller fastställt ifall AI har använts för att skapa mejlet. AI är en möjlighet men inte ett bekräftat faktum. Oavsett ifall AI har använts eller inte är de föreslagna säkerhetsåtgärderna relevanta för att minska risken med denna typ av misstänkta mejl.
