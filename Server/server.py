from flask import Flask, request, jsonify
import util
app= Flask(__name__)

@app.route('/predict_water_potability', methods=['GET','POST'])
def predict_water_potability():
    ph= float(request.form['ph'])
    Hardness= float(request.form['Hardness'])
    Solids= float(request.form['Solids'])
    Chloramines= float(request.form['Chloramines'])
    Sulfate= float(request.form['Sulfate'])
    Conductivity= float(request.form['Conductivity'])
    Organic_carbon= float(request.form['Organic_carbon'])
    Trihalomethanes= float(request.form['Trihalomethanes'])
    Turbidity= float(request.form['Turbidity'])
    response= jsonify({
        'predicted_potability': util.get_predicted_potability(
            ph,Hardness,Solids,Chloramines,Sulfate,
            Conductivity,Organic_carbon,
            Trihalomethanes,Turbidity
        )
    })
    response.headers.add('Access-Control_Allow_Origin', '*')
    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()