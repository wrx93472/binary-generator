# Szablon (uproszczony)
import struct

class SensorData:
    def __init__(self, id, value, timestamp):
        
        self.id = id
        
        self.value = value
        
        self.timestamp = timestamp
        

    def serialize(self):
        # Format: i = int32, f = float, q = int64
        return struct.pack('ifq', self.id, self.value, self.timestamp)

    @staticmethod
    def deserialize(data):
        unpacked = struct.unpack('ifq', data)
        return SensorData(*unpacked)