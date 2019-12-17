from flask import Flask, request, Response
from up import *

app = Flask(__name__)

@app.route('/metrics')
def test():
    uptime = up()
    uptime = uptime.getUptime()   
    t = "# HELP uptime_days_total Total uptime in days by /proc/uptime\n# TYPE uptime_days_total counter\n"
    t += uptime 

    return Response(t, mimetype='text/plain')
    
@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0', port=5002)
