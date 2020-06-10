# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 




# code starts here
bank=pd.read_csv(path)

categorical_var=bank.select_dtypes(include='object')
print(categorical_var)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var)



# code ends here


# --------------
# code starts here


#code ends here
banks=bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode().loc[0]
banks=banks.fillna(bank_mode)
print(banks.isnull().sum())



# --------------
# Code starts here




avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount', aggfunc=np.mean)









# code ends here



# --------------
# code starts here



# code ends here
loan_approved_se=banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()

loan_approved_nse=banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()

percentage_se=(loan_approved_se * 100 / 614)[0]
print(percentage_se)

percentage_nse=(loan_approved_nse * 100 / 614)[0]
print(percentage_nse)




# --------------
# code starts here



loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
banks['loan_term']=banks['Loan_Amount_Term'].apply( lambda x : x/12 )
print(banks['loan_term'])
big_loan_term = banks[banks['loan_term']>=25.0].count()[0]
print(big_loan_term)


# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


