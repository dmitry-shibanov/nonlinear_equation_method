from lab2.Jeves import Jeves
from lab2.MyFunctions import MyFunctions
from lab2.Simplex import Simplex
import matplotlib.pyplot as plt

simplex = Simplex()
jeves = Jeves()
my_function = MyFunctions()

simplex.SimplexSearch()
my_function.figure()
jeves.HookJeves()
plt.show()