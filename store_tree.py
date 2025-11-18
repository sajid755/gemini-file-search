"""
Display all stores and documents in tree structure
"""
from config import client

def display_tree():
    """
    Display all stores and their documents in a tree structure
    """
    response = client.file_search_stores.list()
    stores = list(response)

    print("Gemini File Search Stores Tree")
    print("=" * 70)
    print()

    if not stores:
        print("No stores found")
        return

    for i, store in enumerate(stores, 1):
        active = store.active_documents_count or 0
        pending = store.pending_documents_count or 0
        failed = store.failed_documents_count or 0
        total = active + pending + failed

        print(f"{store.display_name}")
        print(f"  ID: {store.name}")
        print(f"  Documents: {active} active, {pending} pending, {failed} failed")
        print(f"  Size: {store.size_bytes or 0} bytes")

        if active > 0:
            docs_response = client.file_search_stores.documents.list(parent=store.name)
            docs = list(docs_response)

            for j, doc in enumerate(docs, 1):
                is_last = j == len(docs)
                prefix = "  └─" if is_last else "  ├─"

                print(f"{prefix} {doc.display_name}")
                print(f"  {'  ' if is_last else '  │'} Size: {doc.size_bytes or 0} bytes")
                print(f"  {'  ' if is_last else '  │'} State: {doc.state}")
                print(f"  {'  ' if is_last else '  │'} Type: {doc.mime_type}")

        print()


if __name__ == "__main__":
    display_tree()
