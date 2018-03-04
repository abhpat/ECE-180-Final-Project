def replaceTabs(file):
    with open(file) as fin, open('fixed' + file, 'w') as fout:
        for line in fin:
            fout.write(line.replace('\t', ','))
    return 'fixed'+file

def combine_districts(filename):
    import pandas as pd
    assert type(filename) == str
    
    """replacing tabs in files with commas for easy parsing"""
    filename = replaceTabs(filename)
    s_df = pd.read_csv(filename)

    """replacing all the * in dataset with true NaNs for easy removal"""
    s_df = s_df.replace('*', float('nan'))
    s_df = s_df.dropna()

    """all the values in data are strs. they need to be floats for calculations"""
    for i in s_df.columns:
        s_df[i] = s_df[i].astype("float")
    
    """get all unique district codes"""
    district_code_unique = s_df['District Code'].unique()

    """get the first district and calculate mean"""
    avg = s_df[s_df['District Code'] == district_code_unique[0]].mean()
    
    """put in a the new dataframe to be returned"""
    merge = pd.DataFrame( dict(avg), index = [0], columns = s_df.columns)
    
    """now do the same for the rest of the districts and add to the dataframe"""
    for i in range(1,len(district_code_unique)):
        avg = s_df[s_df['District Code'] == district_code_unique[i]].mean()
        df = pd.DataFrame(dict(avg), index = [0], columns = s_df.columns)
        merge = merge.append(df, ignore_index = True)
    
    #print(s_df)
    #print(merge)
    merge.to_csv("mean" + filename[5:]) 
    return merge
