# Projekt-Python
=========

Opis
--------
W tym repozytorium znajduje się program umożliwiający monitorowanie stanu urządzeń IoT w inteligentnym domu, poprzez subskrypcję tematów na brokerze MQTT i interpretacje wiadomości
publikowanych na brokerze. 

Zależności:
------------
* PyGame
* Paho-MQTT

Instalacja i użytkowanie
------------

```
git clone https://github.com/sp9dev/Projekt-Python.git
cd Projekt-Python
python3 main.py
```
Plik config.json zawiera dane dotyczące połączenia z brokerem MQTT (Host, port, timeout, topic), a także ścieżkę obrazu zawierającego plan domu i dane dotyczące urządzeń IoT, których stan użytkownik chce monitorować. 

