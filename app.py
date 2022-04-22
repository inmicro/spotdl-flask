from flask import Flask, render_template, request, send_file
import subprocess
import sys
import time
import random

app = Flask(__name__,
  template_folder='templates',
	static_folder='static'
  )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        url_link = request.form.get('urllink')
        timestr = time.strftime("%Y%m%d-%H%M%S")
        result = subprocess.run(["python3", "musicdl.py", url_link, timestr], capture_output=True)
        print(result.stdout, file=sys.stdout)
        path = timestr + '.zip'
        return send_file(path, as_attachment=True)

    return render_template('index.html')

if __name__ == "__main__":
  app.run(
    host = '0.0.0.0',
    port=random.randint(2000, 9000)
  )