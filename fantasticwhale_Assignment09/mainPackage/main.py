
#main.py

from utilsPackage.utils import get_db_connection  # Importing the connection function from utils
import pyodbc #For Question 2
import random

def fetch_data(query):
    try:
        conn= get_db_connection()
    #Submits sql to database and stores in cursor
        cursor = conn.cursor() #Temporary table
        cursor.execute('SELECT * FROM tProduct')
    except Exception as e:
        print("Error accessing database")
        print(e)
        exit() #Give up


def main():
    # 1
    query_products = """
    SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID 
    FROM tProduct
    """
    products = fetch_data(query_products)

    # 2
    if products:
        selected_product = random.choice(products) 
        ProductID = selected_product[0]  
        Description = selected_product[2]  
        ManufacturerID = selected_product[3]  
        BrandID = selected_product[4]  


if __name__ == "__main__":
    main()