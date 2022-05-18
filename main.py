from flask import Flask, request, redirect
from processing import process_data

app = Flask(__name__, static_folder='result')
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def file_summer_page():
    if request.method == "POST":
        input_file = request.files["input_file"]
        input_data = input_file.stream.read().decode("utf-8")
        output_data = process_data(input_data)
        print(output_data)
        
        textfile = open(app.static_folder+"/perfis.txt", "w")
        for element in output_data:
          textfile.write(element + "\n")
        textfile.close()
      
        return redirect("https://findprofile.soulevanscfal.repl.co/result/perfis.txt", code=302)
        #response.headers["Content-Disposition"] = "attachment; filename=perfis.txt"
        #return response
    return '''
        <html>
            <body>
                <p>Selecione o arquivo contendo a lista de nomes:</p>
                <form method="post" action="." enctype="multipart/form-data">
                    <p><input type="file" name="input_file" /></p>
                    <p><input type="submit" value="Procurar perfis" /></p>
                </form>
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)