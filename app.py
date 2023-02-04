import os
import pathlib
from flask import Flask, request, jsonify

from functions import com_filter, com_map, com_unique, com_limit


app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    """
    The function implements a view that processes the request by the POST method at the address "/perform_query",
    accepts five parameters in the request body: where four parameters define the requests and their parameters,
    and the fifth is the file name. The query result is returned as a list of found elements in JSON format.
    """
    req_json = request.json

    file_name = req_json.get("file_name")
    com_list = [(req_json.get("cmd1"), req_json.get("value1")), (req_json.get("cmd2"), req_json.get("value2"))]

    if not file_name:
        return '', 400

    path = pathlib.Path(f"{DATA_DIR}/{file_name}")

    if not path.is_file():
        return '', 400

    with open(path, 'r', encoding='utf-8') as data:

        for cmd, value in com_list:
            if cmd == "filter":
                data = com_filter(data, value)
            elif cmd == "map":
                data = com_map(data, int(value))
            elif cmd == "limit":
                data = com_limit(data, int(value))
            elif cmd == "unique":
                data = com_unique(data)

    return jsonify(data), 200


if __name__ == '__main__':
    app.run()
