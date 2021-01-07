import sqlite3 as sqlite3

class Sqlite():
    
    dbpath = "D:\courses\dersler\web-data-mining\yazganwebminingproject\data\database.sq3"
    
    def __init__(self):
        conn = sqlite3.connect(self.dbpath)
        conn.execute('CREATE TABLE IF NOT EXISTS entries (url varchar(255), keyword varchar(255))')
        print("Table created successfully")
        pass
    
    
    def save(self,url,keywords):
        isOk = False
        try:
            with sqlite3.connect(self.dbpath) as con:
                cur = con.cursor()
                for keyword in keywords:
                    cur.execute("INSERT INTO entries (url,keyword) VALUES (?,?)",(url,keyword) )
                    pass
                con.commit()
                isOk = True
                pass
        except:
            con.rollback()
            pass
        finally:
            con.close()
            pass
        
        if(isOk == True):
            return True 
        else:
            return False        
        pass
    
    
    def find(self, keywords):
        con = sqlite3.connect(self.dbpath)
        con.row_factory = sqlite3.Row
        
        cur = con.cursor()
        in_query = "select * from entries WHERE "
        for keyword in keywords:
            in_query += "( keyword LIKE "  + " '%" + keyword + "%') OR"
            pass
        in_query = in_query + "( keyword LIKE 'alper' ) ;"
            
        cur.execute(in_query)
        rows = cur.fetchall()
        
        con.close()
        return rows
    
    def all(self):
        con = sqlite3.connect(self.dbpath)
        con.row_factory = sqlite3.Row
        
        cur = con.cursor()
        cur.execute("select * from entries")
        rows = cur.fetchall()
        
        con.close()
        return rows
    pass