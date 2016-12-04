for i in range(0,14):
    userid = str(13111111111+i)
    name = "doge"+str(i)
    user="INSERT INTO users(userid,username,password) VALUES ('"+userid+"','"+name+"','123456');"
    print user