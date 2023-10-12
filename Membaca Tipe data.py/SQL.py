#read_sql_table()untuk membaca SQL database table dan mempresentasikannya ke dalam bentuk pandas DataFrame.

import pandas as pd
import sqlalchemy as sqla
 
db = sqla.create_engine("sqlite:///mydata.sqlite")
 
pd.read_sql_table("table_name", db)

#read_sql_query()untuk membaca SQL query dan mempresentasikannya ke dalam bentuk pandas DataFrame.

import pandas as pd
import sqlalchemy as sqla
 
db = sqla.create_engine("sqlite:///mydata.sqlite")
 
pd.read_sql_query("SELECT * FROM table_name", db)

#read_sql()untuk membaca SQL query atau table dan mempresentasikannya ke dalam bentuk pandas DataFrame.

import pandas as pd
import sqlalchemy as sqla
 
db = sqla.create_engine("sqlite:///mydata.sqlite")
 
pd.read_sql("SELECT * FROM table_name", db)