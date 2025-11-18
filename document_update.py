"""
Update document metadata
"""
from config import client
from google.genai.types import UpdateDocumentConfig

def update_document(document_name, display_name=None, custom_metadata=None):
    """
    Update document metadata

    Args:
        document_name: Full document name (e.g., fileSearchStores/store-id/documents/doc-id)
        display_name: New display name (optional)
        custom_metadata: Dictionary of custom metadata to update (optional)

    Returns:
        Updated document object
    """
    # Build update mask based on what is being updated
    update_mask = []
    update_data = {}

    if display_name:
        update_mask.append('display_name')
        update_data['display_name'] = display_name

    if custom_metadata is not None:
        update_mask.append('custom_metadata')
        update_data['custom_metadata'] = custom_metadata

    config = UpdateDocumentConfig(
        update_mask=update_mask
    )

    doc = client.file_search_stores.documents.update(
        name=document_name,
        config=config,
        **update_data
    )

    print(f"Document updated successfully")
    print(f"  Name: {doc.name}")
    print(f"  Display Name: {doc.display_name}")

    if hasattr(doc, 'custom_metadata'):
        print(f"  Custom Metadata: {doc.custom_metadata}")

    return doc


if __name__ == "__main__":
    # Replace with your actual document name
    document_name = "fileSearchStores/store-id/documents/doc-id"

    updated_doc = update_document(
        document_name,
        display_name="Updated Document Name",
        custom_metadata={"category": "updated", "version": "2.0"}
    )
