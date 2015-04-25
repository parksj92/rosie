from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"


@app.route("/bash/<end_goal>")
def run_bash_script(end_goal):

    bash_command = 'rosrun rosie_2dnav rosie_nav_command.py ' + end_goal

    subprocess.call(['. ../../devel/setup.sh'], shell=True)
    subprocess.call([bash_command], shell=True)
    return "Bash Commands Successfully Executed"

if __name__ == "__main__":
    app.run()
