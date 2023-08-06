def showDatabases():
    # return '''
    # mysql -u root << MYSQL_SCRIPT
    # SHOW DATABASES;
    # MYSQL_SCRIPT
    # '''
    return '''sudo mysql -u root -e 'show databases';'''


def exportDatabase(dbName, dbPath):
    # return f'''sudo mysqldump -u root {dbName} > '{dbPath}' --skip-dump-date; '''
    # return f'''sudo mysqldump -u root {dbName} > '{dbPath}' --skip-dump-date --extended-insert=FALSE;'''
    return f'''sudo mysqldump -u root {dbName} > '{dbPath}' --skip-dump-date --extended-insert | sed 's/),(/),\n(/g' > '{dbPath}' ;'''
