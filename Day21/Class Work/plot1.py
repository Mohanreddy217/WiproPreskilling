import matplotlib.pyplot as plt

#! normal chart

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

#! line chart

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker="o", linestyle="--")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line chart")
plt.grid(True)
plt.show()

#! bar chart

# & vertical bar chart

names = ["A", "B", "C"]
scores = [80, 90, 100]
plt.bar(names, scores)
plt.title("Student scores - vertical")
plt.show()


# & horizontal bar chart

plt.barh(names, scores)
plt.title("Student scores - horizontal")
plt.show()


#! Histogram

marks = [50, 60, 80, 70, 67, 86, 32]
plt.hist(marks, bins=5)
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.title("Histogram of marks")

plt.grid(True)
plt.show()


#! Scatter

plt.scatter(x, y)
plt.show()

#! piechart

labels = ["chrome", "Firefox", "Brave"]
sizes = [20, 10, 70]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Browser usage Piechart")
plt.show()