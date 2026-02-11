import matplotlib.pyplot as plt
import seaborn as sns


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 27000, 30000, 28000, 32000, 31000]

plt.plot(months, sales)
plt.title("Line chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("Q1_linechart.png")
plt.show()

sns.barplot(x=months, y=sales)
plt.title("Seaborn bar plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("Q1_barplot.png")
plt.show()