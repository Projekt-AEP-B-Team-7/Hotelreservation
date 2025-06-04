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

## Methodologie

## Teamarbeit:
Unser Team hat grundsätzlich gemeinsam gearbeitet und sich gegenseitig unterstützt, da niemand von uns einen IT-Background hatte. Anstatt feste Rollen oder Zuständigkeiten zu vergeben, haben wir uns jede Woche neue Ziele gesetzt, die wir bis zum nächsten Coaching erreichen wollten. Diese Ziele umfassten sowohl Repetition als auch das Bearbeiten konkreter Aufgaben.

Zu Beginn haben wir mit einem Projektboard gearbeitet, im weiteren Verlauf jedoch primär über WhatsApp und Microsoft Teams kommuniziert. Gegen Projektende haben wir das Board nochmals aktiv genutzt, um offene Aufgaben vor der Abgabe zu erledigen. Da alle Teammitglieder regelmässig vor Ort waren, konnten wir die Coaching-Zeit optimal nutzen, um gemeinsam weiterzuarbeiten und bei Bedarf direkt Fragen an unsere Coaches zu stellen.

# Projektziele: 
 



# Vorgehen:

Zu Beginn dieser Phase haben wir das Projekt mit GitHub und Deepnote verknüpft. Durch das bereitgestellte Einführungsvideo funktionierte dies problemlos. Da wir bereits im vorherigen Semester mit Deepnote gearbeitet hatten und damit vertraut waren, entschieden wir uns bewusst dafür, alle Bestandteile unseres Projekts, also Model, Data Access, Business Logic und User Interface, vollständig in Deepnote umzusetzen.

Zuerst haben wir den Klassendiagramms basierend auf dem vorgegebenen ER-Modell erstellt. Da die Klassen und Attribute bereits definiert waren, konnten wir diese direkt übernehmen. Ursprünglich wollten wir auch Methoden ergänzen, entschieden uns jedoch, diese erst später zu definieren. sobald klar war, welche Methoden für die Umsetzung der User Stories tatsächlich benötigt werden.


# Class Diagram

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


# Implentierung der Modelklassen: 

Im nächsten Schritt wurden die Modellklassen des Projekts im Github implentiert. 

Dabei gingen wie folgt vor:

Für jede Modellklasse wurde eine eigene .py-Datei erstellt (z. B. hotel.py, room.py) und im Ordner models gespeichert.
  
Jede Klasse wurde mit einem __init__-Konstruktor versehen. Dadurch können beim Erstellen eines Objekts direkt Werte mitgegeben werden.
Beispiel:            class Hotel:
                        def __init__(self, hotel_name, stars):
                          self.hotel_name = Royal
                          self.stars = 4
                        hotel = Hotel
                        print(hotel.hotel_name) #Ausgabe Royal

Dann wurden die Getter- und Setter-Methoden angewendet,um eine saubere Datenkapselung sicherzustellen. Damit können wir verhindern,    dass Daten von aussen unkontrolliert verändert werden. Zum Beispiel durch falsche oder ungültige Werte. Ausserdem lässt sich steuern, ob und wie jemand einen Wert lesen oder ändern darf. Das ist besonders relevant für Funktionen in unseren User Stories für Admin oder Guest. 

# Implentierung Data Access: 

Nach dem wir den "model" fertiggestellt haben, fingen wir mit der "data access" an. Die Base Data wurde uns vorgegeben, dies haben wir für unser Projekt übernommen. Mit der Base Data müssen wir den Code nicht neu schreiben und es ermmöglich uns einfach diese für weitere Klassen zu übernehemen (Vererbung). Die Data Access stellt eine Verbindung zu SQL und in diesem Layer können vor allem Daten gelesen, gelöscht oder bearbeitet werden. In diesem Layer werden vor allem Funktioniern wie Select, Insert into, Delete. Update verwendet. 

# Implentierung Business Logic: 

Im Layer Business Logic (Manager Schicht) verbindet den Data Access mit der UI. Hier wird definiert, was der USER (Admin oder Guest) machen darf. z.B. Guest darf eine Buchung stornieren,suchen,buchen usw. -> Die Methode wird dem Benutzter entsprechend zugewiesen. Die Data Access speichert oder holt Daten ohne zu wissen, ob das Sinn ergibt, dafür gibt es denn Business Logic. Dort werden die Regeln definiert. 












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

