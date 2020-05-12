"""
 @DataPull.py
 
 Consists the data that is retrieved from yahoo finance and put into excel file 

"""
import pandas as pd
from pyautogui import alert

class GetSummary():
        #Function to retrieve the summary of the stock into excel file
        def get_key_summary(self,tgt_website):

            #Retrieves all tables from summary page in dataframe format by making a call to read_html function            
            df_list = pd.read_html(tgt_website)
            result_df = df_list[0]
     
            for df in df_list[1:]:
                result_df = result_df.append(df)
             
            #Taking transpose of the data to convert it into row format    
            result_df = result_df.set_index(0).T
            #Saves the result in .csv format
            result_df.to_csv('results.csv', index =False)
            alert(text='Data has been pulled to results.csv', title='Data pulled notification', button='OK')     
