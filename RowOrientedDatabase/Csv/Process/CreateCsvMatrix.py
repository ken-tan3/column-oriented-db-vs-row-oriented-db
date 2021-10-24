import pandas as pd
import numpy as np

ids = pd.DataFrame({"id": np.arange(1, 10001)})
columns_data = pd.DataFrame(np.random.randint(10000, size=(10000, 10)))
data = pd.concat([ids, columns_data], axis=1)

print(data)
data.to_csv(
    "/Users/mac/Psql/RowOrientedDatabase/Csv/Output/Matrix.csv",
    header=False,
    index=False,
)
