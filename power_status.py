import psutil

def secs2hours(secs):
     mm, ss = divmod(secs, 60)
     hh, mm = divmod(mm, 60)
     return "%d:%02d:%02d" % (hh, mm, ss)
battery = psutil.sensors_battery()
#battery



if battery.percent<20 and battery.power_plugged==False:
    print("Feeling Hungry!!, Please plug me to Charge...")

else:
    print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
    print("Power Plugged =", battery.power_plugged)
        