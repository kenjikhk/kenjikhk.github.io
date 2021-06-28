from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Get back home"
    
    text = """You are lost in the forest while hiking on your own. It is getting dark. Your phone is dead. Suddenly you hear people voices getting closer to you but there is no one around."""

    choices = [
        ('follow_voices',"Try to find where voices are coming from"),
        ('wait',"Wait and see what happens")
    ]

    return render_template('backhome.html', title=title, text=text, choices=choices)



@app.route("/check")
def follow_voices():
    title = "You follow the voices..."
    
    text = """You followed the voices for the next 15 minutes until you got to a dark cave. You see a lit candle inside the cave..."""

    choices = [
        ('go_inside',"Get into the cave"),
        ('wait',"Wait and see what happens")
    ]

    return render_template('backhome.html', title=title, text=text, choices=choices)

@app.route("/wait")
def wait():
    title = "No balls no goals"
    
    text = """You stayed there for the rest of your life"""

    choices = []

    return render_template('backhome.html', title=title, text=text, choices=choices)



@app.route("/cave")
def go_inside():
    title = "Be careful the voices are getting even closer!"
    
    text = """The voices got very close to you and you realized that these were voices of a couple of exhausted miners getting back home after anouther tough day in the mine. You ask for help and get back to the city together with the guys. Ta-dam """

    choices = []

    return render_template('backhome.html', title=title, text=text, choices=choices)
