description = {
	1 : 'часов',
	2 : 'часа',
	3 : 'час',
	4 : 'день',
	5 : 'дня',
	6 : 'дней',
}

# дни:
def days(delta_days):
	if delta_days % 10 == 1:
		d_des = description.get(4)
		return d_des
	elif 1 < delta_days  % 10 < 5:
		d_des = description.get(5)
		return d_des
	else:
		d_des = description.get(6)
		return d_des


# часы:
def hours(delta_hours):
	if delta_hours % 10 == 1:
		h_des = description.get(3)
		return h_des
	elif 1 < delta_hours % 10 < 5:
		h_des = description.get(2)
		return h_des
	else:
		h_des = description.get(1)
		return h_des
