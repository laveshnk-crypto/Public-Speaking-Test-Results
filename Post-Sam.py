import plotly.express as px
import pandas as pd

# Create a DataFrame from the provided data
def create_radar():
    data = {
        "Q1": [4, 3, 2, 4, 2, 4, 3, 5],
        "Q2": [4, 4, 2, 2, 2, 4, 2, 4],
        "Q3": [3, 3, 3, 3, 4, 3, 1, 3],
        "Q4": [4, 4, 3, 4, 2, 3, 2, 4],
        "Q5": [3, 3, 0, 4, 2, 3, 3, 4],
        "Q6": [3, 3, 0, 4, 2, 3, 0, 3]
    }

    df = pd.DataFrame(data)

    # Transpose the DataFrame
    df_transposed = df.T.reset_index()

    # Rename columns
    df_transposed.columns = ['question', 'response1', 'response2', 'response3', 'response4', 'response5', 'response6', 'response7', 'response8']

    # Melt the DataFrame
    df_melted = pd.melt(df_transposed, id_vars=['question'], var_name='respondent', value_name='response')

    # Define the categories for the radar chart
    categories = list(df_melted['question'].unique())

    # Create a list of colors for each category
    colors = px.colors.qualitative.Set1

    # Create the radar chart
    fig = px.line_polar(df_melted, r='response', theta='question', line_close=True, color='respondent', color_discrete_sequence=colors)

    # Update chart layout to remove the radial axis line and its labels
    fig.update_layout(polar=dict(radialaxis=dict(showline=False, showticklabels=False)))

    # Update traces to fill area
    fig.update_traces(fill='toself')

    fig.show()


import matplotlib.pyplot as plt

def create_bar():
    # Data
    questions = [
        "Q1",
        "Q2",
        "Q3",
        "Q4",
        "Q5",
        "Q6"
    ]

    average_scores = [3.375, 3, 2.875, 3.25, 2.75, 2.25]
    colors = ['skyblue', 'lightgreen', 'salmon', 'gold', 'lightcoral', 'darkgreen']

    # Create bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.barh(questions, average_scores, color=colors)
    
    # Bold and increase font size for question labels
    plt.xticks(fontsize=12, fontweight='bold')
    plt.yticks(fontsize=12, fontweight='bold')

    plt.xlabel('Average Score', fontsize=14, fontweight='bold')
    plt.title('Average Scores for Post-SAM', fontsize=16, fontweight='bold')
    
    plt.xlim(0, 5)  # Setting limit for x-axis
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    # Adding labels to bars
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, '{:.2f}'.format(bar.get_width()), 
                va='center', ha='left', fontsize=12, fontweight='bold', color='black')

    plt.show()



if __name__ == "__main__":
    create_radar()
    create_bar()