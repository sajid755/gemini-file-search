"""
Update File Search Store metadata
"""
from config import client
from google.genai.types import UpdateFileSearchStoreConfig

def update_store(store_name, display_name=None, description=None):
    """
    Update store metadata

    Args:
        store_name: Full store name (e.g., fileSearchStores/store-id)
        display_name: New display name (optional)
        description: New description (optional)

    Returns:
        Updated store object
    """
    # Build update mask based on what is being updated
    update_mask = []
    update_data = {}

    if display_name:
        update_mask.append('display_name')
        update_data['display_name'] = display_name

    if description is not None:
        update_mask.append('description')
        update_data['description'] = description

    config = UpdateFileSearchStoreConfig(
        update_mask=update_mask
    )

    store = client.file_search_stores.update(
        name=store_name,
        config=config,
        **update_data
    )

    print(f"Store updated successfully")
    print(f"  Name: {store.name}")
    print(f"  Display Name: {store.display_name}")
    print(f"  Description: {getattr(store, 'description', 'N/A')}")

    return store


if __name__ == "__main__":
    # Replace with your actual store name
    store_name = "fileSearchStores/your-store-id"
    updated_store = update_store(
        store_name,
        display_name="updated-name",
        description="Updated description"
    )
