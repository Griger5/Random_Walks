import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation  

fig = plt.figure()  
    
axis = plt.axes(xlim =(-6, 6), ylim =(-6, 6))  
  
(path,) = axis.plot([], [], lw = 3)
x = 0
y = 0
x_path = [0]
y_path = [0]
    
def init():  
    path.set_data([], []) 
    return (path,) 
   
def move(i): 
    global x,y
    angle = np.random.uniform(0, 2*np.pi)
    distance = np.random.uniform(0, 1)

    x += distance * np.cos(angle)
    y += distance * np.sin(angle)

    x_path.append(x)
    y_path.append(y)

    path.set_data(x_path, y_path)
      
    return (path,) 
   
anim = FuncAnimation(fig, move, init_func = init, frames = 100, interval = 30, blit = True) 
  
   
anim.save("2dwalk.gif", writer="ffmpeg", fps=30) 