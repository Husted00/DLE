# %%
from paho.mqtt import client as mqtt

# -----------------------------------------------------
# KONFIGURATION
# -----------------------------------------------------
MQTT_BROKER = "test.mosquitto.org"        # IP på din MQTT broker
MQTT_TOPIC  = "Jakob/UR"     # Det topic du sender fra Node-RED


# -----------------------------------------------------
# CALLBACK når Python forbinder
# -----------------------------------------------------
def on_connect(client, userdata, flags, rc):
    print("[MQTT] Forbundet:", rc)
    client.subscribe(MQTT_TOPIC)
    print("[MQTT] Lytter på topic:", MQTT_TOPIC)


# -----------------------------------------------------
# CALLBACK når der kommer en besked
# -----------------------------------------------------
def on_message(client, userdata, msg):
    print(f"[MQTT] Modtaget fra Node-RED:")
    print(f"Topic : {msg.topic}")
    print(f"Payload: {msg.payload.decode()}")
    print("------------------------------")


# -----------------------------------------------------
# START MQTT CLIENT
# -----------------------------------------------------
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(MQTT_BROKER)
mqttc.loop_forever()

# %%
