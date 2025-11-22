# imports do Python
from flask import Flask, render_template, request

# import dos módulos do projeto
from pycpf import converte_cpf, gera_cpf, verifica_cpf, calcula_dv, compara_dv, verifica_uf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['GET', 'POST'])
def gerar():
	lista_cpf = []
	cpf = gera_cpf()
	while cpf.count(cpf[0]) == 11:
		cpf = gera_cpf()
	uf = verifica_uf(cpf[8])
	cpf = converte_cpf(cpf)
	lista_cpf = [cpf, uf]
	return lista_cpf

@app.route('/validar', methods=['GET', 'POST'])
def validar():
	lista_cpf = []
	cpf = ''
	
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
	lista_cpf = [cpf, situacao, uf]
	return lista_cpf

if __name__ == '__main__':
    main()
