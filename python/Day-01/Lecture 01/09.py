#Smart Home System

#Device Information 
device_name="Air Conditioner"  #str
device_id=2023001    #int
power_usage=3.75   # float
is_on=True   #bool
#Threshold
threshold_usage=5.0  #float

#Device Display Information
print("===SMART DEVICE STATUS===")
print("Device name :",device_name)
print("Device ID :",device_id)
print("Current Usage:",power_usage)
print("Device on :",is_on)

# check if energy usage exceeds threshold.
if power_usage > threshold_usage:
    print("Alert:High power consumption!")
else:
    print("power usage is within limit.")
    
