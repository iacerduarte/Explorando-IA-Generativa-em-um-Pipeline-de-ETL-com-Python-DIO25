import pandas as pd
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# -------------------------------
# EXTRACT
# -------------------------------
def extract(csv_path):
    df = pd.read_csv(csv_path)
    return df["UserID"].tolist()

# -------------------------------
# TRANSFORM (GPT-4)
# -------------------------------
def transform(user_ids):
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    enriched_users = []

    for user_id in user_ids:
        prompt = f"""
        Crie um perfil bancário fictício para um usuário com ID {user_id}.
        Retorne apenas JSON válido contendo:
        nome, idade, profissão, limite_credito, recomendacao_financeira
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        data = json.loads(response.choices[0].message.content)
        data["UserID"] = user_id
        enriched_users.append(data)

    return enriched_users

# -------------------------------
# LOAD
# -------------------------------
def load(data, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# -------------------------------
# PIPELINE
# -------------------------------
def run_pipeline():
    users = extract("SDW2023.csv")
    enriched_data = transform(users)
    load(enriched_data, "SDW2023_output.json")
    print("Pipeline ETL executado com sucesso.")

if __name__ == "__main__":
    run_pipeline()
