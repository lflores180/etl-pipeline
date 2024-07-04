import pandas as pd
import sqlite3

def extract_transactional_data():
    # Connect to db
    conn = sqlite3.connect("../week11/database/bootcamp_db")

    # query that extracts and transforms the data
    query = """
        select ot.*,
            case when description is null then 'UNKNOWN' else description end as description
        from online_transactions as ot
        left join (select *
                   from stock_description
                   where description <> '?') as sd on ot.stock_code = sd.stock_code
        where customer_id <> ''
            and ot.stock_code not in ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')"""

    online_transactions_fixed = pd.read_sql(query, conn)

    print("The shape of the data is", online_transactions_fixed.shape)

    return online_transactions_fixed