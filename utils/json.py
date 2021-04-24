def update_or_create_elements_from_json(response, update_or_create_element, obj):
    for element in response.json():
        update_or_create_element(element, obj)
