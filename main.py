import json

from flask import Flask, request, Response, render_template


gifts = {
    'tv': 'amzn.to/3s0JQLF',
    'music_headphones': 'amzn.to/3dwxpi4',
    'tv_headphones': 'amzn.to/3rLLQHl',
    'sunglasses': 'amzn.to/3GpXc7S',
    'smart_watch': 'amzn.to/31BsBFK',
    'blender_bottle': 'amzn.to/3EuQsoN',
    'underwear': 'amzn.to/32yIm0h'
}

app = Flask(__name__)


@app.route("/")
def homepage():
    # return render_template("page.html", title="HOME PAGE")
    return '1'


@app.route('/collect-feedback', methods=['POST'])
def collect_feedback():
    data = json.loads(request.data)
    dadTv = data['dadTv']
    shopFrequency = data['shopFrequency']
    dadWorkPlace = data['dadWorkPlace']
    dadBluetooth = data['dadBluetooth']
    dadHealthCareWatch = data['dadHealthCareWatch']
    dadWorkout = data['dadWorkout']
    dadGlasses = data['dadGlasses']

    if dadTv[0] == 'Yes':
        return Response(gifts['tv'], mimetype='application/json')
    elif shopFrequency[0] == "My mom shops for him":
        return Response(gifts['underwear'], mimetype='application/json')
    if dadWorkout[0] == 'Yes':
        return Response(gifts['music_headphones'], mimetype='application/json')
    elif dadGlasses[0] == 'Yes':
        return Response(gifts['sunglasses'], mimetype='application/json')
    elif dadHealthCareWatch[0] == 'Yes':
        return Response(gifts['smart_watch'], mimetype='application/json')
    elif dadWorkout[0] == 'Yes':
        # return gifts['blender_bottle']
        return Response('hi', mimetype='application/json')
    else:
        # return "hi"
        return Response('hi', mimetype='application/json')


@app.route("/about")
def about():
    return render_template("page.html", title="about page")


if __name__ == "__main__":
    app.run(debug=True)
