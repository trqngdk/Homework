# Homework

## Extract the domain name from url!

**Description:** Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

**Example**

```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
```

### Solution

```python
def domain_name(url):
    """ Split domain name from url

    Args:
        url (str): Url

    Returns:
        str: Return domain name
    """

    return url.split("www.")[-1].split("//")[-1].split(".")[0]

```
