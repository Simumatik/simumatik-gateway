import psutil

possible_service_names = ["s7oiehsx64", "s7oiehsx"]
service = None
for name in possible_service_names:
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))

    if service:
        break

if service:
    print("service found")
else:
    print("service not found")


if service and service['status'] == 'running':
    print("service is running")
else:
    print("service is not running")



