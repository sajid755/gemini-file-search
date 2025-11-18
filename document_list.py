"""
List all documents in a File Search Store
"""
from config import client

def list_documents(store_name):
    """
    List all documents in a store

    Args:
        store_name: Full store name (e.g., fileSearchStores/store-id)

    Returns:
        List of document objects
    """
    response = client.file_search_stores.documents.list(parent=store_name)
    documents = list(response)

    print(f"Total documents: {len(documents)}\n")

    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc.display_name}")
        print(f"   ID: {doc.name}")
        print(f"   Size: {doc.size_bytes or 0} bytes")
        print(f"   State: {doc.state}")
        print(f"   Type: {doc.mime_type}")
        print(f"   Created: {doc.create_time}")

        if hasattr(doc, 'custom_metadata') and doc.custom_metadata:
            print(f"   Metadata: {doc.custom_metadata}")

        print()

    return documents


if __name__ == "__main__":
    # Replace with your actual store name
    store_name = "fileSearchStores/your-store-id"
    documents = list_documents(store_name)
