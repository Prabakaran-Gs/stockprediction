import pandas as pd
import datareturn 

# Create a sample DataFrame
data=datareturn.datas("AAPL")
df = pd.DataFrame(data)
# Save the DataFrame to a CSV file
df.to_csv("stock_prices.csv", index=False)
