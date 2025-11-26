# %%
from pymodbus.client import ModbusTcpClient

UR_IP = "192.168.10.132"  # UR robot IP
UR_PORT = 502           # Standard Modbus TCP port

def send_to_ur(value):
    client = ModbusTcpClient(UR_IP, port=UR_PORT)
    client.connect()
    
    # Hvis værdien er float, skal vi muligvis konvertere til int eller splitte til 2x16bit
    int_value = int(float(value))  # eksempelkonvertering
    register_address = 0            # det register du vil skrive til

    # Skriv til holding register
    client.write_register(register_address, int_value)
    
    client.close()

# %%
