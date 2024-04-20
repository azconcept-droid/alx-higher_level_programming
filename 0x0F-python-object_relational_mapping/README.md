# 0x0F. Python - Object-relational mapping
``Python`` ``OOP`` ``SQL`` ``MySQL`` ``ORM`` ``SQLAlchemy``

 **INSTALL AND ACTIVATE VENV**
<p>To create Python Vrtual Environment, allowing you to install specifci dependencies for this python project</p>

```
sudo apt-get update
```

```
sudo apt-get install python3.8-venv
```

or

```
sudo apt install python3.10-venv
```

```
python3 -m venv venv
```

```
source venv/bin/activate
```

**Install MySQLdb module version 2.0.x**
<p>For installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)</p>

```
sudo apt-get install python3-dev
```

```
sudo apt-get install libmysqlclient-dev
```

```
sudo apt-get install zlib1g-dev
```

```
sudo pip3 install mysqlclient
```

**OR**
```
pip install mysqlclient
```
**Check if it is successfully installed**
```
python3
```
>>> import MySQLdb  
>>> MySQLdb.version_info  
(2, 0, 3, 'final', 0)

**Install SQLAlchemy module version x.x.x**
```
sudo pip3 install SQLAlchemy
```
**OR**
```
pip install SQLAlchemy
```
**Check if it is successfully installed**
```
python3
```
>>> import sqlalchemy  
>>> sqlalchemy.__version__  
'1.4.22'
