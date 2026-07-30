print("==TRAFFIC SIGNAL STIMULATION===")

signal=input("Enter traffic signal colour:").lower()
if signal=="red":
    print("Action:STOP")
elif signal=="yellow":
    print("Action:WAIT")
elif signal=="green":
    print("Action:GO")
else:
    print("invalid signal")
   