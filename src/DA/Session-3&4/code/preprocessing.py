import pandas as pd
def drop_cols(df: pd.DataFrame, cols :list[str])->pd.DataFrame:
    '''  
    
    '''
    return df.drop(columns=cols )

def get_info(df):
    return pd.DataFrame({"dtype": df.dtypes, "nunique": df.nunique()}).T


def replace_outliers(df):
    for col in num_cls:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        # print(Q1, Q3)
        IQR = Q3 -Q1
        lower_fence = Q1  -     1.5 * IQR
        upper_fence = Q3  +     1.5 * IQR
        
        df[col] = df[col].clip(lower_fence,upper_fence)
    return df