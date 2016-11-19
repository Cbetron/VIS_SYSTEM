Spezifikation der VIS-Software
===============================

Date:	21.10.16
Author:	Raphael Kreft

Inhalt
=======

- Grundidee
- Anforderungen
- Aufbau bzw. Aufteilung der Softwarekomponenten



1. Grundidee
-------------
Virtuelles System zur Nutzung im alltag und am PC. Im Prinzip eine AI für Zuhause


2. Anforderungen
-----------------
Kernfunktionen:
- Suche im Internet/Dokumenten --> Datascience
- Netzwerktools
- Hacking-Tools(Mailbot, dos, bruteforce)
- ***Steuerung von Sensoren/Aktoren*** z.B wetter, Haus...
- AI-Funktionalitäten
- Sprach Ein, Ausgabe
- Steuerung über Controller(Authentifizierung)


3. Aufbau
----------
- VIS-Server auf Server: Steuert Sensoren und Aktoren, Regelt Netzwerk, Hacking... 

- VIS-Clients: Nimmt Nutzereingaben entgegen und leitet diese an einen vis-Server weiter. GUI, speaking.

--> Masterserver hört auf clients, Masterserver hat volle volle funktionalität, client nur zur Nutzerkommunikation
