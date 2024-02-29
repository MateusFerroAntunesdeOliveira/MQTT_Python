import paho.mqtt.client as mqtt

from .callbacks import on_connect, on_subscribe, on_message

class MqttClientConnection:
    def __init__(self, broker_ip: str, broker_port: int, client_name: str, keep_alive = 60):
        self.__broker_ip = broker_ip
        self.__broker_port = broker_port
        self.__client_name = client_name
        self.__keep_alive = keep_alive
        self.__mqtt_client = None

    def start_connection(self):
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, self.__client_name)

        # Callbacks
        mqtt_client.on_connect = on_connect
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message

        mqtt_client.connect(host = self.__broker_ip, port = self.__broker_port, keepalive = self.__keep_alive)
        self.__mqtt_client = mqtt_client
        self.__mqtt_client.loop_start()

    def stop_connection(self):
        try:
            self.__mqtt_client.loop_stop()
            self.__mqtt_client.disconnect()
            return True
        except:
            return False

