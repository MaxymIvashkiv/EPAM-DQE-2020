
img_net = 'https://img3.goodfon.com/wallpaper/nbig/c/9d/simpsony-the-simpsons-homer.jpg'

_img_resp = ('<html>\n'
             '<body>\n'
             '<img src="{img_net}" alt="Image to server">\n'
             '</body></html>')

def image(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _img_resp.format(img_net = img_net)
    yield resp.encode('utf-8')