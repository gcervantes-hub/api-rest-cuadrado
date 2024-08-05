#Api que evalua el área y perímtro de una cuadrado
from flask import Flask, jsonify, request

app = Flask(__name__)

def evalua_area(lado):
    calculo = lado * lado
    return calculo

def evalua_perimetro(lado):
    calculo = lado * 4
    return calculo
    
@app.route('/cuadrado', methods = ['POST'])
def formulas():
    data = request.get_json()
    input_lado=data.get('lado')
    
    if data['type'] == 'area':
        result = evalua_area(input_lado)
        output_unit = 'area'
    
    if data['type'] == 'perimetro':
        result = evalua_perimetro(input_lado)
        output_unit = 'perimetro'
        
    return jsonify({"resultado": result, "Tipo": output_unit})



if __name__ == '__main__':
    app.run(debug=False)