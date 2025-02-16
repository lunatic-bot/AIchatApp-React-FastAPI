import wikipediaapi

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia("en")

def search_wikipedia(query: str) -> str:
    """Search Wikipedia for the given query and return the summary."""
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary[:500]  # Return the first 500 characters
    return None  # Return None if no page is found
