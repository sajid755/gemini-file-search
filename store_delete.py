"""
Delete a File Search Store
"""
from config import client
from google.genai.types import DeleteFileSearchStoreConfig

def delete_store(store_name, force=True):
    """
    Delete a file search store

    Args:
        store_name: Full store name (e.g., fileSearchStores/store-id)
        force: If True, also deletes all documents in the store

    Returns:
        None
    """
    config = DeleteFileSearchStoreConfig(force=force) if force else None

    client.file_search_stores.delete(
        name=store_name,
        config=config
    )

    print(f"Store deleted successfully: {store_name}")


if __name__ == "__main__":
    # Replace with your actual store name
    store_name = "fileSearchStores/your-store-id"

    # Delete with force to remove all documents
    delete_store(store_name, force=True)
