"""Core Skills Drill — Descriptive Analytics

Compute summary statistics, plot distributions, and create a correlation
heatmap for the sample sales dataset.

Usage:
    python drill_eda.py
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def compute_summary(df):
    """Compute summary statistics for all numeric columns.

    Args:
        df: pandas DataFrame with at least some numeric columns

    Returns:
        DataFrame containing count, mean, median, std, min, max
        for each numeric column. Save the result to output/summary.csv.
    """
    # TODO: Compute descriptive statistics (count, mean, median, std, min, max)
    #       for all numeric columns and save to output/summary.csv
    
    numeric_df = df.select_dtypes(include='number')
    
    summary = numeric_df.describe().T
    
    summary['median'] = numeric_df.median()
    
    summary = summary[['count', 'mean', 'median', 'std', 'min', 'max']]
    
    os.makedirs('output', exist_ok=True)
    
    summary.to_csv('output/summary.csv')
    
    return summary
    


def plot_distributions(df, columns, output_path):
    """Create a 2x2 subplot figure with histograms for the specified columns.

    Args:
        df: pandas DataFrame
        columns: list of 4 column names to plot (use numeric columns)
        output_path: file path to save the figure (e.g., 'output/distributions.png')

    Returns:
        None — saves the figure to output_path
    """
    # TODO: Create a 2x2 figure with sns.histplot (KDE overlay) for each column
    #       Add titles, labels, and tight layout before saving
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    
    axes = axes.flatten()
    
    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    
    plt.tight_layout()
    
    os.makedirs('output', exist_ok=True)
    
    fig.savefig(output_path, dpi=150)
    
    plt.close()


def plot_correlation(df, output_path):
    """Compute Pearson correlation matrix and visualize as a heatmap.

    Args:
        df: pandas DataFrame with numeric columns
        output_path: file path to save the figure (e.g., 'output/correlation.png')

    Returns:
        None — saves the figure to output_path
    """
    # TODO: Compute the correlation matrix for numeric columns and
    #       visualize it as an annotated Seaborn heatmap
    
    numeric_df = df.select_dtypes(include='number')
    
    corr_matrix = numeric_df.corr()
    
    # رسم heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        ax=ax
    )
    
    ax.set_title('Correlation Heatmap')
    
    plt.tight_layout()
    
    os.makedirs('output', exist_ok=True)
    
    fig.savefig(output_path, dpi=150)
    
    plt.close()


def main():
    """Load data, compute summary, and generate all plots."""
    os.makedirs("output", exist_ok=True)

    # TODO: Load the CSV from data/sample_sales.csv
    # TODO: Call compute_summary and save the result
    # TODO: Choose 4 numeric-friendly columns and call plot_distributions
    # TODO: Call plot_correlation
    
    
    os.makedirs("output", exist_ok=True)

    df = pd.read_csv("data/sample_sales.csv")
    
    df['revenue'] = df['quantity'] * df['unit_price']

    compute_summary(df)

    # Task 2: Distribution plots
    plot_distributions(
        df,
        columns=['quantity', 'unit_price', 'revenue', 'quantity'],  
        output_path='output/distributions.png'
    )


    # Task 3: Correlation heatmap
    plot_correlation(df, output_path='output/correlation.png')




if __name__ == "__main__":
    main()
