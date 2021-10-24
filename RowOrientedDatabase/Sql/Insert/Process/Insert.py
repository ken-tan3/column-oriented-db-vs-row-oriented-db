import numpy as np

ids = np.arange(1, 10001)
randoms = np.random.randint(10000, size=100000)
random_array = list(np.array_split(randoms, 10000))

num = 0

with open(
    "/Users/mac/Psql/RowOrientedDatabase/Sql/Insert/Output/Insert.sql",
    "w",
) as f:
    for id in ids:
        text = (
            "INSERT INTO one_to_ten values ("
            + id.astype("str")
            + ","
            + ",".join(map(str, random_array[num]))
            + ");"
        )
        print(text, sep="\n", file=f)
        num += 1
