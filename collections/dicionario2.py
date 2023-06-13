from collections import Counter

texto1 = '''
O Parque Nacional Yellowstone é um dos destinos mais impressionantes para os amantes da natureza. Localizado principalmente no estado de Wyoming, nos Estados Unidos, o parque é conhecido por sua paisagem diversificada, que inclui montanhas majestosas, rios serpenteantes, cachoeiras deslumbrantes e uma abundância de vida selvagem.
Com uma área de mais de 8.900 quilômetros quadrados, o Parque Nacional Yellowstone é considerado o primeiro parque nacional dos Estados Unidos e também o primeiro parque nacional do mundo. Foi estabelecido em 1872 pelo presidente Ulysses S. Grant, com o objetivo de preservar a beleza natural e os ecossistemas únicos da região.
Uma das características mais famosas do parque é o seu conjunto de gêiseres, com destaque para o famoso Old Faithful. O Old Faithful é um gêiser previsível e confiável, que entra em erupção aproximadamente a cada 90 minutos, lançando água quente a uma altura impressionante. Os visitantes podem testemunhar esse espetáculo natural e explorar as trilhas ao redor dos gêiseres, admirando a incrível geologia do parque.
Além dos gêiseres, o Parque Nacional Yellowstone abriga uma variedade de vida selvagem, incluindo ursos, alces, bisões, lobos e águias. Os entusiastas da observação de aves também encontrarão uma ampla variedade de espécies para observar e fotografar. As atividades no parque incluem caminhadas, camping, pesca, passeios de barco e observação da vida selvagem.
'''

texto2 = '''
A inteligência artificial (IA) tem sido um dos campos mais empolgantes e em rápido crescimento da tecnologia nas últimas décadas. A IA é a capacidade de uma máquina ou sistema de computador de imitar a inteligência humana e realizar tarefas que normalmente exigiriam a intervenção humana.
Existem várias abordagens para a implementação da inteligência artificial, incluindo a aprendizagem de máquina (machine learning), a visão computacional, o processamento de linguagem natural e as redes neurais artificiais. Essas técnicas permitem que os sistemas de IA aprendam com dados, reconheçam padrões, tomem decisões e executem tarefas de forma autônoma.
A inteligência artificial está sendo amplamente aplicada em uma variedade de setores e áreas, incluindo medicina, finanças, transporte, educação e entretenimento. Por exemplo, na área médica, a IA pode ajudar a diagnosticar doenças, interpretar exames de imagem e desenvolver tratamentos personalizados. Na indústria automotiva, a IA é utilizada para o desenvolvimento de veículos autônomos.
Apesar de todos os avanços e benefícios da inteligência artificial, também surgem questões éticas e preocupações relacionadas à privacidade e segurança dos dados. A medida que a IA continua a evoluir, é importante equilibrar o progresso tecnológico com salvaguardas adequadas e garantir que a implementação da inteligência artificial seja feita de forma responsável e ética.
'''

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = Counter(dict([(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()])).most_common()
    for caractere, proporcao in proporcoes:
        print(f'{caractere} => {proporcao * 10:.2f}%')

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)