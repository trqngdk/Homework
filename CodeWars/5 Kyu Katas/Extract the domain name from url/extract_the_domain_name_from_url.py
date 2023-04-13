def domain_name(url):
    """
    Return a domain name from specific url
    Args:
        url (str): An url that neet to be split
    """

    return url.split("www.")[-1].split("//")[-1].split(".")[0]
