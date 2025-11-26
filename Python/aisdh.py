import asyncio
import json
import paho.mqtt.client as mqtt
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusDeviceContext, ModbusServerContext, ModbusSequentialDataBlock

# --- Subclass for logging client writes ---
class LoggingDeviceContext(ModbusDeviceContext):
    def setValues(self, fx, address, values):
        # Print når Modbus client opdaterer værdier
        if fx == 1:
            print(f"[Modbus] Client skrev til coils fra adresse {address}: {values}")
        elif fx == 3:
            print(f"[Modbus] Client skrev til holding registers fra adresse {address}: {values}")
        super().setValues(fx, address, values)

# --- Opsæt 4 coils og 10 holding registers ---
store = LoggingDeviceContext(
    co=ModbusSequentialDataBlock(0, [False, False, False, False]),
    hr=ModbusSequentialDataBlock(0, [0]*10),
    ir=ModbusSequentialDataBlock(0, [0]*10),
    di=ModbusSequentialDataBlock(0, [0]*10)
)
context = ModbusServerContext(devices=store, single=True)

# --- MQTT opsætning ---
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "Jakob/UR"

def on_connect(client, userdata, flags, rc):
    print("MQTT connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    """Print og opdater Modbus ud fra MQTT payload"""
    try:
        payload = msg.payload.decode()
        print(f"Ny MQTT besked på {msg.topic}: {payload}")
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            data = payload

        # Hvis data er boolean eller enkelt værdi -> konverter til liste
        if isinstance(data, bool):
            coils = [data, False, False, False]  # sæt coil 0 til værdien
            store.setValues(1, 0, coils)
        elif isinstance(data, dict):
            if "coils" in data:
                coils = data["coils"]
                store.setValues(1, 0, coils)
            if "hr" in data:
                hr_values = data["hr"]
                store.setValues(3, 0, hr_values)

    except Exception as e:
        print(f"Fejl ved MQTT message: {e}")

# --- Start MQTT klient ---
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()  # kør MQTT i baggrunden

# --- Asyncio server ---
def run_server():
    print("Starter Modbus TCP server på 0.0.0.0:502")
    StartTcpServer(context, address=("0.0.0.0", 502))

# --- Kør server ---
run_server()
