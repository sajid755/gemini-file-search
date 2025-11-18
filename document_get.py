"""
Get details of a specific document
"""
from config import client

def get_document(document_name):
    """
    Get details of a specific document

    Args:
        document_name: Full document name (e.g., fileSearchStores/store-id/documents/doc-id)

    Returns:
        Document object
    """
    doc = client.file_search_stores.documents.get(name=document_name)

    print(f"Document Details:")
    print(f"  Name: {doc.name}")
    print(f"  Display Name: {doc.display_name}")
    print(f"  Size: {doc.size_bytes or 0} bytes")
    print(f"  MIME Type: {doc.mime_type}")
    print(f"  State: {doc.state}")
    print(f"  Created: {doc.create_time}")
    print(f"  Updated: {doc.update_time}")

    if hasattr(doc, 'custom_metadata') and doc.custom_metadata:
        print(f"  Custom Metadata:")
        for key, value in doc.custom_metadata.items():
            print(f"    {key}: {value}")

    return doc


if __name__ == "__main__":
    # Replace with your actual document name
    document_name = "fileSearchStores/store-id/documents/doc-id"
    document = get_document(document_name)
