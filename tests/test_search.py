def test_search_functionality(home_page):
    search_query = "Developer"

    results = home_page.search_for_item_and_return_results(search_query)

    for result in results:
        assert search_query.lower() in result.text.lower(), f"Search result '{result.text}' does not contain '{search_query}'"
