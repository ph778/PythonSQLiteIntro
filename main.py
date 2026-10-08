import sqlite3

conn = sqlite3.connect('store')
print("Database has been created")

conn.execute("DROP TABLE IF EXISTS pet")

conn.execute("CREATE TABLE 'pet' (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), checkups SMALLINT UNSIGNED, birth DATE, death DATE)")

print ("Table created successfully")

conn.execute("INSERT INTO pet (name, owner, species, sex, checkups, birth, death)VALUES ('Fluffy', 'Harold', 'cat', 'f', 5, '2001-02-04','')")
conn.execute("INSERT INTO pet (name, owner, species, sex, checkups, birth, death)VALUES ('Claws', 'Gwen', 'cat', 'm', 2, '2000-03-17','')")

conn.commit
print("Records created successfully")
print("Total number of rows created:", conn.total_changes)

def print_all():

    cursor = conn.execute("SELECT name, owner, species, sex, checkups, birth, death from pet")

    for row in cursor:
        print("Name= ", row[0])
        print("Owner= ", row[1])
        print("Species= ", row[2])
        print("Sex= ", row[3])
        print("Checkups= ", row[4])
        print("Birth= ", row[5])
        print("Death= ", row[6], "\n")

def print_all_by_name(name):

    find_name = ("SELECT name, owner, species, sex, checkups, birth, death from pet WHERE name=?")

    cursor = conn.execute(find_name, (name,))

    for row in cursor:
        print("Name= ", row[0])
        print("Owner= ", row[1])
        print("Species= ", row[2])
        print("Sex= ", row[3])
        print("Checkups= ", row[4])
        print("Birth= ", row[5])
        print("Death= ", row[6], "\n")

def update_death(death, name):

    update_death = 'UPDATE pet SET death=? WHERE name=?'

    conn.execute(update_death, (death, name))
    conn.commit
    print_all_by_name(name)

def add_checkup(name, owner):
    
    find_checkups = 'SELECT checkups FROM pet WHERE name=? AND owner=?'
    add_checkup = 'UPDATE pet SET checkups=? WHERE name=? AND owner=?'
    
    cursor = conn.execute(find_checkups, (name, owner))
    result = cursor.fetchone()

    if result is not None:
        current_checkups = result[0]

        if current_checkups is None:
            current_checkups = 0

        new_checkups = current_checkups + 1
        
        conn.execute(add_checkup, (new_checkups, name, owner))

        conn.commit
        print(f"New number of checkups {new_checkups} for pet {name} owned by {owner}")
        print_all_by_name(name)

    else:
        print(f"No pet found for Owner {owner} named {name}.")
    
    

##update_death('2026-10-08', 'Fluffy')

##print_all_by_name('Fluffy')

##update_death('', 'Fluffy')

add_checkup('Claws', 'Gwen')