# Node-RED Projekt: Tørring Kraftvarmeværk

## Beskrivelse
Dette Node-RED projekt samler og visualiserer data fra Tørring Kraftvarmeværk.  
Projektet indsamler data fra MQTT-sensorer, behandler dem og sender dem til en dashboard-visning med grafer og tekstfelter. Projektet inkluderer også integration med MSSQL-database og eksterne API'er (fx vejrdata via Weatherstack API).

---

## Funktioner
- Indsamling af temperatur- og tryksensordata via MQTT.
- Databehandling og konvertering af sensorværdier.
- Visualisering på Node-RED dashboard:
  - Tryk og temperatur grafiske visninger.
  - Tekstfelter for aktuelle målinger.
  - Beregning af differens mellem temperaturer (T1-T3).
- Integration med MSSQL database (`Tørring DB`).
- Hentning af vejrdata fra eksterne API’er.
- Debug nodes til overvågning af flows.

---

## Krav
- Node-RED version: 3.x eller nyere.
- Node-RED nodes:
  - `node-red-dashboard`
  - `node-red-node-mqtt`
  - `node-red-node-mssql`
  - Evt. brugerdefinerede nodes (`mqtt-processData`, `sensor-processData`)
- MQTT broker: `142.93.135.2:1883` (lokal) og `test.mosquitto.org`.
- MSSQL server: `localhost:1433`, database: `Tørring`.

---

## Installation

1. Klon repository:
```bash
git clone https://github.com/brugernavn/node-red-projekt.git
cd node-red-projekt
