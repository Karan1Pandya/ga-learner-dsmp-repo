# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data=np.genfromtxt(path,delimiter=",", skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census=np.concatenate([data,np.array(new_record)])
print(census)
#Code starts here



# --------------
#Code starts here
age=census[:,0]
max_age=age.max()
print(max_age)
min_age=age.min()
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=age.std()
print(age_std)


# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

length=[len_0,len_1,len_2,len_3,len_4]
dic={i:length[i] for i in range(len(length))}
minimum=[m for m in dic.keys() if dic[m]==min(length)]
minority_race=minimum[0]
print(minimum)


# --------------
#Code starts here
import numpy as np
senior_citizens=np.array(census[census[:,0]>60])
senior_citizens_len=len(senior_citizens)
working_hours_sum=0
for i in range(len(census)):
    if census[i][0]>60:
        working_hours_sum+=census[i][6]

avg_working_hours=(working_hours_sum/senior_citizens_len)
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np
high=np.array(census[census[:,1]>10])
low=np.array(census[census[:,1]<=10])
 
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])

print(high)
print(low)

print(avg_pay_high)
print(avg_pay_low)
print(avg_pay_high > avg_pay_low)


