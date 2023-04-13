def domain_name(url):
    """ Split domain name from url

    Args:
        url (str): Url

    Returns:
        str: Return domain name
    """

    return url.split("www.")[-1].split("//")[-1].split(".")[0]
