import numpy as np

num_array = np.arange(1, 10001)

with open(
    "/Users/mac/Psql/RowOrientedDatabase/Sql/Delete/Output/Delete.sql",
    "w",
) as f:
    for num in num_array:
        text = "DELETE FROM one_to_ten WHERE one_to_ten.id IN (" + str(num) + ");"
        print(text, sep="\n", file=f)
