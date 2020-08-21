from Connection import Connection
from InterfaceCarBrand import CarBrand
from InterfaceEmploye import InterfaceEmploye, Doctor, Worker, Cleaner, Employe

# 1
con = Connection().json('{"user": "jesiel", "password": "1234", "port": "5432", "host": "localhost"}')
print(vars(con))
con2 = Connection().xml("connection",
    "<connection>"
    "   <user>curvello</user>"
    "   <password>123456</password>"
    "   <host>curvello</host>"
    "   <port>curvello</port>"
    "</connection>")
print(vars(con))
con2.user = "leonardo"
print(vars(con))

# 2 a
print()
# Fiz algo diferente para evitar ifs, n sei se é bom para uma app de vdd
fd = Employe('1')
fd.info()
fw = Employe('2')
fw.info()
fc = Employe('3')
fc.info()
# 2 b
print()
fiat = CarBrand('uno')
fiat.info()
wolks = CarBrand('fusca')
wolks.info()
ford = CarBrand('kkk')
ford.info()
