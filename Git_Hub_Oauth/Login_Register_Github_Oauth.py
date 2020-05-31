from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
app = Flask(__name__)
app.secret_key = "githuboauth"
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
github_blueprint = make_github_blueprint(
    client_id="a847eb0c987406fb261d",
    client_secret="b615bb17974dd9410204543e334ae6105ef1645d")

app.register_blueprint(github_blueprint, url_prefix="/github_login")


@app.route("/github")
def github_login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    account_info = github.get("/user")

    if account_info.ok:
        account_info_json = account_info.json()
        return (account_info_json)

    return 'Request Failed'

if __name__ == '__main__':
    app.run(debug=True, port=4122)