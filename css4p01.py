# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
file = pd.read_csv('movie_dataset.csv')
print(file.info())
print(file.describe())


# Rename columns by removing spaces
file.columns = file.columns.str.replace(' ', '_')

# Remove the "Rank" column if it exists
file = file.drop(columns=['Rank'], errors='ignore')

#Drop rows with missing values
file.dropna(inplace = True)
file = file.reset_index(drop=True)

# Display information about the cleaned dataset
print("\nCleaned Dataset Information:")
print(file.info())

summary_statistics = file.describe(include='all')
print("\nSummary Statistics:")
print(summary_statistics)


"""Question 1"""

# Find the highest-rated movie
highest_rated_movie = file[file['Rating'] == file['Rating'].max()]['Title'].values[0]
print("The highest-rated movie in the dataset is:", highest_rated_movie)

 
"""Question 2"""

# Calculate the average revenue
average_revenue = file['Revenue (Millions)'].mean()
print("The average revenue (in Millions) of all movies in the dataset is:", average_revenue)


"""Question 3"""

# Filter movies from 2015 to 2017 and calculate the average revenue
average_revenue_2015_to_2017 = file.loc[(file['Year'] >= 2015) & (file['Year'] <= 2017), 'Revenue (Millions)'].mean(skipna=True)
print("The average revenue of movies from 2015 to 2017 in the dataset is:", average_revenue_2015_to_2017)


"""Qusetion 4"""

import pandas as pd
file = pd.read_csv('movie_dataset.csv')

# Display unique values in the 'Year' column
unique_years = file['Year'].unique()
print("Unique years in the dataset:", unique_years)

#  Count the number of movies released in 2016
movies_2016_count = file[file['Year'].astype(str) == '2016'].shape[0]
print("The number of movies released in the year 2016 is:", movies_2016_count)

"""Question 5"""


# Count the number of movies directed by Christopher Nolan
nolan_movies_count = file[file['Director'] == 'Christopher Nolan'].shape[0]
print("The number of movies directed by Christopher Nolan is:", nolan_movies_count)


"""Question 6"""

# Count the number of movies with a rating of at least 8.0
high_rating_movies_count = file[file['Rating'] >= 8.0].shape[0]
print("The number of movies with a rating of at least 8.0 is:", high_rating_movies_count)


"""Question 7"""

# Filter movies directed by Christopher Nolan
nolan_movies = file[file['Director'] == 'Christopher Nolan']

# Calculate the median rating of Christopher Nolan's movies
nolan_median_rating = nolan_movies['Rating'].median()

print("The median rating of movies directed by Christopher Nolan is:", nolan_median_rating)


"""Question 8"""

# Group the data by year and calculate the average rating for each year
average_rating_by_year = file.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
highest_avg_rating_year = average_rating_by_year.idxmax()

print("The year with the highest average rating is:", highest_avg_rating_year)


"""Question 9"""

# Filter movies made in 2006 and 2016
movies_2006 = file[file['Year'] == 2006]
movies_2016 = file[file['Year'] == 2016]

# Calculate the number of movies made in 2006 and 2016
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print("The percentage increase in the number of movies made between 2006 and 2016 is:", percentage_increase, "%")


"""Question 10"""

from collections import Counter

# Combine all actors into a single list
all_actors = file['Actors'].str.split(',').explode().str.strip()

# Count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0][0]

print("The most common actor in all the movies is:", most_common_actor)


"""Question 11"""

# Combine all genres into a single list
all_genres = file['Genre'].str.split(',').explode().str.strip()

# Count the unique genres
unique_genres_count = all_genres.nunique()

print("The number of unique genres in the dataset is:", unique_genres_count)


"""Question 12"""

# Select numerical features for correlation analysis
numerical_features = file.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)















