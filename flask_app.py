from colorama import Fore
from flask import Flask, render_template

import googleDoc

app = Flask(__name__)


@app.route('/')
def index():
    doc_link = "https://docs.google.com/document/d/1I5P-SzaiKAOrnPBhnqtoCWDiWrDtSueWodlkjkjegEU/export?format=txt"
    approver_names = {"T+": "Taylan", "Y+": "Baran", "C+": "Can", "B+": "Burak"}

    output_file = "songs.txt"
    googleDoc.download_google_docs(doc_link, output_file)

    approvers = {"T+": Fore.RED, "Y+": Fore.BLUE, "C+": Fore.GREEN, "B+": Fore.YELLOW}

    approved_songs, approvals_count, songs_approved_by_everyone, songs_approved_by_everyone_no_parentheses, double_plussed_songs, approver_approved_songs, double_plussed_songs_info = googleDoc.get_future_songs_with_plus(
        output_file)

    return render_template('index.html',
                           approver_names=approver_names,
                           approvers=approvers,
                           approver_approved_songs=approver_approved_songs,
                           approvals_count=approvals_count,
                           songs_approved_by_everyone=songs_approved_by_everyone,
                           songs_approved_by_everyone_no_parentheses=songs_approved_by_everyone_no_parentheses,
                           double_plussed_songs=double_plussed_songs,
                           double_plussed_songs_info=double_plussed_songs_info,
                           approvers_dict=approvers)  # Include approvers_dict in the render_template function


if __name__ == '__main__':
    app.run(debug=True, port=5001)
