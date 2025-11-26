# PythonDLEopgaver — Oversigt og dokumentation

Dette repository indeholder flere små Python-scripts relateret til MQTT, Modbus og simple elpris-analyser. Nedenfor findes en kort dokumentation for hver Python-fil, deres formål, afhængigheder og tips til at køre dem.

--

## Fil: `aisdh.py`
- **Formål:** Kører en Modbus TCP-server (simuleret device) og lytter på MQTT for at opdatere coils / holding registers.
- **Nøgleelementer:** `LoggingDeviceContext` (logger skriverier), Modbus-datastore med coils og holding registers, MQTT klient med `on_message` der opdaterer Modbus store.
- **Afhængigheder:** `paho-mqtt`, `pymodbus`, `asyncio`, `json`.
- **Kør:** `python aisdh.py` (bemærk: binder til port 502 — kræver ofte administratorrettigheder på Windows eller brug en højere port).
- **Bemærk:** MQTT broker er sat til `test.mosquitto.org`. Payload kan være bool, dict med `coils` eller `hr`.

## Fil: `elpriser.py`
- **Formål:** Simpel analyse af elpriser gemt i `elspot.csv` (udregner gennemsnit, min, max).
- **Nøgleelementer:** Læser `elspot.csv` med `pandas`, tilføjer kolonnen `område` og udskriver statistik.
- **Afhængigheder:** `pandas`.
- **Kør:** `python elpriser.py` (kræver at `elspot.csv` eksisterer i samme mappe).

## Fil: `Grafer.py`
- **Formål:** Plotter elprisen fra `elspot.csv` med `matplotlib`.
- **Nøgleelementer:** Læser `elspot.csv`, konverterer `time_start` til datetime og laver et linjeplot af `DKK_per_kWh`.
- **Afhængigheder:** `pandas`, `matplotlib`.
- **Kør:** `python Grafer.py` (viser et plot vindue; bruges typisk i et system med grafisk environment).

## Fil: `MQTT-Modbus.py`
- **Formål:** Simpelt helper-script til at sende en værdi til en UR-enhed via Modbus TCP.
- **Nøgleelementer:** Funktion `send_to_ur(value)` som konverterer værdi og skriver til et holding register (adresse 0 som eksempel).
- **Afhængigheder:** `pymodbus`.
- **Kør:** Importer og kald `send_to_ur()` fra et andet script, eller kør interaktivt.
- **Bemærk:** IP og port er sat i variablerne `UR_IP`/`UR_PORT`.

## Fil: `NodeRed.py`
- **Formål:** En simpel MQTT-klient der lytter på et topic og printer indkommende beskeder (bruges til debugging fra Node-RED).
- **Nøgleelementer:** `on_connect` og `on_message` callbacks opsat, bruger `paho-mqtt`.
- **Afhængigheder:** `paho-mqtt`.
- **Kør:** `python NodeRed.py` (lytter kontinuerligt på `MQTT_TOPIC`).

## Fil: `test_installation.py`
- **Formål:** Eksempel på at hente elpriser fra en offentlig API (`elprisenligenu.dk`) for en given dato og gemme et CSV.
- **Nøgleelementer:** Bygger URL baseret på år og dato, henter JSON via `requests`, konverterer til `pandas.DataFrame` og gemmer `elspot.csv`.
- **Afhængigheder:** `requests`, `pandas`.
- **Kør:** Rediger parametre (`år`, `måned_dag`, `prisklasse`) og kør: `python test_installation.py`.

## Fil: `UR.py`
- **Formål:** Modtager MQTT beskeder og skriver værdier til en UR-enhed via Modbus TCP (integration til Node-RED -> Modbus).
- **Nøgleelementer:** `write_modbus(value)` funktion, MQTT `on_connect`/`on_message`, bruger `pymodbus` og `paho.mqtt`.
- **Afhængigheder:** `paho-mqtt`, `pymodbus`, `json`.
- **Kør:** `python UR.py` (kræver netværksforbindelse til den konfigurerede `MODBUS_HOST` og en MQTT broker).

--

Generelle tips
- Installer afhængigheder via `pip`, fx:

```powershell
pip install paho-mqtt pymodbus pandas matplotlib requests
```

- Hvis et script binder til port 502 (Modbus TCP), kan det kræve administratorrettigheder på Windows. Alternativt skift til en højere port til test.
- Flere scripts bruger `test.mosquitto.org` som default MQTT-broker — udskift med din egen broker hvis privat netværk kræves.

Hvis du ønsker, kan jeg:
- Tilføje eksempelkald/brugsscenarier per fil (fx sample payloads til `aisdh.py` / `UR.py`).
- Generere et `requirements.txt` med de fundne afhængigheder.
- Udbygge README med kommandoeksempler og fejlhåndteringstips.

Sig til hvad du vil have næste. 
