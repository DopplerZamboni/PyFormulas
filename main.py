import math

a = 0
b = 0
c = 0
d = 0
m = 0
x = 0
y = 0
z = 0

def getVars():
  a = 0
  b = 0
  c = 0
  d = 0
  x = 0
  y = 0
  z = 0
  while True:
    print ("1: Quadratic Equation")
    print ("2: Pythagorean Theorem")
    print ("3: Slope from two points")
    print ("")
    type = int(input("Please enter type of equation (0 to cancel): "))
    
    if type == 0:
      print ("Thanks for using this program!")
      return
  
    elif type == 1:
      a = int(input("Enter variable a: "))
      b = int(input("Enter variable b: "))
      c = int(input("Enter variable c: "))
      quadratic(a,b,c)
    
    elif type == 2:
      side = (input("Which side is unknown? (A, B, or C)")).upper()
      if side == "A":
        a = 0
        b = int(input("Enter variable b: "))
        c = int(input("Enter variable c: "))
      
      elif side == "B":
        a = int(input("Enter variable a: "))
        b = 0
        c = int(input("Enter variable c: "))
      
      elif side == "C":
        a = int(input("Enter variable a: "))
        b = int(input("Enter variable b: "))
        c = 0
      
      else:
        print ("Invalid side!")
        return
      pythag(a,b,c,side)
    elif type == 3:
      x1 = int(input("X1? "))
      y1 = int(input("Y1? "))
      x2 = int(input("X2? "))
      y2 = int(input("Y2? "))
      slope(x1,x2,y1,y2)
    else:
      print ("Invalid Type!")
  

def quadratic(a, b, c):
  d = b**2-4*a*c
  if d < 0:
    print ("This equation has no real solutions.")
  elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print ("This equation has one real solution: " +str(x)+".")
  else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print ("This equation has two real solutions: "+str(x1)+" and "+str(x2)+".")
    print("")

def pythag(a,b,c,side):
  if side == "A":
    print ("A is",math.sqrt((c**2)-(b**2)))
    print ("")
  if side == "B":
    print ("B is",math.sqrt((c**2)-(a**2)))
    print ("")
  if side == "C":
    print ("C is",math.sqrt((a**2)+(b**2)))
    print ("")
  else:
    return
  
def slope(x1,x2,y1,y2):
  m = ((y2-y1)/(x2-x1))
  print ("")
  print ("The Slope is:",m)
  b = y1-(m*x1)
  print("The equation of your line is: y="+str(m)+"x+"+str(b))
  print("")

getVars()