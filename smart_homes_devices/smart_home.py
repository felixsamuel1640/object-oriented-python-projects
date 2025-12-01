import datetime
class PowerFeatures:
    def __init__(self, status, power_source):
        self.status = status
        self.power_source = power_source

class NetworkFeatures:

    def __init__(self, wifi_name, ip_address):
        self.wifi_name = wifi_name
        self.ip_address = ip_address

class SmartHomeDevice(PowerFeatures, NetworkFeatures):
    def __init__(self, status, power_source, wifi_name, ip_address, 
device_name, room):
        PowerFeatures.__init__(self, status, power_source)
        NetworkFeatures.__init__(self, wifi_name, ip_address)
        self.device_name = device_name
        self.room = room

    def turn_on(self):
        print(f"Device name: {self.device_name} is {self.status}")

    def connect_wifi(self):
        date = datetime.datetime.today()
        print(f"Connecting {self.device_name} to {self.wifi_name}")
        print(f"Connected at {date}")

    def device_info(self):
        print(f"Device Name: {self.device_name} | Status: {self.status} | 
Power AC: {self.power_source}")
        print(f"Home WIFI: {self.wifi_name} | Room: {self.room}")


if __name__ == "__main__":
    smartdevice = SmartHomeDevice("ON", "AC", "Bells Apartment",
                                  "192.168.1.10", "SmartLight", "Bedroom")

    smartdevice.turn_on()
    smartdevice.connect_wifi()
    smartdevice.device_info()

