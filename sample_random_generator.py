from random import *
from pandas import * 

len_hf_1 = 5

def random_column(size):
    col = []
    for x in range(nb_user) :
        col.append(randint(1,size))

    return col

def generate_df_dimensions(category,size):
    return DataFrame(data={category+'_PR':random_column(size),
                           category+'_DS':random_column(size),
                           category+'_DF':random_column(size),
                           category+'_EE':random_column(size),
                           category+'_TB':random_column(size)})

def generate_data(social_aspect):
    
    #Generate data frames for Confidentiality, Integrity, Authenticity
    df_c = generate_df_dimensions(social_aspect+"_C",len_hf_1)
    df_i = generate_df_dimensions(social_aspect+"_I",len_hf_1)
    df_a = generate_df_dimensions(social_aspect+"_A",len_hf_1)
    # print(df_c)
    #Concatenate data frames to return the dataFrame for one security aspect
    frames = [df_c,df_i,df_a]
    c_df = concat(frames, axis=1)
    
    return c_df

def generate_user():
    #Skill
    skill_df = DataFrame(data=generate_data("SKILL"))
    #Experience
    exp_df = DataFrame(data=generate_data("EXPERIENCE"))

    #Concat df
    return concat([skill_df,exp_df],axis=1)



def write_to_csv(df,folder,filename):
    #Writing to csv file
    df.to_csv(f'{folder}{filename}.csv', encoding='utf-8',sep=";")

#Creating tab
nb_user = 10
user_tab = generate_user()
write_to_csv(user_tab,"generated_results/",f"data_sample_{nb_user}")
