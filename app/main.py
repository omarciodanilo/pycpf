# imports do Python
from flask import Flask, render_template, request, jsonify, g
import psycopg2
import time

# import dos módulos do projeto
from pycpf import converte_cpf, gera_cpf, verifica_cpf, calcula_dv, compara_dv, verifica_uf

app = Flask(__name__)

dict_cpf = {
	'cpf': '',
	'situacao': '',
	'uf': '',
}

# Comunicação com o PostgreSQL
conexao_db = psycopg2.connect(
    database="pycpfdb",
    host="localhost",
    user="pycpf",
    password="pycpf",
    port="5432"
)

@app.before_request
def iniciar_timer():
    g.start_time = time.time()

@app.after_request
def logs_requisicoes(response):
    tempo_execucao = time.time() - g.start_time

    metodo_http = request.method.upper()
    interacao = bool(request.get_data() or request.values)
    pagina = request.endpoint.upper() if request.endpoint else 'DESCONHECIDO'
    status_http = response.status_code

    insert_sql = """
        INSERT INTO logs_requisicoes (metodo_http, interacao, pagina, status_http, tempo_execucao) VALUES (%s, %s, %s, %s, %s);
    """
    cursor = conexao_db.cursor()
    cursor.execute(insert_sql, (
        metodo_http,
        interacao,
        pagina,
        status_http,
        tempo_execucao
        )
    )
    conexao_db.commit()
    cursor.close()
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['GET', 'POST'])
def gerar():
	cpf = gera_cpf()
	
	while cpf.count(cpf[0]) == 11:
		cpf = gera_cpf()
	uf = verifica_uf(cpf[8])
	cpf = converte_cpf(cpf)
	dict_cpf['cpf'] = cpf
	dict_cpf['situacao'] = "correto"
	dict_cpf['uf'] = uf
	return jsonify(dict_cpf)

@app.route('/validar', methods=['GET', 'POST'])
def validar():
	if request.method == 'POST':
		cpf = request.form.get('cpf')
	elif type(request.args.get('cpf')) is str:
		cpf = request.args.get('cpf')
		
	if verifica_cpf(cpf):
		primeiro_dv = calcula_dv(cpf, 10)
		segundo_dv = calcula_dv(cpf, 11)
		situacao = compara_dv(cpf, primeiro_dv, segundo_dv)
		if situacao == 'correto':
			uf = verifica_uf(cpf[8])
		else:
			uf = ''
	else:
		situacao = 'incorreto'
		uf = ''
	dict_cpf['cpf'] = cpf
	dict_cpf['situacao'] = situacao
	dict_cpf['uf'] = uf
	return jsonify(dict_cpf)

if __name__ == '__main__':
    main()
