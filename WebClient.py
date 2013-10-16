__author__ = 'adamhammes'

import mechanize
import bs4

br = mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.addheaders = [('User-agent', 'Mozilla/6.0 (X11; U; Linux i686; en-US; rv:1.9.0.1')]

