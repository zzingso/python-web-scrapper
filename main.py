from flask import Flask
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()

# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)

app = Flask("WebScrapping")


@app.route("/")
def home():
    return "Hello!"


app.run(host="0.0.0.0")
