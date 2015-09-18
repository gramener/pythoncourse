Working With the Web
====================

This chapter discusses various ways to download data from the web, programatically interacting with web applications using JSON and XML APIs, and screen scraping websites to extract data from them.

**Suggested References**

* `urllib - Python module of the week <http://pymotw.org/2/urllib2>`_
* `urllib2 - Python module of the week <http://pymotw.org/2/urllib2>`_
* `Requests: HTTP for Humans <http://python-requests.org>`_
* `json - Python module of the week <http://pymotw.org/2/json>`_
* `xml.etree.ElementTree - Python module of the week <https://pymotw.com/2/xml/etree/ElementTree/>`_
* `BeautifulSoup Documentation <http://www.crummy.com/software/BeautifulSoup/>`_

Downloading Data From The Web
-----------------------------

The ``urllib`` module provides a way to download data from the web.

::

    >>> import urllib
    >>> response = urllib.urlopen("http://httpbin.org/html")

The response is a file-like object.
::

    >>> html = response.read()
    >>> print html[:100]
    <!DOCTYPE html>
    <html>
      <head>
      </head>
      <body>
          <h1>Herman Melville - Moby-Dick</h1>

The response object also contains the HTTP headers.
::

    >>> print response.headers
    Server: nginx
    Date: Fri, 18 Sep 2015 15:34:01 GMT
    Content-Type: text/html; charset=utf-8
    Content-Length: 3741
    Connection: close
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Credentials: true

**Problem**  Write a program ``wget.py`` to download a given URL. The program should accept a URL as a command-line argument, download it and save it with the basename of the URL. If the URL ends with a ``/``, consider the basename as ``index.html``.

::

    $ python wget.py https://docs.python.org/2/tutorial/interpreter.html
    saving interpreter.html
    $ python wget.py https://docs.python.org/2/tutorial/
    saving index.html
    $ python wget.py https://www.python.org/static/img/python-logo.png
    saving python-logo.png

The ``urllib2`` module
^^^^^^^^^^^^^^^^^^^^^^

While the ``urllib`` module is good enough of simple cases, it has some limitations. One of the main drawback is error reporting. If we try to access a web page that gives an error status like 404, the urllib module doesn't treat that an error case. It is the responsibility of the caller to check the status code.

::

    >>> import urllib
    >>> response = urllib.urlopen("http://httpbin.org/no-such-page")
    >>> response.code
    404

The `urllib2` modules solves that issue nicely by raising an error when there is an error condition like this.

::

    >>> import urllib2
    >>> response = urllib2.urlopen("http://httpbin.org/no-such-page")
    Traceback (most recent call last):
        ...
    urllib2.HTTPError: HTTP Error 404: NOT FOUND

The ``requests`` module
^^^^^^^^^^^^^^^^^^^^^^^

Even using the ``urllib2`` module gets pretty complicated when dealing with things like basic-auth, cookies etc. The third-party library `requests <http://python-requests.org/>`_ provides a very nice API for making HTTP requests.

::

    >>> import requests
    >>> print requests.get("http://httpbin.org/html").text[:100]
    <!DOCTYPE html>
    <html>
      <head>
      </head>
      <body>
          <h1>Herman Melville - Moby-Dick</h1>

Working with APIs
-----------------

Various websites provide APIs to interact with them programatically. XML and JSON are the popular formats for exchange of information over the web.

In this section we'll see how to work with JSON and XML APIs using Python, using `Open Weather Map <http://openweathermap.org/>`_ and `GitHub <https://developers.github.com/>`_ as examples.

JSON APIs
^^^^^^^^^

JSON is the simplest and most popular format on web. JSON looks very much like Python, with slight exceptions.

The standard library module ``json`` provides functionality to serialize and restore a python datastrucure to JSON. The ``json.dumps`` function converts a python data strucuture to JSON.

::

    >>> import json
    >>> json.dumps({"name": "Alice", "score": 34, "verified": True})
    '{"score": 34, "verified": true, "name": "Alice"}'

Pretty printing can be enabled optionally.

::

    >>> json.dumps({"name": "Alice", "score": 34, "verified": True}, indent=True)
    '{\n "score": 34, \n "verified": true, \n "name": "Alice", \n "email": "alice@example.com"\n}'
    >>> print json.dumps({"name": "Alice", "score": 34, "verified": True}, indent=True)
    {
     "score": 34,
     "verified": true,
     "name": "Alice",
     "email": "alice@example.com"
    }

The ``json.loads`` function takes a JSON string and returns a Python data structure.

    >>> json.loads('{"name": "Alice", "x": 42, "verified": true}')
    {u'x': 42, u'verified': True, u'name': u'Alice'}

Please note that the strings in the result will always be in unicode.

Example: Open Weather Map API
`````````````````````````````

`Open Weather Map <http://openweathermap.org/>`_ provides an API for weather forecast for many cities around the world. See their `API documentation <http://openweathermap.org/current>`_ for more details of the API.

Lets look at the response format.

::

    $ curl http://api.openweathermap.org/data/2.5/weather?q=bangalore
    {"coord":{"lon":77.6,"lat":12.98},"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"base":"cmc stations","main":{"temp":304.15,"pressure":1010,"humidity":62,"temp_min":304.15,"temp_max":304.15},"wind":{"speed":4.1,"deg":270},"clouds":{"all":40},"dt":1442566800,"sys":{"type":1,"id":7823,"message":0.0129,"country":"IN","sunrise":1442536722,"sunset":1442580522},"id":1277333,"name":"Bangalore","cod":200}

The response has description of the weather, min and max temparatures, wind speed etc. Lets write a program to print the description of the current weather of given city.

.. code-block:: python

    # weather.py
    import urllib, urllib2
    import json
    import time
    import sys

    def jsonget(url):
        jsontext = urllib2.urlopen(url).read()
        return json.loads(jsontext)

    def get_forecast(city):
        """Returns data about current weather forcast for given city.
        """
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city
        return jsonget(url)

    def main():
        city = sys.argv[1]
        forecast = get_forecast(city)

        # The response is representing time as integer seconds from epoch.
        # convert it into string.
        t = time.ctime(forecast['dt'])

        # read the description
        description = forecast['weather'][0]['description']

        # display it
        print "{} - {}".format(t, description)

    if __name__ == "__main__":
        main()

Lets try running it.

::

    $ python weather.py Bangalore
    Fri Sep 18 14:30:00 2015 - scattered clouds

    $ python weather.py Chennai
    Fri Sep 18 14:40:00 2015 - few clouds

**Problem** Write a program ``forecast.py`` to display the weather forcast for next 5 days in the given city. The program should accept the city name as command-line argument and display the summary of forecast for next 5 days.

::

    $ python forecast.py Bangalore
    2015-10-18 scattered clouds
    2015-10-19 few clouds
    2015-10-20 moderate rain
    2015-10-21 light rain
    2015-10-22 heavy intensity rain

Example: GitHub API
```````````````````

`GitHub <https://github.com/>`_ provides `extensive API <https://developers.github.com/>`_ to interact with it. While part of that requires authentication, there are parts which are open to the public.

Let try to find top python repositories by number of forks.

.. code-block: Python

    # top-python-repos.py
    """Program to print top python repositories on GitHub.
    """
    import requests
    URL = "https://api.github.com/search/repositories"
    params = {
        "q": "language:python",
        "sort": "forks"
    }
    result = requests.get(URL, params=params).json()
    repos = [repo['name'] for repo in result['items']]

    for name in repos[:5]:
        print name

Output::

    $ python top-python-repos.py
    django
    shadowsocks
    flask
    scikit-learn
    ansible

**Problem** Write a program `top-repos.py` to find top five public repositories of any given organization on GitHub. The program should accept the org name as command-line argument.

::

    $ python top-repos.py flipkart
    phantom
    aesop
    HostDB
    loader
    harness

    $ python top-repos.py facebook
    hhvm
    facebook-android-sdk
    facebook-ios-sdk
    folly
    presto

Working with XML APIs
^^^^^^^^^^^^^^^^^^^^^

XML is hard to parse than JSON. While it is hard, parsing XML is lot easier in Python than many other languages.

One of the easiest ways to parse XML in Python is using `xml.etree.ElementTree` module.

Open Weather Map XML API
^^^^^^^^^^^^^^^^^^^^^^^^

Open Weather Map also provides XML API in addition to JSON API. Let try the XML API to get the current weather.

::

    >>> url = "http://api.openweathermap.org/data/2.5/weather?q=Bangalore&mode=xml"
    >>> xmltext = urllib.urlopen(url).read()
    >>> print xmltext
    <current><city id="1277333" name="Bangalore"><coord lon="77.6" lat="12.98"></coord><country>IN</country><sun rise="2015-08-22T00:38:01" set="2015-08-22T13:06:52"></sun></city><temperature value="300.15" min="300.15" max="300.15" unit="kelvin"></temperature><humidity value="83" unit="%"></humidity><pressure value="1014" unit="hPa"></pressure><wind><speed value="5.7" name="Moderate breeze"></speed><gusts></gusts><direction value="290" code="WNW" name="West-northwest"></direction></wind><clouds value="75" name="broken clouds"></clouds><visibility value="10000"></visibility><precipitation mode="no"></precipitation><weather number="803" value="broken clouds" icon="04d"></weather><lastupdate value="2015-08-22T07:30:00"></lastupdate></current>

Lets try to parse the XML text.

::

    >>> from xml.etree import ElementTree as et
    >>> root = et.fromstring(xmltext)
    >>> root
    <Element 'current' at 0x112cc6e90>

Now, we got the an XML element and we need to get the current weather description from that.

::

    >>> root.find("weather").get("value")
    'scattered clouds'

**Problem** Write a program ``temp-forecast.py`` to display the forecast of the min and max temparatures for next five days. Use the forecast API with XML format to finx this.

Scraping Web Pages
------------------

TODO