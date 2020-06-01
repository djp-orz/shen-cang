import numpy as np
import matplotlib.pyplot as plt

'''数据和程序在同一个文件夹下面，因此不用加上数据文件所在地址'''
#res = np.loadtxt('chen rc_m errorbar.txt')
res_m = np.loadtxt('chen rc_m mean.txt')
res_e = np.loadtxt('chen rc_m std.txt')
res_m = res_m[:-2]
res_e = res_e[:-2]
#quar = []
#for i in range(len(res_m)):
#    medi = np.percentile(res[i], 50)
#    quar1 = medi - np.percentile(res[i], 25)
#    quar2 = np.percentile(res[i], 75) - medi
#    quar.append([medi, quar1, quar2])
#quar = np.array(quar).reshape(-1, 3)

Dr = np.arange(50, 401, 50)


figsize = 8, 6
fig, ax = plt.subplots(figsize=figsize)
plt.rc("font", family="Times New Roman")
fs = 24
font1 = {'family' : 'Times New Roman',  
'weight' : 'normal',  
'size'   : 16,  }
  
font2 = {'family' : 'Times New Roman',  
'weight' : 'normal',  
'size'   : fs,  
}    

ax1 = plt.subplot(111)
#plt.errorbar(Dr, res[:, 0], res[:, 1:].T, marker='o',capsize=3,markerfacecolor='b')
#plt.errorbar(Dr, quar[:, 0], quar[:, 1:].T, fmt='o-',ecolor='r',color='r',elinewidth=2,capsize=4)
plt.errorbar(Dr, res_m, res_e, fmt='o-',ecolor='r',color='r',elinewidth=2,capsize=4)
#plt.errorbar(Dr, res_m1, res_e1, fmt='o-',ecolor='b',color='b',elinewidth=2,capsize=4)
#plt.errorbar(Dr, Val_medi_m, yerr=Val_quar_m, fmt='o-',ecolor='k',color='k',elinewidth=2,capsize=4)
plt.ylabel('Valid Time(${t_v}$)', font2)
plt.xlabel(r'${D_r}$' , font2)
plt.tick_params(labelsize=fs)
ax1.set_xticks([0, 100, 200, 300, 400])
ax1.spines['bottom'].set_linewidth(2)
ax1.spines['left'].set_linewidth(2)
ax1.spines['right'].set_linewidth(2)
ax1.spines['top'].set_linewidth(2)


