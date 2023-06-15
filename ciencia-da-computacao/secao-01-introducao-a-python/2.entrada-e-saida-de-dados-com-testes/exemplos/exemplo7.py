import csv

with open("graduacao_unb.csv", encoding="utf-8") as file:
    # Os valores padrão de 'delimiter' e 'quotechar' são os mesmos utilizados
    # abaixo. Você pode removê-los ou alterá-los conforme necessidade
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')

    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader

group_by_department = {}
for row in data:
    department = row[15]
    if department not in group_by_department:
        group_by_department[department] = 0
    group_by_department[department] += 1

# Escreve o relatório em .csv
# Abre um arquivo para escrita
with open("department_report.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Escreve o cabeçalho
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    writer.writerow(headers)

    # Escreve as linhas de dados
    # Desempacotamento de valores
    for department, grades in group_by_department.items():
        # Agrupa o dado com o turno
        row = [
            department,
            grades,
        ]
        writer.writerow(row)

# Baseado em dicionarios

# A linha de cabeçalhos é utilizada como chave do dicionário
# agrupa cursos por departamento
    group_by_department = {}
    for row in graduacao_reader:
        department = row["unidade_responsavel"]
        if department not in group_by_department:
            group_by_department[department] = 0
        group_by_department[department] += 1
