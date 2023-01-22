from flask import Flask, request, abort
import producer as pr
app = Flask(__name__)

@app.route('/metrics_webhook', methods=['POST'])
def metrics_webhook():
    print('running')
    if request.method == 'POST':
        print('metrics web hook')
        pr.Push_to_queue(request.json,'metrics')
        return 'success', 200
    else:
        abort(400)

@app.route('/workorder_webhook', methods=['POST'])
def workorder_webhook():
    print('running')
    if request.method == 'POST':
        print('workorder web hook')
        pr.Push_to_queue(request.json,'workorder')
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()