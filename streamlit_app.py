import streamlit as st
import snowflake.connector
import pandas as pd


# Write directly to the app
st.title("Onboard-13 Sales")
st.write(
    """Counts
    """
)

conn = snowflake.connector.connect(
        user='DEPUTYUSER',
        password='wm$4Zh62',
        account='dfzqycb-tz75056',
        warehouse='COMPUTE_WH',
        database='ANALYSIS',
        schema='FACT')

cursor = conn.cursor()

query = '''
select 
concat(first_name, ' ', last_name) as name,
total_qty::integer,
total_sales::float
from analysis.fact.onboard13_sales_recent;
'''

cursor.execute(query)
result = cursor.fetchall()

df = pd.DataFrame(result,
                      columns=['Name', 'Total Quantity', 'Total Sales']).sort_values(by='Total Sales', ascending = False)

# Create a simple bar chart
# See docs.streamlit.io for more types of charts
st.subheader("Onboard-13 Sales")
st.bar_chart(data=df, x="Name", y = "Total Sales")

st.subheader("Underlying data")
st.dataframe(df, use_container_width=True, hide_index = True)