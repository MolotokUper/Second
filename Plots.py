import matplotlib.pyplot as plt
measure_data = [10, 20, 30, 40, 3, 59, 2]
plt.plot(measure_data)
plt.show()

measure_data_str = [str(i) for i in measure_data]

with open("data.txt", 'w') as outfile:
    outfile.write("\n".join(measure_data_str))

