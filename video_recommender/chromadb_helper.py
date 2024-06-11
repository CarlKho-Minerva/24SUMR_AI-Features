# video_recommender/chromadb_helper.py

import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from constants import *


def initialize_chromadb():
    """
    Initialize ChromaDB client and collection.

    Returns:
    collection: Initialized ChromaDB collection.
    """
    chroma_client = chromadb.PersistentClient(path="db")
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY, model_name=OPENAI_EmbeddingModel
    )
    collection = chroma_client.get_or_create_collection(
        name=chromadb_name,
        embedding_function=openai_ef,
        metadata={"hnsw:space": "cosine"},
    )
    return collection


def add_or_update_chromadb_rows(df, collection):
    """
    Add or update rows in the ChromaDB collection.

    Parameters:
    df (DataFrame): DataFrame containing video data.
    collection: ChromaDB collection.
    """
    documents = df["tags"].apply(lambda x: x.split(",")).tolist()
    documents_str = [", ".join(doc) for doc in documents]
    ids = [str(i + 1) for i in range(len(documents_str))]
    collection.upsert(documents=documents_str, ids=ids)
