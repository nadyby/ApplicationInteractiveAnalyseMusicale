import pandas as pd

def load_spotify_data():
    """
    Charge le dataset Spotify Tracks directement depuis Hugging Face en utilisant pd.read_csv.
    """
    df = pd.read_csv("hf://datasets/maharshipandya/spotify-tracks-dataset/dataset.csv")
    print("Aperçu des premières lignes du dataset:")
    print(df.head())
    return df

if __name__ == "__main__":
    load_spotify_data()