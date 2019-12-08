import os


def extract_name(name):
    return name.split('.')[0]


def read_lines(filename):
    _file = open(os.path.join('data/meta-data', filename), 'rt')
    data = _file.read().split('\n')
    _file.close()
    return data


def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            metadata.append(tuple(column.split('\t'[:3])))
    return metadata


def prompt():
    print("\nO que deseja ver?")
    print("(l) Listar entidades")
    print("(d) Exibir atributos de uma entidade")
    print("(r) Exibir referências de uma entidade")
    print("(s) Sair do programa")
    return input('')


def main():
    # dicionário nome entidade -> atributos
    meta = {}

    # dicionário identificador -> nome entidade
    keys = {}

    # dicionário de relacionamentos
    relationships = {}

    for meta_data_file in os.listdir('data/meta-data'):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            _col = col[0]
            if _col in keys and not _col == meta[key][0][0]:
                relationships[key] = keys[_col]

    opcao = prompt()
    while opcao != 's':
        if opcao == 'l':
            for entity_name in meta.keys():
                print(entity_name)
        elif opcao == 'd':
            entity_name = input('Nome da entidade: ')
            for col in meta[entity_name]:
                print(col)
        elif opcao == 'r':
            entity_name = input('Nome da entidade: ')
            if relationships.__contains__(entity_name):
                other_entity = relationships[entity_name]
                print(other_entity)
            else:
                print('Não existe referência para {}'.format(entity_name))
        else:
            print('Inexistente\n')
        opcao = prompt()


if __name__ == "__main__":
    main()
