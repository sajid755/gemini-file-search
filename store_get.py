"""
Get details of a specific File Search Store
"""
from config import client

def get_store(store_name):
    """
    Get details of a specific store

    Args:
        store_name: Full store name (e.g., fileSearchStores/store-id)

    Returns:
        Store object
    """
    store = client.file_search_stores.get(name=store_name)

    print(f"Store Details:")
    print(f"  Name: {store.name}")
    print(f"  Display Name: {store.display_name}")
    print(f"  Active documents: {store.active_documents_count or 0}")
    print(f"  Pending documents: {store.pending_documents_count or 0}")
    print(f"  Failed documents: {store.failed_documents_count or 0}")
    print(f"  Total size: {store.size_bytes or 0} bytes")
    print(f"  Created: {store.create_time}")
    print(f"  Updated: {store.update_time}")

    return store


if __name__ == "__main__":
    # Replace with your actual store name
    store_name = "fileSearchStores/your-store-id"
    store = get_store(store_name)
