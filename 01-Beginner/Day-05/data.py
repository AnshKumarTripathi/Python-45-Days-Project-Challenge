# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Matplotlib Basics
# ==================
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
# It is highly customizable, allowing detailed control over the plot appearance.
# Basic plots in matplotlib include line plots, scatter plots, bar charts, histograms, and pie charts.
# The figure and axes are the main elements in a matplotlib plot. The figure is the overall window or page,
# and the axes are the individual plots within the figure.

# Example of a simple line plot using matplotlib
plt.figure(figsize=(10, 6))  # Create a figure with a specific size
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, label='x vs y', color='blue', marker='o')  # Plotting the data with labels and styling
plt.title('Simple Line Plot')  # Adding a title to the plot
plt.xlabel('X-axis Label')  # Adding a label to the x-axis
plt.ylabel('Y-axis Label')  # Adding a label to the y-axis
plt.legend()  # Display the legend
plt.grid(True)  # Adding a grid to the plot
plt.show()  # Display the plot

# Seaborn Basics
# ===============
# Seaborn is built on top of matplotlib and provides a high-level interface for drawing attractive statistical graphics.
# It is particularly useful for visualizing complex datasets.
# Seaborn includes several built-in themes that improve the aesthetic appeal of plots.
# It also provides functions for creating commonly used visualizations such as box plots, violin plots, and heatmaps.

# Example of a simple scatter plot using seaborn
sns.set(style="darkgrid")  # Set the aesthetic style of the plots
tips = sns.load_dataset("tips")  # Load an example dataset provided by seaborn
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='time')  # Create a scatter plot with hue based on 'time'
plt.title('Scatter Plot of Total Bill vs Tip')  # Adding a title to the plot
plt.xlabel('Total Bill')  # Adding a label to the x-axis
plt.ylabel('Tip')  # Adding a label to the y-axis
plt.show()  # Display the plot

# Key Differences and Complementarity
# ====================================
# While matplotlib is highly customizable and allows for fine-grained control over the plot elements,
# seaborn simplifies the process of creating aesthetically pleasing and informative statistical plots with fewer lines of code.
# Seaborn integrates seamlessly with pandas dataframes and is particularly powerful for visualizing data distributions and relationships.

# When to Use Matplotlib:
# - When detailed customization and control over every aspect of the plot is required.
# - For creating complex figures with multiple subplots and intricate layouts.

# When to Use Seaborn:
# - For quick and aesthetically pleasing statistical plots.
# - When working with pandas dataframes and needing to visualize data distributions and relationships.

# In practice, matplotlib and seaborn are often used together to leverage the strengths of both libraries.
