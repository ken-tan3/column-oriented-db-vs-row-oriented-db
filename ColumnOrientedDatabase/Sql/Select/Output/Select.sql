SELECT
  one.id,
  column_1,
  column_2,
  column_3,
  column_4,
  column_5,
  column_6,
  column_7,
  column_8,
  column_9,
  column_10
FROM
  one
  INNER JOIN two ON one.id = two.id
  INNER JOIN three ON one.id = three.id
  INNER JOIN four ON one.id = four.id
  INNER JOIN five ON one.id = five.id
  INNER JOIN six ON one.id = six.id
  INNER JOIN seven ON one.id = seven.id
  INNER JOIN eight ON one.id = eight.id
  INNER JOIN nine ON one.id = nine.id
  INNER JOIN ten ON one.id = ten.id;