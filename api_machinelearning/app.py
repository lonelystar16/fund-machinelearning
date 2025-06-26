# 1. IMPORTAR LIBRERÍAS
import flask
import pickle
import pandas as pd

# 2. CARGAR EL MODELO Y LAS COLUMNAS
# Cargamos el modelo y las columnas desde los archivos .pkl que creamos.
# Esto se hace solo una vez cuando la aplicación se inicia.
with open('checkpoints/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('checkpoints/model_columns.pkl', 'rb') as f:
    model_columns = pickle.load(f)

# 3. CREAR LA INSTANCIA DE LA APLICACIÓN FLASK
# Asignamos el constructor de Flask a la variable 'app'[cite: 109].
app = flask.Flask(__name__, template_folder='templates')


# 4. DEFINIR LAS RUTAS DE LA API
# La ruta principal ('/') mostrará el formulario HTML.
# app.route() es un decorador que le dice a Flask qué URL debe activar nuestra función[cite: 110].
@app.route('/', methods=['GET', 'POST'])
def main():
    
    # Si el método es GET, simplemente mostramos la página con el formulario.
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    # Si el método es POST, significa que el usuario ha enviado datos.
    if flask.request.method == 'POST':
        
        # Recogemos los datos del formulario.
        # La presentación usa request.form.to_dict()[cite: 141], nosotros construiremos el DataFrame directamente.
        input_variables = pd.DataFrame([[
            flask.request.form['MatchFlankKills'],
            flask.request.form['TeamStartingEquipmentValue'],
        ]],
            columns=model_columns, # model_columns ahora tiene 2 nombres, coincidiendo con los datos
            dtype=float,
            index=['input'])

        # Hacemos la predicción con nuestro modelo cargado.
        prediction_code = model.predict(input_variables)[0]
        
        # Mapeamos el resultado numérico (0 o 1) a un texto legible.
        if prediction_code == 1:
            prediction_text = 'Alto Desempeño'
        else:
            prediction_text = 'No Alto Desempeño'

        # Devolvemos la misma página, pero ahora incluyendo el resultado de la predicción.
        # Esto es similar a como la presentación muestra el resultado en 'result.html'[cite: 121].
        return flask.render_template('main.html',
                                    result=prediction_text)

# 5. PUNTO DE ENTRADA PARA EJECUTAR LA APLICACIÓN
if __name__ == '__main__':
    # app.run() inicia el servidor web.
    app.run()