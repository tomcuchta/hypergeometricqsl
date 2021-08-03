from mpmath import *
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pylab import rcParams
rcParams['figure.figsize'] = (7.10,5.10)


from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)


callsign="KI0Y"

def alphabetposition(c):
    if(c=="A"):
        return 6.5
    if(c=="B"):
        return 6
    if(c=="C"):
        return 5.5
    if(c=="D"):
        return 5
    if(c=="E"):
        return 4.5
    if(c=="F"):
        return 4
    if(c=="G"):
        return 3.5
    if(c=="H"):
        return 3
    if(c=="I"):
        return 2.5
    if(c=="J"):
        return 2
    if(c=="K"):
        return 1.5
    if(c=="L"):
        return 1
    if(c=="M"):
        return 0.5
    if(c=="N"):
        return 0.5
    if(c=="O"):
        return 1
    if(c=="P"):
        return 1.5
    if(c=="Q"):
        return 2
    if(c=="R"):
        return 2.5
    if(c=="S"):
        return 3
    if(c=="T"):
        return 3.5
    if(c=="U"):
        return 4
    if(c=="V"):
        return 4.5
    if(c=="W"):
        return 5
    if(c=="X"):
        return 5.5
    if(c=="Y"):
        return 6
    if(c=="Z"):
        return 6.5
    else:
        return c      
   
num_csg=[int(alphabetposition(x)) for x in callsign] #callsign as list of numbers

if len(callsign)==6:
    def base_function(z):
        return hyp2f3(num_csg[0]+1,num_csg[1]+1,num_csg[2]+1,num_csg[3]+1,num_csg[4],z**(1+abs(num_csg[5])))
if len(callsign)==5:
    def base_function(z):
        return hyper([num_csg[0]+1,num_csg[1]+1],[num_csg[2]+1,num_csg[3]+1],z**(1+abs(num_csg[4])))
if len(callsign)==4:
    def base_function(z):
        return hyper([num_csg[0]+1],[num_csg[1]+1,num_csg[2]+1],z**(1+abs(num_csg[3])))

def plotme(z):
    return base_function(z)/fabs(base_function(z))

plt.axis('off')
cplot(plotme,[-2.75,2.75],[-1.75,1.75],points=1000000)
#cplot(plotme,[-5.5,5.5],[-3.5,3.5],points=400)

ax=plt.gca()
#rect = Rectangle((-2.5,1.6),1,-1,linewidth=1,edgecolor='r',facecolor='white')
plt.text(0,1,'KE8QZC',bbox=dict(color='white', alpha=0),ha='center', va='center',fontsize=94,alpha=1)
#ax.add_patch(rect)

plt.savefig("frontside.png",bbox_inches='tight', pad_inches=0)