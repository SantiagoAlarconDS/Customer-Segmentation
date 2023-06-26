import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import List, Dict, Tuple

def encode_categorical_features(df: pd.DataFrame, cols: List[str]) -> Tuple[pd.DataFrame, Dict[str, LabelEncoder]]:
    """
    Encode categorical features using LabelEncoder.

    Args:
        df (DataFrame): The input DataFrame.
        cols (List[str]): List of column names to encode.

    Returns:
        Tuple[DataFrame, Dict[str, LabelEncoder]]: Encoded DataFrame and dictionary of LabelEncoder objects.

    """
    
    label_encoders: Dict[str, LabelEncoder] = {}
    
    for col in cols:
        LE = LabelEncoder()
        df[col] = LE.fit_transform(df[col])
        label_encoders[col] = LE
    
    return df, label_encoders

def decode_categorical_features(df: pd.DataFrame, label_encoders: Dict[str, LabelEncoder]) -> pd.DataFrame:
    """
    Decode categorical features using LabelEncoder.

    Args:
        df (DataFrame): The input DataFrame with encoded features.
        label_encoders (Dict[str, LabelEncoder]): Dictionary of LabelEncoder objects.

    Returns:
        DataFrame: Decoded DataFrame.

    """
    
    for col, le in label_encoders.items():
        df[col] = le.inverse_transform(df[col])
    
    return df