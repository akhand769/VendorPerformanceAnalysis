import pandas as pd
import sqlite3
import logging
from ingestion_db import ingest_db


def create_vendor_summary(conn):
    value = pd.read_sql_query("""
    WITH freightsummary AS (
        SELECT vendornumber, SUM(freight) AS total_freight
        FROM vendor_invoice 
        GROUP BY vendornumber
    ),
    
    purchasesummary AS (
        SELECT p.vendornumber,
               p.vendorname,
               p.brand,
               p.description,
               p.purchaseprice,
               pp.volume,
               pp.price AS actualprice,
               SUM(p.quantity) AS totalquantity,
               SUM(p.dollars) AS totalpurchasedollars
        FROM purchases p 
        JOIN purchase_prices pp 
            ON p.brand = pp.brand 
        WHERE p.purchaseprice > 0 
        GROUP BY p.vendorname, p.vendornumber, p.brand 
        ORDER BY totalpurchasedollars
    ),
    
    salessummary AS ( 
        SELECT vendorno,
               brand,
               SUM(salesdollars) AS totalsalesdollars,
               SUM(salesprice) AS totalsalesprice,
               SUM(salesquantity) AS totalsalesquantity,
               SUM(excisetax) AS totalexcisetax
        FROM sales 
        GROUP BY vendorno, brand 
        ORDER BY totalsalesprice
    )
    
    SELECT ps.vendorname,
           ps.vendornumber,
           ps.brand,
           ps.description,
           ps.purchaseprice,
           ps.volume,
           ps.actualprice,
           ps.totalquantity,
           ps.totalpurchasedollars,
           ss.totalsalesdollars,
           ss.totalsalesprice,
           ss.totalsalesquantity,
           ss.totalexcisetax,
           fs.total_freight
    FROM purchasesummary ps
    LEFT JOIN salessummary ss
        ON ps.vendornumber = ss.vendorno
       AND ps.brand = ss.brand
    LEFT JOIN freightsummary fs
        ON ps.vendornumber = fs.vendornumber
    """, conn)
    return value


def clean_data(value):
    value['volume'] = value['volume'].astype('float64')
    value.fillna(0, inplace=True)
    value['vendorname'] = value['vendorname'].str.strip()
    value['grossprofit'] = value['totalsalesdollars'] - value['totalpurchasedollars']
    value['profitmargin'] = (value['grossprofit'] / value['totalsalesdollars']) * 100
    value['stockturnover'] = value['totalsalesquantity'] / value['totalquantity']
    value['sales/purchase_ratio'] = value['totalsalesdollars'] / value['totalpurchasedollars']
    return value


if __name__ == '__main__':
    
    logging.basicConfig(
        filename="logs/get_vendor_summary.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
        
    )

    logging.info("Creating vendor summary table...")
    conn = sqlite3.connect('inventory.db')
    table = create_vendor_summary(conn)
    logging.info(f"Vendor summary created successfully. Sample:\n{table.head()}")

    logging.info("Cleaning data...")
    clean_df = clean_data(table)
    logging.info(f"Cleaned data sample:\n{clean_df.head()}")

    logging.info("Ingesting data into database...")
    ingest_db(clean_df, 'vendor_table_summary', conn)
    logging.info("Data ingested successfully into vendor_table_summary.")
