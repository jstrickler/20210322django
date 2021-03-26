import sqlite3

sql_insert = """
insert into presidents ( 
termnum, lastname, firstname, birthdate, deathdate, birthplace, birthstate, termstart, termend, party
) values (?,?,?,?,?,?,?,?,?,?)
"""

# 1:Washington:George:1732-02-22:1799-12-14:Westmoreland County:Virginia:1789-04-30:1797-03-04:no party
with sqlite3.connect('presidents.db') as pres_conn:
    pres_cursor = pres_conn.cursor()
    with open('presidents.txt') as pres_in:
        for raw_line in pres_in:
            line = raw_line.rstrip()
            fields = line.split(':')
            for i in 3, 4, 7, 8:
                if fields[i] == "NONE":
                    fields[i] = None
            pres_cursor.execute(sql_insert, fields)
            pres_conn.commit()
