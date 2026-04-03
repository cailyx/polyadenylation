#goal- calc how many pabp's could fit in a 20-nm glob, only considering volume.
import numpy as np
import matplotlib.pyplot as plt

#diameters in nm
d_pabp = 40 ##we dont know.
d_nt = 0.3 
nt_per_pabp = 11 #pabp minimal binding size
v_max_globule = 4/3*np.pi*(d_pabp/2)**3

tail_lengths = np.arange(0,1500,1)
total_volumes = []
break_point = None

for n in tail_lengths:
  num_pabps = n/nt_per_pabp
  v_pabp = 4/3*np.pi*(d_pabp/2)**3
  v_nt = 4/3*np.pi*(d_nt/2)**3
  v_globule = num_pabps*v_pabp + (n-num_pabps)*v_nt

  if v_globule >= v_max_globule:
    break_point = n

#plot

                      
