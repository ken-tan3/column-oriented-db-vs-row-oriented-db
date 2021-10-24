import numpy as np

tables = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]
num_array = np.arange(1, 10001)

with open(
    "/Users/mac/Psql/ColumnOrientedDatabase/Sql/Delete/Output/Delete.sql", "w"
) as f:
    for table in tables:
        for num in num_array:
            text = (
                "DELETE FROM "
                + table
                + " WHERE "
                + table
                + ".id IN ("
                + str(num)
                + ");"
            )
            print(text, sep="\n", file=f)
