"""Parser for registry responses"""

def parse_registry_response(response):
    """
    Parse registry response
    
    :param response:
        Registry response to be parsed
    """
    object_id = response["_data"].object_id

    # Delete data key and value from response
    default = response["_data"].content.fields["value"]["fields"]
    del default["data"]

    # Add object_id
    default.update(id=object_id)

    # Return parsed response
    return default