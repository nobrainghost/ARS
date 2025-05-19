import os
def clean_data(data):
    pass

def normalize_data(data):
    pass

def split_data(data, test_size=0.2):
    pass

def encode_categorical(data, columns):
    pass

def clean_numerics(numerics):
    for field in numerics:
        pass

def pass_description_to_model_to_extend(description):
    import os as OS
    from together import Together
    api_key = OS.getenv("TOGETHER_API_KEY")
    client = Together(api_key=api_key)

    completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[{"role": "user", "content": "You are a smart product description enhancer. Given a short or structured item description with key details, generate a natural, engaging, and human-readable version of it. This description needs to be extended to explain what this product is,where it excels best i.e genres/fields/professions. Please extend this description: " + description}],
    )
    output = completion.choices[0].message.content

    print("Extended description: ", output)
    return output

def pinecone_embed(product, text_to_embed, original_description_metadata, api_key):
    from pinecone import Pinecone

    pc = Pinecone(api_key=api_key)
    index = pc.Index("ars")

    try:
        embedding_response = pc.inference.embed(
            model="llama-text-embed-v2", 
            inputs=[text_to_embed],       
            parameters={
                "input_type": "passage"
            }
        )
        print(f"Embedding response: {embedding_response}")
        if embedding_response.data and len(embedding_response.data) > 0:
            # Check if the actual embedding data (the list of floats) is present
            if hasattr(embedding_response.data[0], 'values') and embedding_response.data[0].values is not None:
                vector_values = embedding_response.data[0].values # Changed .embedding to .values
            # Fallback or alternative check if structure is dict-like from print
            elif isinstance(embedding_response.data[0], dict) and 'values' in embedding_response.data[0] and embedding_response.data[0]['values'] is not None:
                vector_values = embedding_response.data[0]['values']
            else:
                print(f"Error: Embedding vector not found or is None in response for product ID {product}.")
                return 
        else:
            print(f"Error: No embedding data returned for product ID {product}.")
            return 
    except Exception as e:
        print(f"Error generating embedding for product ID {product}: {e}")
        return

    try:
        index.upsert(
            vectors=[
                {
                    "id": str(product), 
                    "values": vector_values,
                    "metadata": {"description": original_description_metadata}
                },
            ],
        )
        print(f"Successfully upserted {product} to Pinecone.")
    except Exception as e:
        print(f"Error upserting to Pinecone for product ID {product}: {e}")
