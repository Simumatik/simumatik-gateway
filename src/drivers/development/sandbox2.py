# #import struct
result = b'{E6AXIS: A1 7.45639801, A2 -72.6609879, A3 89.9489059, A4 17.0052299, A5 1.43585670, A6 -13.8282166, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
result = result.decode()
result = result.replace("{E6AXIS:", "")
result = result.replace("}", "")
print(result)
data = result.split(',')
data = [float(x[4:]) for x in data[:6]]
print(data)

quit()

result = b'{E6AXIS: A1 7.45639801, A2 -72.6609879, A3 89.9489059, A4 17.0052299, A5 1.43585670, A6 -13.8282166, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
result = result.decode()
#result = result.replace("{E6AXIS:", "")
#result = result.replace("", "")
print(result)
data = result.split(' \,') 
#data = [float(x[4:]) for x in data[:6]]
print(data)
