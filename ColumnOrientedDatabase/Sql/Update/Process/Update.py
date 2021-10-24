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
ids = np.arange(1, 10001)
randoms = np.random.randint(10000, size=10000)

with open(
    "/Users/mac/Psql/ColumnOrientedDatabase/Sql/Update/Output/Update.sql", "w"
) as f:
    for id in ids:
        num = 0
        for table in tables:
            num += 1
            text = (
                "UPDATE "
                + table
                + " SET column_"
                + str(num)
                + " = "
                + str(randoms[id - 1])
                + " WHERE "
                + table
                + ".id = "
                + str(id)
                + ";"
            )
            print(text, sep="\n", file=f)
