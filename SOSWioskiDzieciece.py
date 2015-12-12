import cStringIO
import os
import tempfile
import urllib
from base64 import b64encode

import math
from flask import Flask, request, render_template
from PIL import Image
import requests
import OverlayingImages

app = Flask(__name__)
app.debug = True
token = 'CAACEdEose0cBAMKyp8Ma2mT4fzfeFDjiiZB2jSWuCBmq4Np0ZChYgrdZBaMxZCLDio7ZBRahFv4Ga3l6eN1UN5DpWA72uQ9vuxWVS24btpUQWg1HcCmQzutk0Xnqls3fi4IZCgzA52GegDayODZBpKNQ9pfyvVvc8xn6ZAs53Rqgurddz16AlgxHHuqDPSInRXIqO0b8HgC8QSNhG5psPrVX'


@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    qs = 'https://graph.facebook.com/me/picture?type=square&height=3000&width=3000' + '&access_token=' + token
    res = requests.request('GET', qs)
    file = cStringIO.StringIO(res.content)
    img = Image.open(file)
    img = OverlayingImages.overlay(img)
    tmp = tempfile.mktemp(suffix='.jpg', dir='./')
    img.save(tmp)
    image = open(tmp, 'rb')
    img = image.read()
    os.remove('./' + tmp)
    trueImage = b64encode( img )


    return render_template('templates.html', trueImage = trueImage )


if __name__ == '__main__':
    app.run()
