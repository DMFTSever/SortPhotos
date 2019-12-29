Foto Umordner 
=============
29.12.2019
----------

SortPhotos benennt die Fotos innerhalb des Zielordnungs mit aufsteigenden
zahlen, geordnet nach dem Aufnahmedatum. Um etwaige Differenzen in der 
eingestellten Zeit der Kameras zu kompensieren gibt es die Möglichkeit
das Datum aller Fotos eines Kameratypes zu verschieben. Dabei wird nicht
das tatsächlich im File geschriebene Datum bearbeitet, sondern nur innerhalb
des Programs ein verschobenes Datum zur Ordnung verwendet.
Der Download, die Verwendung des Programmes und alle dadurch folgenden Konsequenzen
unterliegen der Verantwortung des Verwenders. 

Entwickler:
Severino Adler

Voraussetzungen:
----------------

  - Python3
  - python module: exifread, argeparse, numpy, fnmatch 

Ausführung:
-----------

  1. Kopiere alle Fotos die umbenannt werden sollen in einen neue Ordner,
     um die Originale nicht zu überschreiben.
  2. Führe das Program aus dem übergeordneten Ordner aus. Der Zielordner mit den
     Fotos wird als input übergeben.

       $ python3 \<Pfad zu SortPhotos.py\> zielordner --> führt das Programm ohne weitere optionen aus.
         
       $ python3 \<Pfad zu SortPhotos.py\> -h --> zeigt Hilfe zum Ausführen des Programmes an.
         
       $ python3 \<Pfad zu SortPhotos.py\> zielordner --info --> Zeigt Informationen zum Zielordner an ohne die Fotos umzubennen.

