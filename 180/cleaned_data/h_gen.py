def replaceTabs(file):
    with open(file) as fin, open('fixed'+file, 'w') as fout:
        for line in fin:
            fout.write(line.replace('\t', ','))
    return 'fixed'+file
def combine(filename):
    assert type(filename) == str
    import pandas as pd
    
    """repalce tabs with commas"""
    filename = replaceTabs(filename)
    df = pd.read_csv(filename)
    
    """find unique District Codes"""
    u = df["District Code"].unique()

    print(type(df["District Code"]))
    
    """take average of the first unique district code scores"""
    avg = df[df["District Code"] == u[0]].mean()

    """add it to a new dataframe"""
    merge = pd.DataFrame(dict(avg), index = [0], columns = df.columns)

    """do the same for the rest of the districts"""
    for i in range(1, len(u)):
        avg = df[df["District Code"] == u[i]].mean()
        d = pd.DataFrame(dict(avg), index = [0], columns = df.columns)
        merge = merge.append(d, ignore_index = True)

    """convert to csv file"""
    merge.to_csv("final" + filename[5:])
    return merge

