import numpy as np
import matplotlib.pyplot as plt 

# defining the constants
 
G = 6.674*1e-11 # in SI units 
c = 3*1e8 # in SI units
M_0 = 1.989e30 # mass of the sun 
psi_vals = np.linspace(np.radians(89), np.radians(91), 100)
# the true anomaly measured from the ascending node of the pulsar

class pulsar:
    a=8.784E8
    e=0.0878
    o=73.8
    time =22.7E-3
    i=[90.14,90.28,90.56]
    mass=1.25
    eta=45
    zeta=50
    alpha=4
    big_phi0=115
    
    def __init__(self, mass):
        self.mass=mass
    
    def axis(self, a):
        self.a = a

    def ecc(self, e):
        self.e = e

    def omega(self, o):
        self.o = o

    def angle(self, i):
        self.i = i

    def spin(self, spin):
        self.spin = spin

    def eta(self, eta):
        self.eta = eta

    def zeta(self, zeta):
        self.zeta = zeta
    
    def alpha(self, alpha):
        self.alpha = alpha

    def big_phi0(self, big_phi0):
        self.big_phi0 = big_phi0

def details(pulsar):
    print(pulsar.mass, pulsar.a, pulsar.e, pulsar.o, pulsar.i, pulsar.eta, pulsar.zeta)
    
# def amp_plot_demo(a=8.784*1e8, e=0.0878, omega=73.8, i=[90.14,90.28,90.56], M_c=1.25, flag=0): 
#     """
#     Provides amplification factor for the images plotted as a function of 
#     longitude.
#     The user has to provide information/parameters about 
#     the double pulsar system in the following order - semi 
#     major axis, eccentricity, the longitude of 
#     periastron in radians, the inclination angle of the orbital plane
#     in degrees, the mass of the companion pulsar, and a variable 'flag' 
#     which shows the plot for the dominant image if left at 
#     its default value 0 and shows the subdominant case if 
#     set to 1  
#     """

#     phi = psi_vals - np.radians(omega)*np.ones(len(psi_vals))
#     r = a*(1-e**2)/(np.ones(len(phi))+e*np.cos(phi))
#     R_g = 2*G*M_c*M_0/c**2
#     amplification = np.zeros((len(i), len(psi_vals)))
#     for j in range(len(i)):
#         R = r*(1-(np.sin(np.radians(i[j])))**2*(np.sin(psi_vals))**2)**0.5
#         a_pll = a*np.sin(np.radians(i[j]))*(1-e**2)/(1+e*np.sin(np.radians(omega)))
#         R_E = (2*R_g*a_pll)**0.5
#         u = R/R_E
#         if flag == 1:
#             amplification[j,:] = (u**2+2)/(2*u*(u**2+4)**0.5)-0.5  # dominant
#         else:
#             amplification[j,:] = (u**2+2)/(2*u*(u**2+4)**0.5)+0.5  # subdominant
#         plt.plot(np.degrees(psi_vals), amplification[j,:])
    
#     plt.xlim(89,91)
#     plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
#     if flag == 1:
#         plt.yscale('log')
#         plt.title('Sub-dominant image')
#         plt.ylabel("$A_{-}$")
#     else:
#         plt.title('Dominant image')
#         plt.ylabel("$A_{+}$")
#     plt.legend(i)
#     plt.show()


def amp_plot(pulsar, flag=0): 
    """
    Provides amplification factor for the images plotted as a function of 
    longitude.
    The user has to provide information/parameters about 
    the double pulsar system in the following order - semi 
    major axis, eccentricity, the longitude of 
    periastron in radians, the inclination angle of the orbital plane
    in degrees, the mass of the companion pulsar, and a variable 'flag' 
    which shows the plot for the dominant image if left at 
    its default value 0 and shows the subdominant case if 
    set to 1  
    """
    
    phi = psi_vals - np.radians(pulsar.o)*np.ones(len(psi_vals))
    r = pulsar.a*(1-pulsar.e**2)/(np.ones(len(phi))+pulsar.e*np.cos(phi))
    R_g = 2*G*pulsar.mass*M_0/c**2
    amplification = np.zeros((len(pulsar.i), len(psi_vals)))
    for j in range(len(pulsar.i)):
        R = r*(1-(np.sin(np.radians(pulsar.i[j])))**2*(np.sin(psi_vals))**2)**0.5
        a_pll = pulsar.a*np.sin(np.radians(pulsar.i[j]))*(1-pulsar.e**2)/(1+pulsar.e*np.sin(np.radians(pulsar.o)))
        R_E = (2*R_g*a_pll)**0.5
        u = R/R_E
        if flag == 1:
            amplification[j,:] = (u**2+2)/(2*u*(u**2+4)**0.5)-0.5  # dominant
        else:
            amplification[j,:] = (u**2+2)/(2*u*(u**2+4)**0.5)+0.5  # subdominant
        plt.plot(np.degrees(psi_vals), amplification[j,:])
    
    plt.xlim(89,91)
    plt.xlabel('$Longitude \quad (degree)$', fontsize=15)
    if flag == 1:
        plt.yscale('log')
        plt.title('Sub-dominant image')
        plt.ylabel("$A_{-}$")
    else:
        plt.title('Dominant image')
        plt.ylabel("$A_{+}$")
    plt.legend(pulsar.i)
    plt.show()


# Driver Code
# pulsar1 = pulsar(20)
# pulsar1.axis=8.784*1e8
# pulsar1.ecc=0.0878
# pulsar1.omega=73.8
# pulsar1.angle=[90.2, 90.4,91]

# details(pulsar1)
# amp_plot(pulsar1)
# amp_plot_demo()

# print(pulsar.mass)
# print(pulsar.ecc)
# pulsar.ecc=0.9
# print(pulsar.e)
# print(pulsar.ecc)
# print(pulsar.omega)
# details(pulsar)
# amp_plot(pulsar)
