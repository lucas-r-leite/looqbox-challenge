import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
ip = os.getenv("IP")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

host = ip
database = db_name
user = db_user
password = db_pass


def main():
    try:
        # Create SQLAlchemy engine
        engine = create_engine(
            f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        )

        # Query to retrieve all data from IMDB_Movies table
        query = "SELECT * FROM IMDB_movies"

        # Load data into a pandas DataFrame
        movies_df = pd.read_sql(query, engine)

        # Top 10 Movies by Revenue
        top_revenue_movies = movies_df.sort_values(
            by="RevenueMillions", ascending=False
        ).head(10)

        # Bar Chart of Top 10 Movies by Revenue
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x="RevenueMillions",
            y="Title",
            data=top_revenue_movies,
            legend=False,
            orient="h",
        )
        plt.title("Top 10 Movies by Revenue")
        plt.xlabel("Revenue (in Millions)")
        plt.ylabel("Movie Title")
        plt.show()

        # Scatter Plot of Revenue vs. Rating
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="Rating", y="RevenueMillions", data=movies_df)
        plt.title("Revenue vs. Rating")
        plt.xlabel("IMDB Rating")
        plt.ylabel("Revenue (in Millions)")
        plt.show()

        # Count the number of movies per genre
        genre_counts = movies_df["Genre"].value_counts()

        # Select the top 10 genres
        top_10_genres = genre_counts.head(10).index
        top_10_genre_counts = genre_counts.head(10)

        # Histogram of Movie Counts by Top 10 Genre
        plt.figure(figsize=(10, 6))
        sns.barplot(
            y=top_10_genre_counts.index,
            x=top_10_genre_counts.values,
            hue=top_10_genre_counts.index,
            legend=False,
            dodge=False,
        )
        plt.title("Number of Movies by Top 10 Genre")
        plt.xlabel("Count")
        plt.ylabel("Genre")
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the database connection is properly closed
        if "engine" in locals():
            engine.dispose()
            print("Database connection closed")


# Run the main function
if __name__ == "__main__":
    main()
