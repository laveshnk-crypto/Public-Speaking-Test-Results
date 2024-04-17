import matplotlib.pyplot as plt
import numpy as np

def generate_histogram(data):
    # Convert data to a NumPy array
    data_array = np.array(data)

    # Calculating the average for each question
    averages = np.mean(data_array, axis=0)

    # Questions
    questions = [f"Q{i+1}" for i in range(len(averages))]

    # Creating a list of light colors for bars
    light_colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightsalmon', 'lightpink',
                    'red', 'lightgrey', 'lightblue', 'lightskyblue', 'lightcyan',
                    'lightsteelblue', 'red', 'lightcoral', 'lightgreen', 
                    'lightblue', 'lightpink', 'lightgrey']

    # Creating the histogram
    plt.figure(figsize=(10, 6))
    bars = plt.bar(questions, averages, color=light_colors)

    # Set y-axis ceiling to 5
    plt.ylim(0, 5)

    # Adding labels and title
    plt.xlabel('Questions')
    plt.ylabel('Average Rating')
    plt.title('Average Ratings for Pre-PSAS Test')

    # Displaying the plot
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Annotate each bar with its value
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, round(height, 2), ha='center', va='bottom')
    
    plt.show()

# Sample data provided
data = [
    [3, 4, 2, 3, 1, 5, 4, 3, 1, 3, 4, 1, 2, 1, 1, 3, 4],
    [4, 3, 4, 3, 4, 5, 4, 4, 3, 3, 5, 5, 4, 3, 3, 2, 4],
    [4, 4, 4, 2, 4, 3, 3, 5, 2, 1, 5, 4, 4, 4, 2, 3, 5],
    [3, 4, 1, 2, 2, 3, 2, 2, 2, 3, 3, 5, 5, 2, 4, 3, 1],
    [4, 2, 4, 3, 2, 2, 2, 1, 4, 3, 4, 2, 5, 2, 2, 1, 2],
    [2, 1, 1, 3, 1, 4, 3, 3, 2, 1, 3, 4, 3, 1, 2, 2, 4],
    [4, 4, 4, 3, 4, 5, 2, 2, 1, 2, 5, 5, 4, 4, 2, 1, 2],
    [4, 5, 5, 3, 4, 5, 4, 4, 4, 3, 3, 4, 5, 3, 4, 2, 2]
]

generate_histogram(data)
