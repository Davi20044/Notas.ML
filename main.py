import csv
import math

# Carregar dados do arquivo
def load_data(filename):
    data = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Ignorar cabeçalho
        for row in csv_reader:
            id, name = row[0], row[1]
            grades = [float(x) for x in row[2:] if x]  # Ignorar valores vazios
            data[id] = {'name': name, 'grades': grades}
    return data

# Calcular a média
def mean(values):
    return sum(values) / float(len(values))

# Calcular a variação entre as notas e a média da variação
def calculate_variation(grades):
    variations = [grades[i+1] - grades[i] for i in range(len(grades)-1)]
    return mean(variations)

# Arredondar para o inteiro mais próximo ou meio inteiro
def round_half(num):
    return math.floor(num * 2) / 2

# Fazer uma previsão
def predict_next_grade(train_data):
    predictions = {}
    for id, data in train_data.items():
        grades = data['grades']
        if len(grades) < 2:  # Precisamos de pelo menos duas notas para fazer uma previsão
            print(f"Não há notas suficientes para o aluno com ID {id} para fazer uma previsão.")
            continue
        variation_mean = calculate_variation(grades)
        min_grade = round_half(grades[-1] - variation_mean)
        max_grade = round_half(grades[-1] + variation_mean)
        if min_grade == max_grade:
            predictions[id] = {'grade': min_grade}
        else:
            predictions[id] = {'min': min_grade, 'max': max_grade}
    return predictions

# Carregar e preparar dados
dataset = load_data('notas.csv')

# Fazer uma previsão
predictions = predict_next_grade(dataset)

# Informe o ID ou nome do aluno para prever a próxima nota
student_id = input("Informe o ID ou nome do aluno: ")
if student_id in predictions:
    if 'grade' in predictions[student_id]:
        print('A próxima nota prevista para o aluno com ID {} é: {:.2f}'.format(student_id, predictions[student_id]['grade']))
    else:
        print('A próxima nota prevista para o aluno com ID {} está entre {:.2f} e {:.2f}'.format(student_id, predictions[student_id]['min'], predictions[student_id]['max']))
else:
    print('Aluno não encontrado.')
