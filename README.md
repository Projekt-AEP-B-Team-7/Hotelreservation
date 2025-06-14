'# B-Team-7 Hotelreservation
Das README.md-File sollte Folgendes enthalten:

Name und Vorname der Teammitglieder, die am Projekt mitgearbeitet haben
Eine kurze Übersicht, wer zu welchen Projekt-Themen beigetragen hat (also z. B. zu welchen User-Stories, Files, Projektphasen, Rollen innerhalb des Teams etc.). Themen, die durch mehrere Teammitglieder bearbeitet wurden, dürft ihr bei allen jeweiligen Teammitgliedern aufführen.
Instruktion für uns, wie eure Applikation benutzt werden muss (Schritt-für-Schritt-Anleitung, insb. welche Notebooks oder Files ausgeführt werden müssen).
Annahmen und Interpretationen, falls welche vorhanden sind.

## Einleitung
Im Rahmen unsere Projektarbeit haben wir den Auftrag erhalten eine  Hotelreservierungssystem mit der Programmiersprache Python zu entwerfen, welches die folgenden User Stories realisieren. Wie bereits in den Guidelines beschrieben, werden wir auf die Userstorys richten.

## Deliverables
Abgabetermin: 15.06.2025
- Source Code und Artefakte
-   Link zu Deepnote-Projekt mit allen ausführbaren Notebooks, Dateien und der endgültigen Datenbank
-   Link zum GitHub-Repository
-   Link zu einer Projekt Board
- Dokumentation/Bericht (Link zu GitHub Markdown-Dateien)
- Link zum Präsentationsvideo (Microsoft Stream, SWITCHtube oder Youtube)

## Links
Deepnote: https://deepnote.com/workspace/FHNW-9efe9cac-fee5-4d76-b7c4-0114c7e240f2/project/AEPB-Team-7-12cf43ae-1be3-4ed6-97d6-f7f9a12a6fe8/notebook/User-Stories-c7ba22b20c7a4a278e9192df60615dea
Präsentationsvideo: 

## Teamarbeit
Unser Team hat grundsätzlich gemeinsam gearbeitet und sich gegenseitig unterstützt, da niemand von uns einen IT-Background hatte. Anstatt feste Rollen oder Zuständigkeiten zu vergeben, haben wir uns jede Woche neue Ziele gesetzt, die wir bis zum nächsten Coaching erreichen wollten. Diese Ziele umfassten sowohl Repetition als auch das Bearbeiten konkreter Aufgaben.

Zu Beginn nutzten wir ein Projektboard, später kommunizierten wir hauptsächlich über WhatsApp und Microsoft Teams. Gegen Projektende wurde das Board nochmals aktiv verwendet, um alle offenen Aufgaben vor der Abgabe gezielt abzuarbeiten. Da alle Teammitglieder regelmässig vor Ort waren, konnten wir die Coaching-Zeit optimal nutzen, um gemeinsam weiterzuarbeiten und bei Bedarf direkt Fragen zu stellen.

Da wir bereits im vorherigen Semester mit Deepnote gearbeitet hatten, entschieden wir uns bewusst dafür, das gesamte Projekt in Deepnote umzusetzen, inklusive Datenmodellierung, Datenzugriff, Logik und Benutzeroberfläche.

## Rollenverteilung im Team

| Name                 | Model                                | Data Access & Business Logic          | User Stories                | Sonstiges                  |
|----------------------|--------------------------------------|---------------------------------------|-----------------------------|----------------------------|
| Saruje Varatharajah  | Invoice, Room, RoomType              | Entsprechend unserer User Stories     | User Story 1.1 bis 1.6, 2   | Dokumentation (README)     |
| Luxaayini Ponnaiya   | Hotel, Guest                         | Entsprechend unserer User Stories     | User Story 3, 8, 9, 10      | Dokumentation (README)     |
| Albina Ramesh        | Address, Booking, Facilities, Review | Entsprechend unserer User Stories     | User Story 4, 5, 6, 7 und DB-Schemaänderung (User Story 1, 3, 4) und Datenvisualisierung (User Story 1)| Input helper files     |

## Class Diagram -> Methoden ergänzen und Erklärung fehlt!
![image](https://github.com/user-attachments/assets/ea5177c5-b2a0-46b1-aecf-14cdf52a97a0)

| Klasse     | Verbunden mit | Kardinalität (von–zu) | Aggregation  | Beschreibung                                                                                   |
|------------|----------------|------------------------|---------------|------------------------------------------------------------------------------------------------|
| Address    | Hotel          | 1:1                    | None          | Jede Adresse ist genau einem Hotel zugeordnet.                                                 |
| Address    | Guest          | 1:1                    | None          | Eine Adresse kann von mehreren Gästen verwendet werden, aber ein Gast hat genau eine Adresse. |
| Hotel      | Address        | 1:1                    | None          | Jedes Hotel besitzt genau eine Adresse.                                                        |
| Hotel      | Room           | 1:1..*                 | Composited    | Ein Hotel besteht aus mindestens einem oder mehreren Zimmern. Ohne Hotel existieren keine Zimmer. |
| Room       | Hotel          | 1..*:1                 | Composited    | Ein oder mehrere Zimmer gehören genau zu einem Hotel.                                          |
| Room       | RoomType       | 1..*:1                 | Shared        | Mehrere Zimmer können denselben Zimmertyp haben.                                               |
| Room       | Facilities     | 0..*:0..*              | Shared        | Ein Zimmer kann gar keine bis mehrere Einrichtungen haben.                                       |
| RoomType   | Room           | 1:1..*                 | Shared        | Ein Zimmertyp kann mehreren Zimmern zugewiesen sein.                                           |
| Facilities | Room           | 0..*:0..*              | Shared        | Ein Zimmer kann gar keine bis mehrere Einrichtungen haben.                                       |
| Guest      | Booking        | 1:0..*                 | Composited    | Ein Gast kann mehrere Buchungen tätigen. Ohne Gast keine Buchung.                             |
| Guest      | Review         | 1:0..*                 | None          | Ein Gast kann mehrere Bewertungen abgeben.                                                     |
| Guest      | Address        | 1:1                    | None          | Jeder Gast hat genau eine Adresse.                                                             |
| Booking    | Guest          | 0..*:1                 | Composited    | Eine Buchung gehört zu genau einem Gast. Ohne Gast keine Buchung.                             |
| Booking    | Room           | 0..*:1                 | None          | Eine Buchung bezieht sich genau auf ein Zimmer.                                                |
| Booking    | Invoice        | 1:1                    | Composited    | Jede Buchung erzeugt genau eine Rechnung. Ohne Buchung keine Rechnung.                        |
| Booking    | Review         | 1:0..1                 | None          | Eine Buchung kann mit höchstens einer Bewertung verknüpft sein.                                |
| Invoice    | Booking        | 1:1                    | Composited    | Jede Rechnung gehört zu genau einer Buchung.                                                   |
| Review     | Guest          | 0..*:1                 | None          | Jede Bewertung wird von genau einem Gast erstellt.                                             |
| Review     | Booking        | 0..1:1                 | None          | Eine Bewertung bezieht sich auf eine Buchung.                                                  |


## Technische Architektur

Unsere Anwendung basiert auf einer klar getrennten Vier-Schichten-Architektur, bestehend aus:

### Model
Diese Schicht umfasst die Klassenstruktur, die direkt auf dem Klassendiagramm basiert (Hotel, Room, Guest, Booking, Invoice, RoomType, Facility, Address).
Jede Klasse wurde in einer eigenen .py-Datei gespeichert, besitzt einen Konstruktor zur Initialisierung, enthält Getter- und Setter-Methoden für kontrollierten Zugriff auf Attribute.
Die Klassen dienen zur Abbildung der Geschäftsobjekte im Code und stellen sicher, dass Daten konsistent verarbeitet werden können.

### Data Access
In dieser Schicht erfolgt der Zugriff auf die SQLite-Datenbank. Jede Entität hat eine eigene Klasse, die auf eine gemeinsame Basisklasse für DB-Verbindungen aufbaut.
Diese Klassen enthalten Methoden für: SELECT, INSERT, UPDATE, DELETE, sowie für komplexere Abfragen mit JOINs.
Die Data-Access-Schicht sind reine Daten und enthalten keine Geschäftslogik.

### Business Logic (Manager-Schicht)
Diese Ebene übernimmt die fachliche Steuerung. Sie stellt die Verbindung zwischen Benutzerinteraktion (UI) und Datenzugriff (Data Accsess) her und validiert alle Aktionen.
Hier wird definiert, wer was darf (z. B. Gast bucht, Admin verwaltet Daten),welche Regeln gelten (z. B. keine Buchung in der Vergangenheit),wie Suchanfragen verarbeitet werden.
Die Business-Logic-Schicht ist wichtig für die Sicherheit und Korrektheit der Anwendung. (Damit klar vorgegebn wird, was der USER machen darf oder kann!)

### User Interface (UI)
Die Benutzeroberfläche wurde in Python direkt in Deepnote als Konsolenanwendung umgesetzt. Sie enthält Menüführung und Eingabeaufforderungen, z. B.: Zimmertypen anzeigen, Buchungen erfassen, Hoteldaten aktualisieren.
Sie ruft Methoden aus der Business-Logik auf und zeigt Ergebnisse oder Fehlermeldungen direkt im Menü an.
Zur Vereinfachung und Strukturierung der Benutzereingaben haben wir modulare Input Helper entwickelt, die jeweils für bestimmte Entitäten zuständig sind (z. B. Gast, Adresse, Buchung).

Jede Eingabehilfe ist in einer eigenen Datei gekapselt, um Wiederverwendung und Wartbarkeit zu gewährleisten. Dabei wird sichergestellt, dass Benutzereingaben korrekt validiert werden (z. B. Datumsformate, erlaubte Städte, Nummernformate, Pflichtfelder). So wird die Eingabelogik von der Geschäftslogik getrennt.

Zu den wichtigsten Eingabehilfen zählen:
* `guest_input_helper.py` – erfasst und prüft Gästedaten (Name, Telefonnummer etc.)
* `address_input_helper.py` – strukturiert die Adresseneingabe
* `date_input_helper.py` – validiert Check-in- und Check-out-Daten
* `booking_helper.py` – steuert den Ablauf der Buchungseingabe
* `admin_helper.py` – erlaubt Admins, Stammdaten wie Zimmer oder Einrichtungen zu pflegen
* `star_input_helper.py` – prüft Bewertungen auf Skalen von 1 bis 5 Sternen
* `city_input_helper.py` – verwendet eine JSON-Liste (swiss_city_list.json) zur Überprüfung von Schweizer Städten

Diese modulare Herangehensweise erhöht die Benutzerfreundlichkeit, reduziert Fehlerquellen und sorgt für eine klare Trennung von Zuständigkeiten in der UI.

## Gelerntes Wissen

Im Verlauf des Projekts haben wir vielfältiges Wissen aufgebaut, sowohl auf technischer als auch auf methodischer Ebene. 

Wir lernten unter anderem:

- wie man aus einem ER-Modell ein Klassendiagramm erstellt

- wie man Klassen mit Attributen und Methoden in Python aufbaut und mit Getter-/Setter-Methoden für saubere Datenkapselung sorgt

- wie eine mehrschichtige Architektur funktioniert, bestehend aus Model, Data Access, Business Logic und UI

- wie man mit SQLite arbeitet, Tabellen verknüpft und Datenbankabfragen sicher gestaltet, (Datenschema erstellt??)

- wie man Datenbankzugriffe vom Code trennt, um Wiederverwendbarkeit und Wartbarkeit sicherzustellen (UI layer Methoden werden aufgerufen!)

- wie man Business-Logik sauber strukturiert, um Benutzeraktionen zu steuern und Daten zu validieren

Darüber hinaus lernten wir viel über Testen, Fehlersuche, Umgang mit Fehlermeldungen und wie man im Team gemeinsam Probleme löst. 

## Herausforderung

Eine erste Herausforderung war der Einstieg in die praktische Umsetzung nach der theoretischen Phase. Obwohl wir das Klassendiagramm gut erarbeiten konnten, war zunächst nicht klar, wie daraus ein funktionierendes System entstehen soll. Insbesondere die Trennung in verschiedene Schichten war für uns schwer verständlich. Erst durch Unterstützung unserer Coaches, mit einem praxisnahen Beispiel zur Schichtenarchitektur, konnten wir die Zusammenhänge zwischen Model, Data Access und Business Logic nachvollziehen und korrekt umsetzen.

Ein weiterer schwieriger Punkt war das Fehlersuchen. Sie konnten in jeder Schicht entstehen und waren nicht immer sofort nachvollziehbar. Oft verursachte ein kleider Fehler dazu, dass der gesamte Ablauf nicht mehr funktionierte. Fehlermeldungen waren manchmal unklar und führten zu viel Sucharbeit über mehrere Ebenen hinweg. Das erforderte Geduld, Konzentration und Teamarbeit.
Auch das Umsetzen von Benutzerabfragen und Menüs in der UI-Schicht war komplexer als erwartet, insbesondere, wenn Eingaben validiert oder dynamisch auf Datenbankinhalte reagiert werden musste.Oftmals mussten wir zwischen den layers switchen und dort Änderungen vornehmen und eine von mehreren Fehler zu bereinigen. 

## Reflexion

Rückblickend war dieses Projekt für uns alle ein intensiver, aber auch sehr wertvoller Lernprozess. Wir haben viel Neues über Programmierung, Datenbanken und den Aufbau eines Systems gelernt. Besonders die technische Struktur, also wie man ein Projekt in mehrere Schichten (Model, Data Access, Business Logic und Benutzeroberfläche) aufteilt, wurde für uns nach und nach verständlich.

Wichtig war auch unsere Teamarbeit. Wir haben viel gemeinsam ausprobiert, uns gegenseitig unterstützt, Fehler erklärt und gemeinsam Lösungen gesucht. Dabei haben wir gemerkt, wie wichtig Kommunikation und Geduld sind, vor allem, wenn etwas nicht gleich funktioniert.

Natürlich gab es auch viele Herausforderungen und Momente, in denen wir nicht weiterwussten. Doch gerade in diesen Phasen haben wir am meisten gelernt. Durch die Hilfe unserer Coaches und durch unser eigenes Dranbleiben konnten wir Schritt für Schritt ein funktionierendes System aufbauen.

Am Ende hat uns dieses Projekt gezeigt, dass man etwas Komplexes umsetzen kann, wenn man als Team zusammenarbeitet, sich Zeit nimmt und offen bleibt für Neues.

## Angewendete User Stories
Im Rahmen unseres Projekts haben wir die folgenden User Stories umgesetzt. Die Vorgehensweise ist jeweils in Deepnote bei der entsprechenden User Story dokumentiert. Gemäss Dokument Guidlines haben wir haben alle Minimale User Stories umgesetzt von DB-Schemaänderung haben wir 3 User Stories umgesetzt und von Datenvisualisierung haben wir einen User Story umgesetzt.

### Minimale User Stories

1. Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht.\
1.1 Ich möchte alle Hotels in einer Stadt durchsuchen,damit ich das Hotel nach meinem bevorzugten Standort (Stadt) auswählen kann.\
1.2 Ich möchte alle Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.\
1.3 Ich möchte alle Hotels in einer Stadt durchsuchen,die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).\
1.4 Ich möchte alle Hotels in einer Stadt durchsuchen, die während meines Aufenthaltes ("von" (check_in_date) und "bis" (check_out_date)) Zimmer zur Verfügung haben, damit ich nur relevante Ergebnisse sehe.\
1.5 Ich möchte Wünsche kombinieren können, z.B. die verfügbaren Zimmer zusammen mit meiner Gästezahl und der mindest Anzahl Sterne.\
1.6 Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.

2. Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.\
2.1. Ich möchte die folgenden Informationen pro Zimmer sehen: Zimmertyp, max. Anzahl der Gäste, Beschreibung, Ausstattung, Preis pro Nacht und Gesamtpreis.\
2.2. Ich möchte nur die verfügbaren Zimmer sehen, sofern ich meinen Aufenthalt (von – bis) spezifiziert habe.

3. Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.\
3.1. Ich möchte neue Hotels zum System hinzufügen.\
3.2. Ich möchte Hotels aus dem System entfernen.\
3.3. Ich möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.

4. Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe.
Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.
6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige.
Hint: Sorgt für die entsprechende Invoice.
7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.
Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.
8. Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten.
9. Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.
10. Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.

### User Stories mit DB-Schemaänderung
1. Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer).
3. Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.
4. Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

### User Stories mit Datenvisualisierung
1. Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimiren kann.
Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach Zimmertyp darzustellen (z.B. wie oft jeder Zimmertyp gebucht wird).
