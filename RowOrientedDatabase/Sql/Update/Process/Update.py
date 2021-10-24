import numpy as np

ids = np.arange(1, 10001)
randoms = np.random.randint(10000, size=10000)

with open(
    "/Users/mac/Psql/RowOrientedDatabase/Sql/Update/Output/Update.sql",
    "w",
) as f:
    for id in ids:
        text = (
            "UPDATE one_to_ten SET"
            + " column_1 = "
            + str(randoms[id - 1])
            + ", column_2 = "
            + str(randoms[id - 1])
            + ", column_3 = "
            + str(randoms[id - 1])
            + ", column_4 = "
            + str(randoms[id - 1])
            + ", column_5 = "
            + str(randoms[id - 1])
            + ", column_6 = "
            + str(randoms[id - 1])
            + ", column_7 = "
            + str(randoms[id - 1])
            + ", column_8 = "
            + str(randoms[id - 1])
            + ", column_9 = "
            + str(randoms[id - 1])
            + ", column_10 = "
            + str(randoms[id - 1])
            + " WHERE one_to_ten.id = "
            + str(id)
            + ";"
        )
        print(text, sep="\n", file=f)
