import re
import pandas as pd
from sklearn.model_selection import train_test_split

def tsv_to_csv(path_in: str, path_out: str) -> None:
    """
    Converts a TSV file to a CSV file by replacing tab characters with commas.
    """
    with open(path_in, "r", encoding = "utf-8") as tsv_file:
        with open(path_out, "w", encoding = "utf-8") as csv_file:
            for line in tsv_file:
                line_content = re.sub('\t', ',', line)
                csv_file.write(line_content)

def stratified_split_from_csv(path_in: str, train_path_out: str, test_path_out: str
                              , test_size: float = 0.2, random_state: int = 42
) -> None:
    """
    Splits data into training and testing sets while preserving the distribution of labels.
    """
    # Load CSV
    df = pd.read_csv(path_in)

    # Stratified split
    train_df, test_df = train_test_split(
        df,
        test_size=test_size,
        stratify=df['label'],
        random_state=random_state
    )

    # Save to CSV
    train_df.to_csv(train_path_out, index=False)
    test_df.to_csv(test_path_out, index=False)

