"""
Descriptive Statistics Python Pandas script.
In this script, we use the Python Pandas library to calculate descriptive
statistics on a student mental health dataset, the same way that it's done
in descriptive_stats.ipynb.

We write the results to a CSV file.
All output figures are saved to the output/ directory.
"""
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd

try:
    import lib
except ModuleNotFoundError:
    sys.path.insert(1, "./src")
    import lib

# run descriptive statistics on the age column, including mean, median,
# mode, and percentiles
def descriptive_stats(df, column):
    """Descriptive Statistics function"""
    # get mean, median, mode
    mean_val, median_val, mode_val = lib.get_mean_median_mode(df, column)
    # get percentiles
    percentile_25, percentile_50, percentile_75 = lib.get_percentiles(df, column)

    results = {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val,
        "25th_percentile": percentile_25,
        "50th_percentile": percentile_50,
        "75th_percentile": percentile_75,
    }
    return results


# create bar charts for gender, course of study, year of study,
# marital status, depression, anxiety,
# and panic attacks
def create_bar_charts(df, out_dir):
    """
    This function uses the bar_chart function form lib.py to create 7 bar
    charts in a for loop (for gender, course of study, marital status,
    depression, anxiety, and panic attacks). It saves each bar chart as
    a png file to the /output directory.
    """
    columns = [
        "Choose your gender",
        "What is your course?",
        "Your current year of Study",
        "Marital status",
        "Do you have Depression?",
        "Do you have Anxiety?",
        "Do you have Panic attack?",
    ]

    titles = [
        "Gender Distribution",
        "Course of Study Distribution",
        "Year of study Distribution",
        "Marital Status Distribution",
        "Depression Distribution",
        "Anxiety Distribution",
        "Panic Attack Distribution",
    ]

    colors = [
        ["pink", "skyblue"],
        ["blue"],
        ["green"],
        ["blue", "red"],
        ["blue", "red"],
        ["blue", "red"],
        ["blue", "red"],
    ]

    filenames = [
        "gender",
        "course",
        "year",
        "marital",
        "depression",
        "anxiety",
        "panicattack",
    ]

    # create a bar chart for each column in the columns list
    # ensure that all figures are saved to the output/ directory
    for column, title, color, filename in zip(columns, titles, colors, filenames):
        # create the bar chart
        lib.bar_chart(
            df, column, title=title, xlabel=column, ylabel="Count", color=color
        )
        # save the bar chart to the output/ directory
        figure_path = os.path.join(out_dir, f"{filename}.png")
        plt.savefig(figure_path)
        # close the figure
        plt.close()


def main():

    # read in the data
    df = pd.read_csv("../data/student_mental_health.csv")

    # get descriptive_statistics results
    res = descriptive_stats(df, "Age")

    # open md file in output/ directory
    with open("../output/descriptive_stats.md", "w") as f:
        # write the results to the md file
        f.write("## Descriptive Statistics Results\n\n")
        f.write(f"Mean: {res['mean']}\n\n")
        f.write(f"Median: {res['median']}\n\n")
        f.write(f"Mode: {res['mode']}\n\n")
        f.write(f"25th Percentile: {res['25th_percentile']}\n\n")
        f.write(f"50th Percentile: {res['50th_percentile']}\n\n")
        f.write(f"75th Percentile: {res['75th_percentile']}\n\n")

    # create bar charts and store as png in output/ directory
    create_bar_charts(df, out_dir="../output")


if __name__ == "__main__":
    main()
