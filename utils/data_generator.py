"""
data_generator.py

Este arquivo é responsável por gerar dados dinâmicos e aleatórios para os testes.
Exemplos: nomes, emails, endereços, senhas, ou qualquer dado necessário para
preencher formulários.  

Objetivo: evitar que os testes precisem criar dados manualmente, tornando-os
mais realistas, independentes e reutilizáveis.
"""
from faker import Faker

fake = Faker("pt_BR")

# Dados pessoais
nome = fake.name()
primeiro_nome = fake.first_name()
sobrenome = fake.last_name()
username = fake.user_name()
senha = fake.password()

# Contato
email = fake.email()
telefone = fake.phone_number()
celular = fake.cellphone_number()

# Documentos
cpf = fake.cpf()

# Dados demográficos
idade = str(fake.random_int(min=18, max=65))
data_nascimento = fake.date_of_birth()
genero = fake.random_element(elements=("Masculino", "Feminino"))

# Endereço
endereco = fake.address()
rua = fake.street_name()
numero = fake.building_number()
cidade = fake.city()
estado = fake.state()
pais = fake.country()
cep = fake.postcode()

# Profissional
empresa = fake.company()
cargo = fake.job()
salario = str(fake.random_int(min=2000, max=20000))
departamento = fake.random_element(elements=("QA", "Dev", "RH", "Financeiro"))

# Internet
url = fake.url()
dominio = fake.domain_name()
ip = fake.ipv4()
mac_address = fake.mac_address()

# Financeiro
cartao_credito = fake.credit_card_number()
bandeira_cartao = fake.credit_card_provider()
moeda = fake.currency_name()

# Datas
data = fake.date()
data_hora = fake.date_time()
ano = fake.year()
mes = fake.month()

# Texto
frase = fake.sentence()
paragrafo = fake.paragraph()
texto = fake.text(max_nb_chars=200)

# Segurança
hash_sha256 = fake.sha256()
uuid = fake.uuid4()

# Veículos
placa = fake.license_plate()

# Localização
latitude = fake.latitude()
longitude = fake.longitude()

# Arquivos
nome_arquivo = fake.file_name()
extensao = fake.file_extension()
mime_type = fake.mime_type()

# Extras
cor = fake.color_name()
user_agent = fake.user_agent()


def gerar_dados():
    return {
        # Dados pessoais
        "primeiro_nome": fake.first_name(),
        "sobrenome": fake.last_name(),
        "nome_completo": fake.name(),
        "username": fake.user_name(),
        "senha": fake.password(),

        # Contato
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "celular": fake.cellphone_number(),

        # Documentos
        "cpf": fake.cpf(),

        # Demográficos
        "idade": str(fake.random_int(min=18, max=65)),
        "data_nascimento": str(fake.date_of_birth()),
        "genero": fake.random_element(elements=("Masculino", "Feminino")),

        # Endereço
        "endereco": fake.address(),
        "rua": fake.street_name(),
        "numero": fake.building_number(),
        "cidade": fake.city(),
        "estado": fake.state(),
        "pais": fake.country(),
        "cep": fake.postcode(),

        # Profissional
        "empresa": fake.company(),
        "cargo": fake.job(),
        "salario": str(fake.random_int(min=2000, max=20000)),
        "departamento": fake.random_element(elements=("QA", "Dev", "RH", "Financeiro")),

        # Internet
        "url": fake.url(),
        "dominio": fake.domain_name(),
        "ip": fake.ipv4(),
        "mac_address": fake.mac_address(),

        # Financeiro
        "cartao_credito": fake.credit_card_number(),
        "bandeira_cartao": fake.credit_card_provider(),
        "moeda": fake.currency_name(),

        # Datas
        "data": str(fake.date()),
        "data_hora": str(fake.date_time()),
        "ano": fake.year(),
        "mes": fake.month(),

        # Texto
        "frase": fake.sentence(),
        "paragrafo": fake.paragraph(),
        "texto": fake.text(max_nb_chars=200),

        # Segurança
        "hash_sha256": fake.sha256(),
        "uuid": fake.uuid4(),

        # Veículos
        "placa": fake.license_plate(),

        # Localização
        "latitude": str(fake.latitude()),
        "longitude": str(fake.longitude()),

        # Arquivos
        "nome_arquivo": fake.file_name(),
        "extensao": fake.file_extension(),
        "mime_type": fake.mime_type(),

        # Extras
        "cor": fake.color_name(),
        "user_agent": fake.user_agent()
    }