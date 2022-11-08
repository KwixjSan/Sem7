point_str = input("Enter lead Number:")
point_remai = int(point_str)

lead_calculation= float (point_remai -3)

has_ball = input ("Does the lead team have ball (Yes or No): ")

if has_ball== 'Yes':
	lead_calculation=lead_calculation +0.5
else:
	lead_calculation=lead_calculation -0.5
	
if lead_calculation < 0:
	lead_calculation =0
	
lead_calculation = lead_calculation** 2    #Square the number (lead_calculation)^2

second_remain= int (input ("Enter the number of the second remaining: "))

if lead_calculation > second_remain:
	print("Lead is safe")
else:
	print("Lead is not safe")
	

print(lead_calculation)
