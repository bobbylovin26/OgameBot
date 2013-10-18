__author__ = 'adamhammes'

import cookielib
import mechanize
import bs4

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.addheaders = [('User-agent', 'Mozilla/6.0 (X11; U; Linux i686; en-US; rv:1.9.0.1')]

br.open('http://us.ogame.gameforge.com/')

br.select_form(name = 'loginForm')

br['uni'] = ['uni114.ogame.us']
br['login'] = 'Thaunatos'
br['pass'] = 'ogadrepr7cHubra'

response = br.submit()

print br.geturl()


