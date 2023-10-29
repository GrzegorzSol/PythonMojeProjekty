class Base:
  @staticmethod
  def metoda_base():
    print("Klasa Base")

class testclass(Base):
  def __init__(self, _a: int, _b: int):
    self.a: int = _a
    self.b: int = _b
    self.__c: int = 999  # skaładowa prywatna
    self.d: int = 100

  # def __getattr__(self, item):
  #   print("__getattr__: {}".format(item))
  #   return self.__dict__[item]
  #
  # def __getattribute__(self, name):
  #   print("__getattribute__: {}".format(name))
  #   return object.__getattribute__(self, name)
  #
  # def __setattr__(self, key, value):
  #   print("__setattr__: key: {}, value: {}".format(key, value))
  #   self.__dict__[key] = value

  @staticmethod
  def mystatic():
    print("Metoda statyczna")

  @property
  def sg_c(self):
    print("Odczyt dla self.c")
    return self.__c

  @sg_c.setter
  def sg_c(self, value):
    print("Zapis dla self.__c")
    self.__c = value

tclass = testclass(1234, 5678)
# tclass.a

# print(f"{tclass.a=}, {tclass.b=}, {tclass.d=}")

print("testclass.__dict__: {}".format(testclass.__dict__))
print("testclass.__mro__: {}".format(testclass.__mro__))

# testclass.mystatic()
print("self.__c: {}".format(tclass.sg_c))
tclass.sg_c = 55
print("self.__c: {}".format(tclass.sg_c))
tclass.metoda_base()
