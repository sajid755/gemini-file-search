"""
Query and extract detailed grounding metadata
"""
from config import client, DEFAULT_MODEL

def query_and_extract_sources(question, store_names):
    """
    Query and extract detailed grounding information

    Args:
        question: The question to ask
        store_names: List of store names to search in

    Returns:
        Dictionary with answer and sources
    """
    # Build file search tool
    file_search_tool = {
        'file_search': {
            'file_search_stores': store_names
        }
    }

    # Generate response
    response = client.models.generate_content(
        model=DEFAULT_MODEL,
        contents=question,
        config={
            'tools': [file_search_tool]
        }
    )

    result = {
        'answer': response.text,
        'sources': []
    }

    # Extract grounding metadata
    if hasattr(response, 'candidates') and response.candidates:
        candidate = response.candidates[0]

        if hasattr(candidate, 'grounding_metadata'):
            grounding = candidate.grounding_metadata

            # Extract sources from grounding chunks
            if hasattr(grounding, 'grounding_chunks'):
                seen_titles = set()

                for chunk in grounding.grounding_chunks:
                    if hasattr(chunk, 'retrieved_context'):
                        context = chunk.retrieved_context
                        title = getattr(context, 'title', None)

                        if title and title not in seen_titles:
                            seen_titles.add(title)
                            result['sources'].append({
                                'title': title,
                                'type': 'file'
                            })

            # Extract grounding support
            if hasattr(grounding, 'grounding_support'):
                support = grounding.grounding_support
                result['support_score'] = getattr(support, 'support_score', None)

    # Display results
    print(f"Question: {question}")
    print(f"\nAnswer: {result['answer']}")
    print(f"\nSources ({len(result['sources'])}):")

    for i, source in enumerate(result['sources'], 1):
        print(f"  {i}. {source['title']}")

    if 'support_score' in result and result['support_score'] is not None:
        print(f"\nGrounding Support Score: {result['support_score']}")

    return result


if __name__ == "__main__":
    # Replace with your actual store names
    store_names = ["fileSearchStores/your-store-id"]

    question = "Summarize the key findings from the research documents"

    result = query_and_extract_sources(question, store_names)
