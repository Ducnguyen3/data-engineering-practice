import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

os.makedirs("data", exist_ok=True)
os.makedirs("model", exist_ok=True)

def crawl_currency():
    url = "https://www.x-rates.com/table/?from=USD&amount=1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.find("table", {"class": "tablesorter ratesTable"})
    df = pd.read_html(str(table))[0]
    df.columns = ["Currency", "Rate", "Inverse"]
    df["Rate"] = df["Rate"].astype(float)
    df.to_csv("data/rates.csv", index=False)
    return df

def preprocess(df):
    # Ví dụ đơn giản: phân loại rate > 1 là 1, else 0
    df["Label"] = (df["Rate"] > 1).astype(int)
    X = df[["Rate"]]
    y = df["Label"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, "model/model.pkl")
    return model

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"🎯 Accuracy: {acc:.2f}")

def main():
    print("🔄 Crawling...")
    df = crawl_currency()
    print("📊 Training model...")
    X_train, X_test, y_train, y_test = preprocess(df)
    model = train_model(X_train, y_train)
    evaluate(model, X_test, y_test)

if __name__ == "__main__":
    main()
