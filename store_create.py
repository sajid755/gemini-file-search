"""
Create a new File Search Store
"""
from config import client

def create_store(display_name, description=None):
    """
    Create a new file search store

    Args:
        display_name: User-friendly name for the store
        description: Optional description

    Returns:
        Created store object
    """
    store = client.file_search_stores.create(
        display_name=display_name,
        description=description
    )

    print(f"Store created successfully")
    print(f"  Name: {store.name}")
    print(f"  Display Name: {store.display_name}")
    print(f"  Created: {store.create_time}")

    return store


if __name__ == "__main__":
    # Example usage
    store = create_store(
        display_name="my-knowledge-base",
        description="Sample file search store"
    )
