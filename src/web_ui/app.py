from flask import Flask, render_template
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
    #return "YO"
    return render_template('home.html')


@app.route("/bash/<end_goal>")
def run_bash_script(end_goal):

    bash_command = 'rosrun rosie_2dnav simple_nav_command.py ' + end_goal

    subprocess.call(['. ../../devel/setup.sh'], shell=True)
    subprocess.call([bash_command], shell=True)
    return "Bash Commands Successfully Executed"

if __name__ == "__main__":
    app.run(debug=True)
