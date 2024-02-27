import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Create a pie chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Set aspect ratio to be equal so that pie is drawn as a circle.
ax.set_aspect('equal')

# Show plot
plt.show()
