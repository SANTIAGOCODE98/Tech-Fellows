from pets_db import get_connection

sql_create_favorite_foods = """
CREATE TABLE favorite_foods (
  food_id integer,
  name text,
  vegetarian integer
);
"""

with get_connection() as con:
    con.executescript(sql_create_favorite_foods)


sql_alter_tables_with_favorite_food = """
ALTER TABLE animals ADD COLUMN favorite_food_id integer;
ALTER TABLE people ADD COLUMN favorite_food_id integer;
"""

with get_connection() as con:
    con.executescript(sql_alter_tables_with_favorite_food)

sql_select_all_vegetarian_pets = """
SELECT a.name AS pet_name, ff.name AS food_name
FROM animals a
JOIN favorite_foods ff ON a.favorite_food_id = ff.food_id
WHERE ff.vegetarian = 1;
"""

with get_connection() as con:
    result = con.execute(sql_select_all_vegetarian_pets).fetchall()
    print("Mascotas vegetarianas:", result)

sql_select_all_vegetarian_pets = """
SELECT a.name AS pet_name, ff.name AS food_name
FROM animals a
JOIN favorite_foods ff ON a.favorite_food_id = ff.food_id
WHERE ff.vegetarian = 1;
"""

with get_connection() as con:
    result = con.execute(sql_select_all_vegetarian_pets).fetchall()
    print("Mascotas vegetarianas:", result)
