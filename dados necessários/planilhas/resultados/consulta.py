import pandas as pd

# Carregar os dados em DataFrames
perfil_eleitorado = pd.read_csv('perfil_eleitorado_2020.csv', sep=';', encoding='latin1')
resultados = pd.read_csv('sp_turno_1.csv', sep=';', encoding='latin1')

# Filtrar os dados para o estado de São Paulo
perfil_sp = perfil_eleitorado[perfil_eleitorado['SG_UF'] == 'SP']
resultados_sp = resultados[resultados['SG_UF'] == 'SP']

# Consulta para saber qual candidato foi mais votado em cada município
candidato_mais_votado_por_municipio = resultados_sp.groupby(['NM_MUNICIPIO', 'NM_VOTAVEL'])['QT_VOTOS'].sum().reset_index()
idx = candidato_mais_votado_por_municipio.groupby('NM_MUNICIPIO')['QT_VOTOS'].idxmax()
candidato_mais_votado_por_municipio = candidato_mais_votado_por_municipio.loc[idx]

print(candidato_mais_votado_por_municipio[['NM_MUNICIPIO', 'NM_VOTAVEL', 'QT_VOTOS']])

# Consulta para saber qual perfil do eleitorado mais votou em cada candidato
perfil_resultados = pd.merge(resultados_sp, perfil_sp, on='CD_MUNICIPIO')
perfil_resultados_agrupados = perfil_resultados.groupby(['NM_VOTAVEL', 'DS_GENERO', 'DS_FAIXA_ETARIA', 'DS_GRAU_ESCOLARIDADE'])['QT_VOTOS'].sum().reset_index()
idx = perfil_resultados_agrupados.groupby(['NM_VOTAVEL', 'DS_GENERO', 'DS_FAIXA_ETARIA', 'DS_GRAU_ESCOLARIDADE'])['QT_VOTOS'].idxmax()
perfil_mais_votado_por_candidato = perfil_resultados_agrupados.loc[idx]

print(perfil_mais_votado_por_candidato[['NM_VOTAVEL', 'DS_GENERO', 'DS_FAIXA_ETARIA', 'DS_GRAU_ESCOLARIDADE', 'QT_VOTOS']])
