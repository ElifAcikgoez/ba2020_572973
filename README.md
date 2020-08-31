# ToDo-Liste ba2020_572973 :memo:

## Inhalt
1. [Allgemeine Informationen](#allgemeine-informationen)
2. [Informationen zur Anwendung](#informationen-zur-anwendung)
   > [Einloggen](#einloggen),<br>
   > [Todo und Bild hinzufügen](#todo-und-bild-hinzufügen),<br>
   > [Notiz hinzufügen und bearbeiten](#notiz-hinzufügen-und-bearbeiten),<br>
   > [Todo einzeln löschen](#todo-einzeln-löschen),<br>
   > [Todo als erledigt markieren](#todo-als-erledigt-markieren),<br>
   > [Todo bearbeiten](#todo-bearbeiten),<br>
   > [Alle Todos löschen](#alle-todos-löschen),<br>
   > [Nur erledigte todos löschen](#nur-erledigte-todos-löschen)<br>
   
   
3. [Technologien](#technologien)
4. [Installation](#installation)



## Allgemeine Informationen
***
<br>
Die Webapp ist an alle gerichtet, die Struktur in den Alltag einbringen möchten und soll die Möglichkeit bieten, alle anstehenden Aufgaben in eine Liste einzutragen um sie dann abarbeiten zu können. Somit soll keine Aufgabe, die für den aktuellen Tag vorgenommen wurde, vergessen werden.<br>
<br>
<b>❗️Um die Webapp benutzen zu können muss erst eingeloggt werden❗️<br>
Demo User : Maxmustermann<br>
passwort : maxmaxmax<br></b>
<br>
:globe_with_meridians: Veröffentlicht auf : https://elifacikgoeztodolist.pythonanywhere.com

## Informationen zur Anwendung
***
#### Einloggen:
Bitte zum testen/ausprobieren der Webapp den Demo User verwenden. <br>
Demo User : Maxmustermann<br>
Passwort : maxmaxmax<br>

#### Todo und Bild hinzufügen:
Auf der Startseite befindet sich die Todo-Liste wo man das eintragen kann, was man erledigen möchte. Es können beliebig viele Einträge gemacht werden und jeweils ein Bild hochgeladen werden.
Um ein Todo hinzuzufügen muss das vorhaben in das Texteingabefeld eingetippt werden. Falls Sie ein Bild hochladen wollen einfach die Datei auswählen und anschließend auf den "Hinzufügen" Button klicken : 
❗️Achtung: Eingabe nur bis zu 200 zeichen❗️




#### Notiz hinzufügen und bearbeiten:
Es kann zu jedem einzelnen Todo eine Notiz beigelegt werden. Dazu einfach erst ein Todo zur Liste hinzufügen und dann über den Todo-Text auf den "Notiz" Button klicken. Danach die gewünschte Notiz in das Textfeld eingeben und auf den "Bestätigen" Button klicken. Wenn man die Notiz umbenennen möchte, einfach nochmal auf den Button klicken und die neue Notiz eingeben.



#### Todo einzeln löschen:
Über dem Todo-Text befindet sich ein roter Mülltonenn-Icon Button, womit man jedes einzelne Todo löschen kann. Wenn man auf den Icon klickt, erscheint eine neue "Seite" und man
wird gefragt, ob man das gewählte wirklich löschen möchte. Es kann mit "Ja" bestätigt werden oder mit "Abbrechen" zurück zur Startseite geleitet werden:



#### Todo als erledigt markieren:
Man kann direkt auf den Todo-Text klicken, somit wird der Todo durchgestrichen und als "erledigt" abgespeichert.



#### Todo bearbeiten:
Auf den dunkelgrauen "Bearbeiten" Button mit dem Stift-Icon über dem gewünschten Todo-Text klicken.
Der eingetragene Todo kann im nachhinein umbenannt werden, ein Haken bei "Complete" gesetzt werden wenn es erledigt ist oder der Haken kann rausgenommen werden wenn die Aufgabe doch nicht erledigt worden ist. Wenn der Haken gesetzt wurde, erscheint der Todo-Text auf der Startseite als durchgestrichen und wenn der Haken raus ist, ist der Text wieder normal. Außerdem kann im nachhinein noch ein Bild hochgeladen werden, oder falls schon eins hochgeladen worden ist kann man dieses entfernen oder stattdessen ein anderes hochladen. Die eingetragene Notiz kann von hier aus auch bearbeitet werden. 




#### Alle Todos löschen:
Unter dem Eingabetextfeld auf den roten Button "ALLE LÖSCHEN" klicken.

#### Nur erledigte Todos löschen:
Unter dem Eingabetextfeld auf den roten Button "ERLEDIGTE LÖSCHEN" klicken.






## Technologien
***
Eine Liste mit den verwendeten Technologien in diesem Projekt:
* Verwendete Entwicklungsumgebung : [PyCharm Professional Edition Version](https://www.jetbrains.com/de-de/pycharm/) 2020.1
* [Python](https://www.python.org): Version 3.7
* [Django](https://www.djangoproject.com): Version 3.1
* [Bootstrap](https://getbootstrap.com): Version 4.3.1, 3.3.7
* HTML5
* CSS


## Installation 
***
Kleines Intro zur Installation :octocat: :
```
$ git clone https://github.com/ElifAcikgoez/ba2020_572973.git
$ (myvenv) ~/Mustermann$ python manage.py runserver
```

[Django superuser erstellen](https://docs.djangoproject.com/en/1.8/intro/tutorial02/)




