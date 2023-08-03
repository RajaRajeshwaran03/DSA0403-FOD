import matplotlib.pyplot as plt

def create_rainfall_scatter_plot(months, rainfall):
    plt.figure(figsize=(10, 6))

    plt.scatter(months, rainfall, color='r', label='Rainfall (mm)')

    plt.title('Monthly Rainfall Data')
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.legend()

    plt.grid(True)

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [50, 60, 70, 80, 100, 120, 150, 140, 130, 100, 80, 60]

create_rainfall_scatter_plot(months, rainfall)
