import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df=pd.read_csv(self.original_csv,encoding='utf-8',on_bad_lines='skip').dropna()

        required_cols = {'Name' , 'Genres','synopsis'}

        missing_cols=required_cols-set(df.columns)

        if missing_cols:
            raise ValueError(f"CSV file is missing the following cols: {missing_cols}")

        df['combined_info']=(
            "Title: " + df['Name'] + "\n" +
            "Genres: " + df['Genres'] + "\n" +
            "Synopsis: " + df['synopsis']
        )

        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv