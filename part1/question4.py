import pets_db


sql_pets_owned_by_nobody = """
SELECT a.name, a.species, a.age
FROM animals a
LEFT JOIN people_animals pa ON a.animal_id = pa.pet_id
WHERE pa.owner_id IS NULL;
"""


sql_pets_older_than_owner = """
SELECT COUNT(*) AS num_pets_older_than_owners
FROM animals a
JOIN people_animals pa ON a.animal_id = pa.pet_id
JOIN people p ON pa.owner_id = p.person_id
WHERE a.age > p.age;
"""

sql_only_owned_by_bessie = """ 
SELECT p.name AS person_name, a.name AS pet_name, a.species
FROM animals a
JOIN people_animals pa ON a.animal_id = pa.pet_id
JOIN people p ON pa.owner_id = p.person_id
WHERE p.name = 'bessie'
  AND NOT EXISTS (
    SELECT 1
    FROM people_animals pa2
    WHERE pa2.pet_id = a.animal_id
      AND pa2.owner_id != p.person_id
  );
"""