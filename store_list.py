"""
List all File Search Stores
"""
from config import client

def list_stores():
    """
    List all file search stores

    Returns:
        List of store objects
    """
    response = client.file_search_stores.list()
    stores = list(response)

    print(f"Total stores: {len(stores)}\n")

    for i, store in enumerate(stores, 1):
        print(f"{i}. {store.display_name}")
        print(f"   ID: {store.name}")
        print(f"   Active docs: {store.active_documents_count or 0}")
        print(f"   Size: {store.size_bytes or 0} bytes")
        print(f"   Created: {store.create_time}")
        print()

    return stores


if __name__ == "__main__":
    stores = list_stores()
