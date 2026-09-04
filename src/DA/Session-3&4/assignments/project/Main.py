from config.config import DATA_PATH, COLS_TO_DROP
from Preprocessing import read_data_file, drop_unnecessary_features, check_data_type

def main():
    df = read_data_file(DATA_PATH)
    
    if df is not None:
        print("-----> Data Summary Before Cleaning <----osama-")
        summary_before = check_data_type(df)
        print(summary_before)
        print("osama\n" + "="*50 + "\n")
        
        df_cleaned = drop_unnecessary_features(df, COLS_TO_DROP)
        
        print("-----> Data Summary After Dropping Features <----osama-")
        summary_after = check_data_type(df_cleaned)
        print(summary_after)

if __name__ == "__main__":
    main()