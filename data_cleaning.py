# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:50:13 2020

@author: stuls
"""

import pandas as pd
import datetime
now = datetime.datetime.now()


df = pd.read_csv('glassdoor_jobs_2000.csv')
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0 )
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0 )

 

# salary parsing
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#state field 
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if ',' in x.lower() else -1)
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


#age of company 
df['age'] = df.Founded.apply(lambda x: x if x<1 else now.year - x)

#parsing of job description (python,R,etc)

##python 
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

##r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

##spark 
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

##aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

##azure
df['azure_yn'] = df['Job Description'].apply(lambda x: 1 if 'azure' in x.lower() else 0)

##SQL
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)

##excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel ' in x.lower() else 0)
df.excel_yn.value_counts()



##df.to_csv('salary_data_cleaned.csv',index = False)

