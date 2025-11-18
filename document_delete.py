"""
Delete a document from a File Search Store
"""
from config import client
from google.genai.types import DeleteDocumentConfig

def delete_document(document_name, force=True):
    """
    Delete a document

    Args:
        document_name: Full document name (e.g., fileSearchStores/store-id/documents/doc-id)
        force: If True, force delete even if document has been indexed

    Returns:
        None
    """
    config = DeleteDocumentConfig(force=force) if force else None

    client.file_search_stores.documents.delete(
        name=document_name,
        config=config
    )

    print(f"Document deleted successfully: {document_name}")


if __name__ == "__main__":
    # Replace with your actual document name
    document_name = "fileSearchStores/store-id/documents/doc-id"

    # Delete with force to remove indexed document
    delete_document(document_name, force=True)
