import json
from paho.mqtt import client as mqtt
from pymodbus.client import ModbusTcpClient

# --------------------------------------------------------------------
# KONFIGURATION
# --------------------------------------------------------------------
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC  = "Jakob/UR"   # Dette sætter du i Node-RED

MODBUS_HOST = "192.168.10.132"
MODBUS_PORT = 502
MODBUS_REGISTER =  0                   # Holding-register adresse


# --------------------------------------------------------------------
# Forbind til Modbus (TCP)
# --------------------------------------------------------------------
modbus = ModbusTcpClient(MODBUS_HOST, port=MODBUS_PORT)
modbus.connect()


def write_modbus(value):
    """Skriv værdi til Modbus holding register."""
    try:
        value_int = int(value)
        result = modbus.write_register(MODBUS_REGISTER, value_int)

        if result.isError():
            print("[MODBUS] Fejl ved skrivning:", result)
        else:
            print(f"[MODBUS] Skrev {value_int} til register {MODBUS_REGISTER}")

    except Exception as e:
        print("[MODBUS] Exception:", e)


# --------------------------------------------------------------------
# MQTT callbacks
# --------------------------------------------------------------------
def on_connect(client, userdata, flags, rc):
    print("[MQTT] Forbundet med kode:", rc)
    client.subscribe(MQTT_TOPIC)
    print("[MQTT] Lytter på topic:", MQTT_TOPIC)


def on_message(client, userdata, msg):
    print(f"[MQTT] Modtog fra Node-RED: {msg.payload}")

    try:
        # Hvis payload er JSON fra Node-RED
        try:
            payload = json.loads(msg.payload.decode())
            if "value" in payload:
                write_modbus(payload["value"])
                return
        except json.JSONDecodeError:
            pass

        # Hvis Node-RED sender ren streng eller tal
        write_modbus(msg.payload.decode())

    except Exception as e:
        print("[MQTT] Fejl i behandling:", e)


# --------------------------------------------------------------------
# MQTT klient
# --------------------------------------------------------------------
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(MQTT_BROKER)
mqttc.loop_forever()
