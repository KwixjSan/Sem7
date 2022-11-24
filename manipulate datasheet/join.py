my_str=' This is a test'
string_elements = my_str.split()

string_elements
#['This','is','a','test']

reversed_elements =[]
for element in string_elements:
	reversed_elements.append(element[::-1])
reversed_elements
#['sihT', 'si', 'a', 'eert']
new_str= "".join(reversed_elements)
new_str
#'sihTsiaeert'
new_str= " ".join(reversed_elements)
new_str
#'sihT si a eert'
