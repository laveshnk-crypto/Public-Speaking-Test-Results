import matplotlib.pyplot as plt

def demographic():
    # Data
    age_data = {
        "19 - 24": 3,
        "25 - 34": 4,
        "35 - 44": 1
    }

    race_data = {
        "Asian": 3,
        "Hispanic or Latino or Spanish Origin of any race": 1,
        "White": 3,
        "Black or African American": 1,
        "Two or more races": 1
    }

    gender_data = {
        "Female": 8
    }

    # Customizing colors and font properties
    light_colors = ['#FFDAB9', '#ADD8E6', '#90EE90', '#FFC0CB', '#FFA07A']
    bold_font = {'weight': 'bold'}

    # Plotting Age
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.pie(age_data.values(), labels=age_data.keys(), autopct='%1.1f%%', startangle=140, colors=light_colors)
    plt.title('Age Distribution', fontdict=bold_font)

    # Plotting Race
    plt.subplot(1, 2, 2)
    plt.pie(race_data.values(), labels=race_data.keys(), autopct='%1.1f%%', startangle=140, colors=light_colors)
    plt.title('Race Distribution', fontdict=bold_font)

    plt.tight_layout()
    plt.show()

    # Plotting Gender
    plt.figure()
    plt.pie(gender_data.values(), labels=gender_data.keys(), autopct='%1.1f%%', startangle=140, colors=light_colors)
    plt.title('Gender Distribution', fontdict=bold_font)

    # Making values bold
    for text in plt.gca().texts:
        text.set_fontweight('bold')

    plt.show()

if __name__ == "__main__":
    demographic()
