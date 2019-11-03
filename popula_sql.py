import sqlite3

connection = sqlite3.connect('db.sqlite3')
c = connection.cursor()

def dataEmpresa():
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Merovech Maggot", "25.893.823/0001-14")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Leufroy Goodbody", "61.682.777/0001-78")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Bandobras Burrows", "86.087.593/0001-90")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Chlodomer Burrowes", "02.201.151/0001-33")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Reginar Lightfoot", "02.774.735/0001-06")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Rudolph Silentfoot", "90.578.109/0001-01")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Helinand Proudbody", "15.014.446/0001-42")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Chlodion Brandagamba", "23.502.031/0001-46")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Sergius Farfoot", "57.829.874/0001-73")')
    connection.execute('Insert into catalogs_empresa (nome, CNPJ) values("Scudamor Leafwalker", "77.835.434/0001-36")')

    connection.commit()

#dataEmpresa()

def dataNotaFiscal():
    connection.execute('Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
                      'values ("honni456", 741, "Arnis", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    '''
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni457", 215, "Gunnor", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni458", 8747, "Asvard", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni459", 3456, "Vermundr", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni460", 896, "Mord", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni461", 747, "Gilling", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni462", 36543, "Eric", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni463", 78, "Balder", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni464", 363, "Hrani", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    connection.execute(
        'Insert into catalogs_notafiscal (serie, numero, nome_descricao, peso, cubagem, data, empresa_id) '
        'values ("honni465", 78, "Tor", 96.63, 52.6,"2019-06-28 20:57:32.352790",26)')
    '''
    connection.commit()

#dataNotaFiscal()

def Truncate():
    connection.execute('Delete from catalogs_notafiscal')
    connection.execute('Delete from catalogs_empresa')
    connection.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name = "catalogs_empresa"')
    connection.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name = "catalogs_notafiscal"')

    connection.commit()

Truncate()