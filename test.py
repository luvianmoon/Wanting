from phue import Bridge

def get_response_from_ip(phue):
    b = Bridge('192.168.1.64')
    response = b.get_sensor_objects('phue')
    return response
print ('1')


