def default(alias=None, connection=None, wrapper=None):
    search_path = []

    if wrapper.vendor == 'postgresql':
        if alias == 'default':
            search_path.append('public')
        else:
            search_path.append(alias)
    return search_path

def settings_option(alias=None, connection=None, wrapper=None):
    if 'NAMESPACE' in connection.settings_dict:
        return [connection.settings_dict['NAMESPACE']]