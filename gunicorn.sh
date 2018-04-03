#!/bin/bash
cd /opt/marcajujuy
gunicorn MarcaJujuy.wsgi -t 600 -b 127.0.0.1:8000 -w 6 --user=root --group=root --/opt/marcajujuy/gunicorn.log 2>>/opt/marcajujuy/gunicorn.log
