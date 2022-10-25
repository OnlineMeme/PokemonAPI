import requests
from flask import Flask, render_template, request, jsonify, flash

app = Flask(__name__)
app.secret_key = 'test'


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        pokemon_name = request.form['pokemon'].lower()
        sprites = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon_name)
        names = requests.get('https://pokeapi.co/api/v2/pokemon-species/' + pokemon_name)
        en_flavor = " "
        
        try:
            sprite_data = sprites.json()
            name_data = names.json()
        except:
            flash('Invalid Pokemon Name or ID - Please Try Again')
            return render_template('index.html')

        for flavor in name_data['flavor_text_entries']:
            if flavor['language']['name'] == "en":
                en_flavor = flavor['flavor_text']
                break
            
        return render_template('pokeinfo.html', sprite_data=sprite_data, name_data=name_data, en_flavor=en_flavor)

    return render_template('index.html')
