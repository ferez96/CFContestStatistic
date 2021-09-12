import crawling
import pandas as pd
from flask import render_template


def contest_details_view(contest_id):
    data = crawling.CodeForcesHTTPClient().send_request("contest.standings",
                                                        dict(contestId=contest_id))

    d = [
        {
            "Members": ",".join([x["handle"] for x in u["party"]["members"]]),
            "Penalty": u["penalty"],
            "Points": u["points"],
        } for u in data["rows"]
    ]
    df = pd.DataFrame(d)

    return render_template("contest_details.html", standings=df.style.render())
