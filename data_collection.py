# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:45:09 2020

@author: stuls
"""


import glassdoor_scraper as gs
import pandas as pd
path = 'C:/Users/stuls/Documents/ds_salary_proj/chromedriver'

df = gs.get_jobs('data scientist',15,False,path,15)

df.to_csv('glassdoor_jobs.csv', index= False)