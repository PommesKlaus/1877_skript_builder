# 1877 Skript Builder

Ein einfaches Python-Skript um das Moodle-Buch zur FernUni Hagen Vorlesung *01877 Dokumenten- und Wissensmanagement im Internet* in einer (PDF-)druckbaren Website zusammenzufassen

## Hintergrund

Zu der genannten Vorlesung gibt es ein Moodle-Buch (Online-Version) sowie PDF-Dateien, die vermutlich automatisch aus dem Moodle-Buch generiert wurden. Die PDF-Versionen haben eine kleine Schriftgröße, sind nicht mit Blocksatz formatiert und haben viele Leerstellen, da jedes Kapitel erst auf einer neuen Seite beginnt. Will man das Buch z.B. auf einem Tablet lesen und mit einem Pen bearbeiten, sind diese beiden Buch-Version leider kaum geeignet.

Das vorliegende Skript greift auf das Moodle-Buch (Online-Version) zu und speichert alle Kapitel hintereinander in einer *output.html*-Datei ab. Diese Datei kann im Webbrowser geöffnet von dort aus als PDF-Datei gedruckt werden. Diese PDF-Datei behebt die oben genannten Nachteile der PDF-Version.

## Anleitung

GitHub-Repository klonen.

Sicherstellen, dass die in der Datei `requirements.txt` genannten Pakete auf dem Rechner installiert sind.

Über den Webbrowser in Moodle einloggen und aus den Cookies den Wert für *MoodleSession* in die Datei `MoodleSession_cookie.txt` kopieren.

__ACHTUNG:__ Der im Repository hinterlegte Session-Key ist eine zufällig mit Python generierte Zeichenkette, die nur ein Beispiel für das Format des Keys sein soll. Der Key muss zwingend aus dem Moodle-Cookie verwendet werden.

>__Beispiel für Google Chrome:__
>
>Nach dem Einloggen in Moodle, Entwicklertools öffnen (Google Chrome z.B. macOS: ⌥ + ⌘ + i, Windows/Linux: F12). In den Tab *Application* wechseln und dann links im Auswahlfenster unter *Cookies* den Moodle-Cookie auswählen (https://moodle-wrm.fernuni-hagen.de). Rechts erscheinen dann die für diesen Cookie hinterlegten Werte. Dort dann den Wert aus der *Value*-Spalte für den Eintrag *MoodleSession* kopieren.

Das Skript ausführen:

```
python parse.py
```

## Customizing

Über die Datei `style.css` kann die Formatierung des Buches verändert werden.

Um z.B. die Schriftgröße zu verändern, passt man einfach die `font-size` in Zeile 17 der css-Datei an.

## Rechtliches

Ich übernehme keine Haftung dafür, dass das erzeugte Buch vollständig und richtig ist. Wer auf Nummer sicher gehen will, nimmt die offizielle Version des Lehrstuhls.