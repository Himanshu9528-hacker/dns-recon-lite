from flask import Flask, request
from dns_lookup import domain_to_ip
from reverse_dns import ip_to_domain

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    domain = request.args.get('domain')
    return domain_to_ip(domain)

@app.route('/reverse')
def reverse():
    ip = request.args.get('ip')
    return ip_to_domain(ip)

if __name__ == '__main__':
    app.run(debug=True)
