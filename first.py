import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
ip = os.getenv("IP")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")


def retrieve_data(product_code=None, store_code=None, date=None):
    if product_code is None or store_code is None or date is None or len(date) != 2:
        raise ValueError(
            "All parameters (product_code, store_code, date) are required and date must be a list with two elements."
        )
    # Database connection details
    host = ip
    database = db_name
    user = db_user
    password = db_pass

    try:
        # Create SQLAlchemy engine
        engine = create_engine(
            f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
        )

        # Construct the query with all required parameters
        query = f"""
        SELECT *
        FROM data_product_sales
        WHERE PRODUCT_CODE = {product_code}
        AND STORE_CODE = {store_code}
        AND DATE BETWEEN '{date[0]}' AND '{date[1]}';
        """

        # Retrieve data using pandas with SQLAlchemy engine
        df = pd.read_sql(query, engine)

        print(df)

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Ensure the database connection is properly closed
        if "engine" in locals():
            engine.dispose()
            print("Database connection closed")


# Example usage
if __name__ == "__main__":
    my_data = retrieve_data(
        product_code=18, store_code=1, date=["2019-01-01", "2019-01-31"]
    )
