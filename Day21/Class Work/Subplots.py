import matplotlib.pyplot as plt

# ^ both plots in one figure or one window


plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Plot1")
plt.grid()


plt.subplot(1, 2, 2)
plt.bar(["A", "B", "C"], [3, 5, 7])
plt.title("Plot2")
plt.grid()

plt.savefig("savefig.jpg")
plt.show()