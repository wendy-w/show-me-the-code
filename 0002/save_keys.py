import string, random
import pymysql

def gen_keys(nums=20):
    keys = []
    for i in range(nums):
        keys.append("-".join("".join([random.choice(string.ascii_letters+string.digits) for j in range(5)]) for k in range(4)))
    #print(keys)
    return keys

def connet_db():
	conn = pymysql.connect(
		host='127.0.0.1',
		port=3306,
		user='root',
		password='wd1015wd',
		db = 'testpy',
		#charset = 'utf-8',
		)
	return conn

def save_keys_to_db(conn):
	curs = conn.cursor()
	curs.execute("DROP TABLE IF EXISTS `user_key`")
	curs.execute('''CREATE TABLE `user_key` (`key` varchar(50) NOT NULL)''')
	curs.execute("INSERT INTO `user_key` VALUES (%(value)s)",[dict(value=i) for i in keys])
	curs.execute("SELECT * FROM user_key")
	result = curs.fetchall()
	printResult(result) #printResult
    
if __name__ =="__main__":
    keys = gen_keys(200)
    conn = connet_db()
    save_keys_to_db(conn)

