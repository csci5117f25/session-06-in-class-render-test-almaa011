import os
from pathlib import Path #this is to not hardcode the DB pass and URL
from flask import Flask, render_template, request, abort
# from DB import setup, insert_submission

# from dotenv import load_dotenv
# load_dotenv(dotenv_path=Path(__file__).with_name(".env"))
app = Flask(__name__)

# setup()

# def _init_pool_and_schema():
#     # Initialize DB pool and ensure schema exists 
#     setup()

@app.get("/")#main
def home():
    
    return render_template("hello.html")



@app.get("/survey")
def survey_get():
    
    return render_template("hello.html")

@app.post("/survey")#use POST to be safe and submit new servey submission in DataBasee
def survey_post():
    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    feedback = (request.form.get("feedback") or "").strip()

    try:#see if it works
        
        _new_id = insert_submission(name, email, feedback)#call helper func from DB to insert new submission
    except Exception as e:
        abort(500, description=f"DB failed brooo {e}")#500 for internal server error
    return render_template("thanks.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
