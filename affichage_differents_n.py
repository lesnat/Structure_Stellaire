from matplotlib import pyplot as plt
import numpy as np

results_n0=np.loadtxt("resultats_schema_gauche/resultats_n0.dat")
results_n1=np.loadtxt("resultats_schema_gauche/resultats_n1.dat")
results_n2=np.loadtxt("resultats_schema_gauche/resultats_n2.dat")
results_n3=np.loadtxt("resultats_schema_gauche/resultats_n3.dat")
results_n4=np.loadtxt("resultats_schema_gauche/resultats_n4.dat")
results_n5=np.loadtxt("resultats_schema_gauche/resultats_n5.dat")
results_n6=np.loadtxt("resultats_schema_gauche/resultats_n6.dat")
results_n7=np.loadtxt("resultats_schema_gauche/resultats_n7.dat")

z2,w_calc2,q2=results_n2.T
z3,w_calc3,q3=results_n3.T
z4,w_calc4,q4=results_n4.T
z6,w_calc6,q6=results_n6.T
z7,w_calc7,q7=results_n7.T

z0,w_calc0,w_exact0,q0=results_n0.T
z1,w_calc1,w_exact1,q1=results_n1.T
z5,w_calc5,w_exact5,q5=results_n5.T

plt.axes(xlabel='z')#,yrange=[-0.5,1.2])
plt.plot(z0,w_calc0,'.-',z1,w_calc1,'.-',z2,w_calc2,'.-',z3,w_calc3,'.-',z4,w_calc4,'.-',z5,w_calc5,'.-',z6,w_calc6,'.-',z7,w_calc7,'.-')
plt.legend(('w_calc(n=0)','w_calc(n=1)','w_calc(n=2)','w_calc(n=3)','w_calc(n=4)','w_calc(n=5)','w_calc(n=6)','w_calc(n=7)'))
plt.grid()
plt.title("Évolution de la densité adimensionnée en fonction du rayon adimensionné, pour un schéma à gauche et différents n")


plt.show()