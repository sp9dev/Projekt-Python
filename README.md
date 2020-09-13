# Projekt-Python


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

Niestety, protokół MQTT nie posiada standaryzacji payloadów publikowanych przez urządzenia na broker MQTT, dlatego na chwilę obecną aplikacja obsluguje następujący format wiadomości:

```
{nazwa-urządzenia}:{wiadomość}
```
W pliku konfiguracyjnym można nadać urządzeniu jeden z 4 typów:
* light - urządzenie wyświetla się jako żarówka, obsługiwane wiadomości to on, off.
* sensor - urządzenie wyświetla się jako czujnik, w polu wiadomości przyjmuje dane telemetryczne i bezpośrednio wyświetla je pod ikoną po kliknięciu w nią.
* window - urządzenie wyświetla się jako okno, obsugiwane wiadomości to open, closed.
* door - urządzenie wyświetla się jako drzwi, obsugiwane wiadomości to open, closed.

Po kliknięciu na ikonę urządzenia na planie wyświetla się nad nią nazwa urządzenia, a w przypadku sensorów pod ikoną wyświetla się ostatnia odebrana wiadomość.

