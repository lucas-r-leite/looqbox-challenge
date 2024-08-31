import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

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

        # Query 1: Get store information
        query1 = """
        SELECT
              STORE_CODE,
              STORE_NAME,
              START_DATE,
              END_DATE,
              BUSINESS_NAME,
              BUSINESS_CODE
        FROM data_store_cad
        """

        # Query 2: Get sales data for the year 2019
        query2 = """
        SELECT
              STORE_CODE,
              DATE,
              SALES_VALUE,
              SALES_QTY
        FROM data_store_sales
        WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'
        """

        # Execute queries and load data into DataFrames
        store_df = pd.read_sql(query1, engine)
        sales_df = pd.read_sql(query2, engine)

        # Convert DATE columns to datetime format
        sales_df["DATE"] = pd.to_datetime(sales_df["DATE"])

        # Filter sales data for the specified period
        filtered_sales_df = sales_df[
            (sales_df["DATE"] >= "2019-10-01") & (sales_df["DATE"] <= "2019-12-31")
        ]

        # Merge store and sales data
        merged_df = pd.merge(filtered_sales_df, store_df, on="STORE_CODE", how="inner")

        # Calculate TM (average sales value per transaction)
        merged_df["TM"] = merged_df["SALES_VALUE"] / merged_df["SALES_QTY"]

        # Group by STORE_NAME and BUSINESS_NAME to compute the average TM
        result_df = (
            merged_df.groupby(["STORE_NAME", "BUSINESS_NAME"])
            .agg({"TM": "mean"})
            .reset_index()
        )

        # Rename columns to match desired output
        result_df.columns = ["Loja", "Categoria", "TM"]

        # Round TM to two decimal places
        result_df["TM"] = result_df["TM"].round(2)

        # Sort by "Loja" in ascending order
        result_df = result_df.sort_values(by="Loja", ascending=True)

        # Display the result table
        print(result_df)

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
