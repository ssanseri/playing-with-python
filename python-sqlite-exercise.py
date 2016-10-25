import sqlite3

rosterValues = (
    ('Jean-Baptiste Zorg','Human',122),
    ('Korben Dallas', 'Meat Popsicle', 100),
    ('Ak''not','Mangalore', -5)
)

with sqlite3.connect(":memory:") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?,?,?)", rosterValues)

    # Change Korben Dallas's species to Human
    c.execute("UPDATE Roster SET Species=? WHERE Name=?",
              ('Human','Korben Dallas'))
    
    # select all Names and IQs from Roster whenever the species is human
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")

    for row in c.fetchall():
        print (row)




