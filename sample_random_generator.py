from random import *
from pandas import * 

len_hf_1 = 5

def random_column(size):
    col = []
    for x in range(nb_user) :
        col.append(randint(1,size))

    return col

def generate_df_dimensions(category,size):
    return DataFrame(data={category+'_PC':random_column(size),
                           category+'_AC':random_column(size),
                           category+'_CO':random_column(size),})

def generate_data(social_aspect):
    
    #Generate data frames for Confidentiality, Integrity, Authenticity
    df_c = generate_df_dimensions(social_aspect+"_C",len_hf_1)
    df_i = generate_df_dimensions(social_aspect+"_I",len_hf_1)
    df_a = generate_df_dimensions(social_aspect+"_A",len_hf_1)

    #Concatenate data frames to return the dataFrame for one security aspect
    frames = [df_c,df_i,df_a]
    c_df = concat(frames, axis=1)
    
    return c_df

def generate_user():
    #Skill
    skill_df = DataFrame(data=generate_data("SKILL"))
    #Experience
    per_df = DataFrame(data=generate_data("PERCEPTION"))
    #Capability
    cap_df = DataFrame(data=generate_data("CAPABILITY"))

    #Concat df
    return concat([skill_df,per_df,cap_df],axis=1)



def write_to_csv(df,folder,filename):
    #Writing to csv file
    df.to_csv(f'{folder}{filename}.csv', encoding='utf-8',sep=";")

#Creating tab
nb_user = 15
user_tab = generate_user()
write_to_csv(user_tab,"generated_results/",f"data_sample_SPC_{nb_user}")
