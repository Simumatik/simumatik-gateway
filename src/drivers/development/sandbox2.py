import numpy

#Constants:
A = [-0.4475, 0.60479]
B = [0.15, 0.675]
ang = 10

# Calculate C position
C = [0.35 - 0.2 * numpy.cos(ang * numpy.pi / 180), 0.675 + 0.2 * numpy.sin(ang * numpy.pi/180)]

#calculate length b (A - B)

diff_x = (A[0]-B[0])
diff_y = (A[1]-B[1])

b = numpy.sqrt(pow(diff_x,2) + pow(diff_y,2))

#Calculate length a (B - C)

diff_x = (B[0]-C[0])
diff_y = (B[1]-C[1])

a = numpy.sqrt(pow(diff_x,2) + pow(diff_y,2))

#calculate length c (A - C)
diff_x = (B[0]-A[0])
diff_y = (B[1]-A[1])

c = numpy.sqrt(pow(diff_x,2) + pow(diff_y,2))

# calculate angle alpha
alpha = numpy.arccos((pow(b,2) + pow(c,2) - pow(a,2))/(2*b*c))


print(alpha*180/numpy.pi)


[0.15303844939755837, 0, 0.7097296355333861, 0.7071067805519557, 0, 0, 0.7071067818211394]


quit()

INIT_ORIGIN_CYLINDER = [-0.4475, 0, 0.60479, 0.7071067805519557, 0, 0, 0.7071067818211394]
INIT_ORIGIN_PISTON = [0.15, 0, 0.675, 0.7071067805519557, 0, 0, 0.7071067818211394]

axis_2_output

diff_x = (INIT_ORIGIN_CYLINDER[0]-INIT_ORIGIN_PISTON[0])
diff_y = (INIT_ORIGIN_CYLINDER[2]-INIT_ORIGIN_PISTON[2])

a = numpy.sqrt(pow(diff_x,2) + pow(diff_y,2))

diff_x1 = 0.2 * numpy.cos(axis_2_output)

print(c)

quit()



origin_piston = FIRST_ORIGIN_PISTON

origin_piston[0] -= 0.05

print(FIRST_ORIGIN_PISTON)



quit()




axis_offset = '0 85 -90 0 0 0'
offset = [float(value) for value in axis_offset.split()[:6]]
print(offset)

quit()


# #import struct
result = b'{E6AXIS: A1 7.45639801, A2 -72.6609879, A3 89.9489059, A4 17.0052299, A5 1.43585670, A6 -13.8282166, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
print(result)
data = [float(x[4:]) for x in result.decode().replace("{E6AXIS:", "").replace("}", "").split(',')[:6]]
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
