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
randoms = np.random.randint(10000, size=100000)

num = 0

with open(
    "/Users/mac/Psql/ColumnOrientedDatabase/Sql/Insert/output/Insert.sql", "w"
) as f:
    for table in tables:
        for id in ids:
            text = (
                "INSERT INTO "
                + table
                + " values ("
                + id.astype("str")
                + ","
                + randoms[num].astype("str")
                + ");"
            )
            print(text, sep="\n", file=f)
            num += 1
