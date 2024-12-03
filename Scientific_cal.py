import math

#Frequency
def freq_converter(value, from_frq, to_freq):
    metric_dict = {
        'Hz': 10**0,
        'kHz': 10**3,
        'MHz': 10**6,
        'GHz': 10**9
    }

    if from_frq not in metric_dict or to_freq not in metric_dict:
        return "Enter a valid format"

    result = value * (metric_dict[from_frq] / metric_dict[to_freq])
    return result

#Metric
def metric_converter(value, from_unit, to_unit):
    metric_dict = {
        'pico': 10**-12,
        'nano': 10**-9,
        'micro': 10**-6,
        'milli': 10**-3,
        'base': 10**0,
        'Kilo': 10**3,
        'Mega': 10**6,
        'Giga': 10**9,
        'Tera': 10**12,
        'Peta': 10**15
    }

    if from_unit not in metric_dict or to_unit not in metric_dict:
        return "Enter a valid format"

    result = value * (metric_dict[from_unit] / metric_dict[to_unit])
    return result

#Spped distance and time
def speed(dis, tim):
  spd = dis / tim
  return spd

def time(dis , spd):
  tim = dis / spd
  return tim

def distance(sped , time):
  dist = sped * time
  return dist

def escape_velocity(planet):
  km = {
      'Mercury' : 4.25 ,
      'Venus': 10.36,
      'Earth': 11.19,
      'Mars':  5.03 ,
      'Jupiter': 59.5,
      'Saturn': 35.5 ,
      'Uranus': 21.3,
      'Neptune': 23.5,
  }
  if planet not in km:
      print("not valid")
  result = f'{km[planet]}kms'
  return result

def cal_escape(G ,m,r):
  """
      Arguments :
                  G = Gravitational_Constant(int)
                  m=  Planet_Mass(int)
                  r = Planet_Radius(int)
  """
  vesc = (2*G*m/r)**0.5
  return vesc

def Newton2nd(m ,a):
  f = m*a
  return f

def gravitational_force(Gravitational_Constant, m1 , m2 ,r):
   G  = Gravitational_Constant
   f = (G * m1 * m2 / r**2)
   return f

def tension(m,g,a):
  t = m*g + m*a
  return t

def Einstein_Mass_Energy(m):
  c = 3*10**8
  E= m*c**2
  return E

def cmyk_rgb(c,m,y,k):
  R = round(255 * (1-c) * (1-k))
  G = round(255 * (1-m) * (1-k))
  B = round(255 * (1-y) * (1-k))
  return R,G,B

#Series and Parallel
def series_resistor(*arwg):
   total = 0
   for num in arwg:
        total += num
   return total
def parllel_resisror(*args):
    total_inverse = sum(1 / resistance for resistance in args)
    total_resistance = 1 / total_inverse
    return total_resistance

def series_inductor(*args):
   total = 0
   for num in args:
        total += num
   return total

def parallel_inductor(*args):
   invers = sum(1/ inductance for inductance in args)
   total = 1/invers
   return total

def series_capacitor(*args):
  cap = sum(1/ capacitance for capacitance in args)
  total = 1/cap
  return total

def parallel_capacitor(*args):
  total = sum(cap for cap in args)
  return total

#Wheatstone bridge
def wheatstone_bal(R1,R2,R3):
   Rx = (R2*R3)/R1
   return f"{Rx} ohms"

def ohmslaw(type=str,V=int,I=int,R=int):
  #Current
  if type == "Current":
    if V | R is None:
      print("Enter a valid input")
    else :
      return f'{V/R} ohm'
    
  #Voltage
  if type == "Voltage":
    if I | R is None:
      print("Enter a valid input")
    else :
      return f'{I*R} volts'
    
    #Resistance
  if type == "Resistance":
    if V | I is None:
      print("Enter a valid input")
    else :
      return f'{V/I} ohm'
def powerlaw(type=str,V=int,I=int,P=int):
    #Current
  if type == "Current":
    if V | P is None:
      print("Enter a valid input")
    else :
      return f'{P/V} A'
    
  #Voltage
  if type == "Voltage":
    if P | I is None:
      print("Enter a valid input")
    else :
      return f'{P/I} volts'
    
    #Power
  if type == "Power":
    if V | I is None:
      print("Enter a valid input")
    else :
      return f'{V*I} watt'