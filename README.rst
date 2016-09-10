=====
cgrss
=====

Scrapes the Davis Enterprise `Comings and Goings`_ page and generates an RSS
feed. This was just a little fun project to work on for a couple hours -- I've
always wanted to have an RSS feed for Comings and Goings, so I threw this
together.

I have since figured out that appending ``/rss`` to the URL takes one to the
*official* feed. I wish there were links to such things on the Davis Enterprise
website so I wouldn't waste time with silly things like this, but it was fun to
do a little scraping and parsing -- I hadn't done much of that before.

Installation
------------

Dependencies are specified in ``setup.py``, so the following will install them
and cgrss itself::

    python setup.py install --user

Usage
-----

The installation includes a console script called ``cgrss`` which generates the
feed::

    cgrss -o feed.xml

Serving
-------

I have a home server, and I've installed this along with a systemd timer to
periodically generate the XML file in my Dropbox. Why set up an Apache server
to host a single file when Dropbox works just as well, right? The file is set
up to be shared by link, and I put the direct link to the file in Feedly.
Sweet!


.. _Comings and Goings: http://www.davisenterprise.com/business/comings-and-goings/
