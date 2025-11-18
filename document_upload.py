"""
Upload a document to a File Search Store
"""
from config import client
import mimetypes

def upload_document(store_name, file_path, display_name=None, custom_metadata=None):
    """
    Upload a document to a file search store

    Args:
        store_name: Full store name (e.g., fileSearchStores/store-id)
        file_path: Path to the file to upload
        display_name: Optional custom display name (defaults to filename)
        custom_metadata: Optional dictionary of custom metadata

    Returns:
        Uploaded document object
    """
    # Determine MIME type
    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type:
        mime_type = 'application/octet-stream'

    # Use filename as display name if not provided
    if not display_name:
        import os
        display_name = os.path.basename(file_path)

    # Read file content
    with open(file_path, 'rb') as f:
        file_content = f.read()

    # Upload document
    doc = client.file_search_stores.documents.upload(
        parent=store_name,
        file=file_content,
        config={
            'display_name': display_name,
            'mime_type': mime_type,
            'custom_metadata': custom_metadata or {}
        }
    )

    print(f"Document uploaded successfully")
    print(f"  Document ID: {doc.name}")
    print(f"  Display Name: {doc.display_name}")
    print(f"  Size: {doc.size_bytes} bytes")
    print(f"  State: {doc.state}")

    return doc


if __name__ == "__main__":
    # Replace with your actual store name and file path
    store_name = "fileSearchStores/your-store-id"
    file_path = "path/to/your/document.pdf"

    doc = upload_document(
        store_name,
        file_path,
        display_name="Sample Document",
        custom_metadata={"category": "example", "version": "1.0"}
    )
