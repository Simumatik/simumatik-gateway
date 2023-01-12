def readaxes():
    result = client.read('$AXIS_ACT', debug=False)
    #print(result)
    result = result.decode()
    result = result.replace("{E6AXIS:", "")
    result = result.replace("}", "")
    # print(result)
    data = result.split(',')
    return [float(x[4:]) for x in data[:6]]

import time
from py_openshowvar import openshowvar
client = openshowvar('192.168.138.128', 7000)
#client.can_connect
#print(client.can_connect)

#ov = client.read('$OV_PRO', debug=True)

result = client.write('MY_OUTPUTS', '128', debug=False)
result = client.write('MY_INPUTS', '1596', debug=False)

#result = client.write('$IN[1]', '0', debug=True)
#result = client.read('$OUT[1]', debug=True)
#result = client.read('MY_INPUTS', debug=True)
#result = client.read('MY_OUTPUTS', debug=True)


#print(result)

print(readaxes())



# counter = 0
# t = time.perf_counter()
# while time.perf_counter()-t < 100:


#     print(readaxes())


#     counter += 1
#     time.sleep(0.1)

client.close()