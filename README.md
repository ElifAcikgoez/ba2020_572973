# ToDo-Liste ba2020_572973 :memo:

## Inhalt
1. [Allgemeine Informationen](#allgemeine-informationen)
2. [Informationen zur Anwendung](#informationen-zur-anwendung)
   > [Einloggen](#einloggen),<br>
   > [Todo hinzufügen](#todo-hinzufügen),<br>
   > [Notiz hinzufügen](#notiz-hinzufügen),<br>
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
Die Webapp ist an alle gerichtet ,die Struktur in den Alltag einbringen möchten und soll die Möglichkeit bieten, alle anstehenden Aufgaben in eine Liste einzutragen um sie dann abarbeiten zu können. Somit soll keine Aufgabe , der für den aktuellen tag vorgenommen wurde ,vergessen werden.<br>
<br>
<b>❗️Um die Webapp benutzen zu können muss erst eingeloggt werden❗️<br>
Demo User : MaxMustermann<br>
passwort : maxmaxmax<br></b>
<br>
:globe_with_meridians: Veröffentlicht auf :  https://todolistelif.pythonanywhere.com

## Informationen zur Anwendung
***
#### Einloggen:
Bitte zum testen/ausprobieren der Webapp den Demo User verwenden. <br>
Demo User : MaxMustermann<br>
passwort : maxmaxmax<br>

#### Todo hinzufügen:
Auf der Startseite befindet sich die Todo-Liste wo man das eintragen kann, was man erledigen möchte. Es können beliebig viele einträge gemacht werden.
Um ein Todo hinzuzufügen muss das vorhaben in das Texteingabefeld eingetippt werden und anschließend auf den "Hinzufügen" button gegklickt werden: 
❗️Achtung: Eingabe nur bis zu 200 zeichen❗️




#### Notiz hinzufügen:



#### Todo einzeln löschen:
Über dem todo-text befindet sich ein roter Mülltonenn-icon Button, womit man jedes einzelne todo löschen kann. Wenn man auf den icon klickt, erscheint eine neue "seite" und 
wird gefragt ob man das gewählte wirklich löschen möchte. Es kann mit "Ja" bestätigt werden oder mit "Abbrechen" zurück zur startseite geleitet werden :



#### Todo als erledigt markieren:
Man kann direkt auf den Todo-text klicken , somit wird der todo durchgestrichen und als "erledigt" abgespeichert.



#### Todo bearbeiten:
Auf den dunkelgrauen "Bearbeiten" Button mit dem stift-icon über dem gewünschten todo-text klicken.
Der eingetragene todo kann im nachhinein umbenannt werden ,  ein hacken bei "Complete" gesetzt werden wenn es erledigt ist oder der hacken kann rausgenommen werden wenn die aufgabe doch nicht erledigt worden ist. Wenn der hacken gesetzt wurde, erscheint der todo-text auf der startseite als durchgestrichen und wenn der hacken raus ist , ist der text wieder normal.




#### Alle Todos löschen:
Unter dem Eingabetextfeld auf den roten Button "ALLE LÖSCHEN" klicken.

#### Nur erledigte Todos löschen:
Unter dem Eingabetextfeld auf den roten Button "ERLEDIGTE LÖSCHEN" klicken.






## Technologien
***
Eine Liste mit den verwendeten technologien in diesem Projekt:
* Verwendete Entwicklungsumgebung : [PyCharm Professional Edition Version](https://www.jetbrains.com/de-de/pycharm/) 2020.1
* [Python](https://www.python.org): Version 3.7
* [Django](https://www.djangoproject.com): Version 3.1
* [Bootstrap](https://getbootstrap.com): Version 4.3.1, 3.3.7
* HTML5
* CSS


## Installation 
***
Kleines Intro zur installation :octocat: :
```
$ git clone https://github.com/ElifAcikgoez/ba2020_572973.git
$ (myvenv) ~/Mustermann$ python manage.py runserver
```

[Django superuser erstellen](https://docs.djangoproject.com/en/1.8/intro/tutorial02/)




