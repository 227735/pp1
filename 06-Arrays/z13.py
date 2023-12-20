import matplotlib.pyplot as plt

categories = ['Car', 'Public Transport', 'Bike', 'On Foot']
employees_count = [25, 19, 32, 7]

plt.bar(categories, employees_count, color=['blue', 'orange', 'green', 'red'])

plt.title('Commute Mode of Employees')
plt.xlabel('Commute Mode')
plt.ylabel('Number of Employees')

plt.show()