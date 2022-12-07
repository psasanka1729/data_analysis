import numpy as np
import matplotlib.pyplot as plt

font = {#'family' : 'Helvetica',
        #'weight' : 'bold',
        'size'   : 20}

plt.rc('font', **font)
f = plt.figure()
ax = plt.gca()
ax.tick_params(width=5)
f.set_figwidth(15)
f.set_figheight(10)
plt.xlabel("Number of Grover iterations")
plt.ylabel("Probabilitiy")
plt.xlim([0, 1000])
plt.ylim([0, 1])
Linewidth = 2
plt.legend()
plt.title("L=12, P_0 = Dashed, P_xbar = Solid, Seed = 7000")



delta1 = 0.0
P11,P12,I1 = np.loadtxt(str(delta1)+'_probability_data.txt', delimiter = '\t', unpack=True)
p11 = P11.tolist()
p12 = P12.tolist()
i1 = I1.tolist()
plt.plot(i1,p11,color='r', linestyle=":",label = str(delta1),linewidth=Linewidth)#,marker='o')
plt.plot(i1,p12,color='r',label = str(delta1),linewidth=Linewidth,marker='o')


delta2 = 'small'
P21,P22,I2 = np.loadtxt(str(delta2)+'_probability_data.txt', delimiter = '\t', unpack=True)
p21 = P21.tolist()
p22 = P22.tolist()
i2 = I2.tolist()
plt.plot(i2,p21,color='g', linestyle=":",label = str(delta2),linewidth=Linewidth)#,marker='o')
plt.plot(i2,p22,color='g',label = str(delta2),linewidth=Linewidth,marker='o')

delta3 = 0.05
P31,P32,I3 = np.loadtxt(str(delta3)+'_probability_data.txt', delimiter = '\t', unpack=True)
p31 = P31.tolist()
p32 = P32.tolist()
i3 = I3.tolist()
plt.plot(i3,p31,color='b', linestyle=":",label = str(delta3),linewidth=Linewidth)#,marker='o')
plt.plot(i3,p32,color='b',label = str(delta3),linewidth=Linewidth,marker='o')

delta4 = 0.1
P41,P42,I4 = np.loadtxt(str(delta4)+'_probability_data.txt', delimiter = '\t', unpack=True)
p41 = P41.tolist()
p42 = P42.tolist()
i4 = I4.tolist()
plt.plot(i4,p41,color='mediumvioletred', linestyle=":",label = str(delta4),linewidth=Linewidth)#,marker='o')
plt.plot(i4,p42,color='mediumvioletred',label = str(delta4),linewidth=Linewidth,marker='o')

delta5 = 0.2
P51,P52,I5 = np.loadtxt(str(delta5)+'_probability_data.txt', delimiter = '\t', unpack=True)
p51 = P51.tolist()
p52 = P52.tolist()
i5 = I5.tolist()
plt.plot(i5,p51,color='teal', linestyle=":",label = str(delta5),linewidth=Linewidth)#,marker='o')
plt.plot(i5,p52,color='teal',label = str(delta5),linewidth=Linewidth,marker='o')


delta6 = 0.3
P61,P62,I6 = np.loadtxt(str(delta6)+'_probability_data.txt', delimiter = '\t', unpack=True)
p61 = P61.tolist()
p62 = P62.tolist()
i6 = I6.tolist()
plt.plot(i6,p61,color='navy', linestyle=":",label = str(delta6),linewidth=Linewidth)#,marker='o')
plt.plot(i6,p62,color='navy',label = str(delta6),linewidth=Linewidth,marker='o')
#plt.show()
#plt.legend(loc="upper right")
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.tight_layout()
plt.savefig('12_7000_probability_time_1.png', dpi=600)#, bbox_inches='tight')