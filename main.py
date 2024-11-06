from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot


dataframe = pd.read_csv("jamb_exam_results.csv")


def plot_pie_chart(dataframe):
    bins = [0, 100, 150, 200, 250, 300, 400]
    labels = ["0-100", "101-150", "151-200", "201-250", "251-300", "301-400"]
    dataframe["Score Range"] = pd.cut(dataframe["JAMB_Score"], bins=bins, labels=labels)
    score_counts = dataframe["Score Range"].value_counts().sort_index()
    plot.figure(figsize=(6, 6))
    plot.pie(
        score_counts,
        labels=score_counts.index,
        autopct="%1.1f%%",
        startangle=180,
        colors=plot.cm.Paired.colors,
    )
    plot.title("DISTRIBUTION OF JAMB SCORES")

    plot.savefig("plots/pie_chart.png", bbox_inches="tight")
    plot.close()


plot_pie_chart(dataframe)


def plot_scatter(dataframe):

    jamb_score_mean = dataframe["JAMB_Score"].mean()
    study_hours_per_week_mean = dataframe["Study_Hours_Per_Week"].mean()
    attendance_rate_mean = dataframe["Attendance_Rate"].mean()
    jamb_score_median = dataframe["JAMB_Score"].median()

    plot.figure(figsize=(10, 6))
    plot.scatter(
        dataframe["JAMB_Score"], dataframe["Study_Hours_Per_Week"], alpha=0.7, c="green"
    )

    plot.title("Scatter Plot of JAMB Score to Study Hours Per Week")
    plot.xlabel("Jamb Score")
    plot.ylabel("Study Hours Per Week")

    stats_info = (
        f"Jamb Score Mean: {jamb_score_mean:.2f}\n"
        f"Jamb Score Median: {jamb_score_median:.2f}\n"
        f"Study Hours Per Week Mean: {study_hours_per_week_mean:.2f}\n"
        f"Attendance Rate Mean: {attendance_rate_mean:.2f}"
    )

    plot.gca().text(
        1.05,
        0.95,
        stats_info,
        transform=plot.gca().transAxes,
        fontsize=10,
        verticalalignment="top",
        horizontalalignment="left",
        bbox=dict(facecolor="white", alpha=0.5),
    )

    plot.tight_layout(pad=3)

    plot.savefig("plots/scatter.png")
    plot.close()


def plot_boxplot(dataframe):
    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    plot.figure(figsize=(12, 8))
    sns.boxplot(data=numeric_dataframe, orient="h", palette="coolwarm")

    plot.title("Box Plot with Statistics")
    plot.xlabel("Value")
    plot.ylabel("Variables")

    plot.savefig("plots/boxplot.png", bbox_inches="tight")
    plot.close()


plot_pie_chart(dataframe)
plot_scatter(dataframe)
plot_boxplot(dataframe)
