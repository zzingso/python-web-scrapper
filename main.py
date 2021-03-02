from flask import Flask, render_template, request, redirect
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()

# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)

db = {}

app = Flask("WebScrapping")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_so_jobs(word)
            db[word] = jobs
        return render_template("report.html",
                               searchingBy=word,
                               resultsNumber=len(jobs),
                               jobs=jobs)
    else:
        return redirect("/")


app.run(host="0.0.0.0", port=8080)
