from prettytable import PrettyTable

cities = open("Resources/cities.csv", 'r')


cities = cities.readlines()

l1 = cities[0]
l1 = l1.split(',')


table = PrettyTable([l1[0], l1[1], l1[2], l1[3], l1[4], l1[5], l1[6], l1[7], l1[8], l1[9]])

for i in range(1, len(cities)) :
    table.add_row(cities[i].split(','))

code = table.get_html_string()
html_file = open('cities.html', 'w')
html_file = html_file.write(code)
