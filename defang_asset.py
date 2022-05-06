def defang_asset(input_asset=None, **kwargs):
    """
    Custom function used to defang IP, URL and Domain addresses.
    
    Args:
        input_asset (CEF type: *): The IP, URL or Domain to defang
            
            Adds square brackets to address to ensure it is not active. Typically used for IOCs.
    
    Returns a JSON-serializable object that implements the configured data paths:
        output_asset (CEF type: *): The defanged asset
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    new_address = ""

    try:
        if input_asset: 
            split_address = input_asset.split(".")
            separator = "[.]"
            new_address = separator.join(split_address)
            outputs=({'input_asset': input_asset, 'output_asset': new_address})
    except Exception as e:
        phantom.error(f'Unable to defang asset: {e}')
        

    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
