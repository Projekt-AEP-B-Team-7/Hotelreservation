# B-Team-7 Hotelreservation

## Autoren
- Saruje Varatharajah
- Luxaayini Ponnaiya
- Albina Ramesh

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
Deepnote:\
Project Board:\
Präsentationsvideo:

### Teamarbeit:
Unser Team hat grundsätzlich gemeinsam gearbeitet und sich gegenseitig unterstützt, da niemand von uns einen IT-Background hatte. Anstatt feste Rollen oder Zuständigkeiten zu vergeben, haben wir uns jede Woche neue Ziele gesetzt, die wir bis zum nächsten Coaching erreichen wollten. Diese Ziele umfassten sowohl Repetition als auch das Bearbeiten konkreter Aufgaben.

Zu Beginn haben wir mit einem Projektboard gearbeitet, im weiteren Verlauf jedoch primär über WhatsApp und Microsoft Teams kommuniziert. Gegen Projektende haben wir das Board nochmals aktiv genutzt, um offene Aufgaben vor der Abgabe zu erledigen. Da alle Teammitglieder regelmässig vor Ort waren, konnten wir die Coaching-Zeit optimal nutzen, um gemeinsam weiterzuarbeiten und bei Bedarf direkt Fragen an unsere Coaches zu stellen. Da wir bereits im vorherigen Semester mit Deepnote gearbeitet hatten und damit vertraut waren, entschieden wir uns bewusst dafür, alle Bestandteile unseres Projekts, also Model, Data Access, Business Logic und User Interface, vollständig in Deepnote umzusetzen.

### Vorgehensweise im Projekt:

Unser Projekt begann mit der Erstellung eines Klassendiagramms auf Basis des vorgegebenen ER-Modells. Da die Klassen und ihre Attribute bereits definiert waren, konnten wir diese direkt übernehmen.

### Class Diagram

![image](https://github.com/user-attachments/assets/1b4d7a91-2510-4f92-bc11-e5e5cce9ef09)
 
Class Address: (Cardinality 1:1)
Attributes: address_id, street, city, zip_code
Relationship: One-to-one with both Hotel and Guest (One to One) 

Class Guest: (Cardinality 1:0)
Attributes: address_id, street, city, zip_code
Relationship: One Guest has one address and One Guest can have multiple bookings (One to many)

Class Booking (Cardinality 0:1), (Cardinality 1:1)
Attributes: booking_id, check_in_date, check_out_date, is_cancelled, total_amount
Relationships: One or more Booking belongs to one guest, One Booking is linked to one invoice

Class Invoice: (Cardinality 1:1)
Attributes: invoice_id, issue_date, total_amount
Relationship: One Invoice belongs to one booking

Class Hotel: (Cardinality 1:0)
Attributes: hotel_id, name, stars, rooms, address
Relationships: One hotel has one address, One hotel includes multiple rooms

Class Room: (Cardinality 1:1)
Attributes: room_id, room_no, price_per_night
Relationships: One Room belongs to one hotel, One Room has exactly one room type

Class Room_Type: (Cardinality 0:1)
Attributes: room_type_id, description, max_guests
Relationships: One Room_type can be associated with multiple rooms and one Room_type can have multiple facilities

Class Facilities: (Cardinality 0:1)
Attributes: facility_id, facility_name 
Relationship: One Facility can be linked to multiple room types

Das erstellte Klassendiagramm umfasste zentrale Klassen wie Hotel, Room, Guest, Booking, Invoice, RoomType, Facility und Address. Die Beziehungen zwischen den Klassen wurden anhand der Kardinalitäten modelliert: Ein Hotel hat beispielsweise genau eine Adresse und mehrere Zimmer, ein Zimmer gehört zu genau einem Hotel und ist einem bestimmten Zimmertyp zugeordnet. Gäste wiederum verfügen über genau eine Adresse und können mehrere Buchungen vornehmen. Eine Buchung wiederum ist genau einer Rechnung zugeordnet. Die Beziehung zwischen Zimmertypen und Ausstattungen wurde als Many to Many-Beziehung modelliert, realisiert durch eine Zwischentabelle.

Im Anschluss daran begannen wir mit der Implementierung der Modellklassen. Jede Klasse wurde in einer separaten .py-Datei im Ordner models gespeichert. Der Aufbau erfolgte jeweils mit einem Konstruktor (__init__), um bereits beim Erstellen eines Objekts die relevanten Werte übergeben zu können. Zusätzlich setzten wir Getter- und Setter-Methoden ein, um eine saubere Datenkapselung sicherzustellen. Dies ermöglicht uns eine kontrollierte Datenmanipulation, was insbesondere bei Benutzeraktionen, etwa durch Gäste oder Admin wichtig ist, um ungültige Werte und ungewollte Änderungen zu vermeiden.

Nach der Modellierung der Datenobjekte folgte die Umsetzung der Data-Access-Schicht. Als Grundlage diente uns eine vorgegebene Basisklasse (DB File) zur Anbindung an die SQLite-Datenbank, die wir für unsere konkreten Klassen übernehmen und erweitern konnten. In dieser Schicht wurden grundlegende Datenbankoperationen wie SELECT, INSERT, UPDATE und DELETE umgesetzt. Die Data-Access-Schicht ist rein für den Zugriff auf die Daten zuständig und enthält keine Logik.

Die fachliche Logik wurde stattdessen in der Business-Logic-Schicht (Manager-Schicht) implementiert. Diese bildet die Schnittstelle zwischen der Benutzeroberfläche und der Data-Access-Schicht. Hier werden die Regeln definiert, die festlegen, welche Aktionen ein Benutzer,je nach Rolle ausführen darf. So darf ein Gast beispielsweise eine Buchung erstellen, stornieren oder nach verfügbaren Zimmern suchen, während ein Admini Hotels, Zimmer oder Zimmertypen verwalten kann. Die Business-Logik stellt sicher, dass nur gültige, sinnvolle Operationen ausgeführt werden, und nutzt dafür gezielt Methoden der Data-Access-Schicht.

##Englisch: 

Project Approach
Our project began with the creation of a class diagram based on the provided ER model. Since the classes and their attributes were already defined, we were able to adopt them directly. Initially, we had planned to add methods as well, but we deliberately decided to define them at a later stage—specifically once it became clear which methods would actually be needed to implement the user stories.

The resulting class diagram included core classes such as Hotel, Room, Guest, Booking, Invoice, RoomType, Facility, and Address. The relationships between the classes were modeled using appropriate cardinalities: for example, a hotel has exactly one address and multiple rooms; a room belongs to exactly one hotel and is assigned to one specific room type. Guests have exactly one address and can make multiple bookings. Each booking, in turn, is associated with exactly one invoice. The many-to-many relationship between room types and facilities was modeled using a junction table.

We then proceeded with the implementation of the model classes. Each class was created in a separate .py file and stored in the models directory. Each class was constructed with an __init__ method, allowing us to pass relevant values when creating an object. Additionally, we implemented getter and setter methods to ensure clean data encapsulation. This approach helps prevent uncontrolled manipulation of object data from outside the class and ensures that values are only modified in a controlled and validated way. This is particularly important for user interactions—such as those by guests or administrators—where invalid values must be avoided.

Following the completion of the model classes, we developed the data access layer. This layer was built on top of a provided base class that handles the database connection to SQLite. We reused and extended this base class for our specific entities, enabling efficient code reuse through inheritance. The data access layer implements fundamental database operations such as SELECT, INSERT, UPDATE, and DELETE. It is responsible solely for interacting with the database and does not include any business logic.

Business logic was implemented in a separate business logic layer (also called the manager layer), which connects the data access layer with the user interface. This is where rules are defined to specify what actions a user—depending on their role—is allowed to perform. For example, a guest can make a booking, cancel a reservation, or search for available rooms, whereas an administrator can manage hotels, rooms, or room types. The business logic layer ensures that only valid and meaningful operations are executed, relying on the data access layer for database interaction.






## Minimale User Stories

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

## User Stories mit DB-Schemaänderung
1. Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer).
2. Als Gast möchte ich auf meine Buchungshistorie zuzugreifen ("lesen"), damit ich meine kommenden Reservierungen verwalten kann.\
2.1. Die Anwendungsfälle für meine Buchungen sind "neu/erstellen", "ändern/aktualisieren","stornieren/löschen".

3. Als Gast möchte ich nach meinem Aufenthalt eine Bewertung für ein Hotel abgeben, damit ich meine Erfahrungen teilen kann.

4. Als Gast möchte ich vor der Buchung Hotelbewertungen lesen, damit ich das beste Hotel auswählen kann.

5. Als Gast möchte ich für jeden Aufenthalt Treuepunkte sammeln, die ich dann für Ermässigungen einlösen kann.
Hint: Nur häufige Gäste sollten Treuepunkte erhalten. Definieren Sie eine Regel, um häufige Gäste zu identifizieren.

6. Als Gast möchte ich meine Buchung mit der von mir bevorzugten Zahlungsmethode bezahlen, damit ich meine Reservierung abschliessen kann.

## User Stories mit Datenvisualisierung
1. Als Admin möchte ich die Belegungsraten für jeden Zimmertyp in meinem Hotel sehen, damit ich weiss, welche Zimmer am beliebtesten sind und ich meine Buchungsstrategien optimiren kann.
Hint: Wählt ein geeignetes Diagramm, um die Auslastung nach Zimmertyp darzustellen (z.B. wie oft jeder Zimmertyp gebucht wird).

2. Als Admin möchte ich eine Aufschlüsselung der demografischen Merkmalde meiner Gäste sehen, damit ich gezieltes Marketing planen kann.
Hint: Wählt ein geeignetes Diagramm, um die Verteilung der Gäste nach verschiedenen Merkmalden darzustellen (z.B. Altersspanne, Nationalität, wiederkehrende Gäste). Möglicherweise müssen Sie dier Tabelle "Gäste" einige Spalten hinzufügen.

