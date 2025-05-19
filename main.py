# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Abstract Recommender System API"}


from data import loader
from utils import helpers
import os

DataLoader = loader.DataLoader()

data = DataLoader.get_data()
test_data = data.head(5)
for index, row in test_data.iterrows():
    def gen_product(description_string):
        description_parts = description_string.split(", ")
        product=None
        if len(description_parts) >= 2:
            prod1 = description_parts[0]
            prod2= description_parts[1]
            product=f"{prod1} {prod2}"
        return product
    product = gen_product(row['description'])
    extended_description = helpers.pass_description_to_model_to_extend(row['description'])
    helpers.pinecone_embed(product,extended_description, row['description'], os.getenv("pinecone_key"))
    print(f"Product: {product}")