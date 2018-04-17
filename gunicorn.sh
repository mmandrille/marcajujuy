!/bin/bash
cd /opt/marcajujuy
source venv/bin/activate
cd /opt/marcajujuy/marcajujuy
gunicorn MarcaJujuy.wsgi -t 600 -b 127.0.0.1:8000 -w 6 --user=servidor --group=servidor --log-file=/opt/marcajujuy/marcajujuy/gunicorn.log 2>>/opt/marcajujuy/marcajujuy/gunicorn.log

