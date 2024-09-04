from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    well = request.args.get('well')
    data_base = sqlite3.connect('well_data.db')
    connection = data_base.cursor()
    connection.execute('SELECT oil,gas,brine FROM well_data WHERE api_well_number = ?',(well,))
    result = connection.fetchone()
    data_base.close()
    if result :
        return jsonify({
            "oil":result[0],
            "gas":result[1],
            "brine":result[2],
        })
    else:
        return jsonify({'error': 'Well not found'}), 404


if __name__ == '__main__':
    app.run(port=8080)