Foram desenvolvidas 2 rotas.

Sendo elas 1 crud completo para cadastro, edição, exclusão e listagem de Produtores.
Outra rota para cadastro de dashboard.

A rota relacionada ao crud tem todas as regras de negócios exigidas no teste, com uma observação.

Para validação de CPF E/OU CNPJ utilizei uma biblioteca que tem "ligação" direta com a RF, então para cadastro de novos produtores é necessário que seja um cpf ou cnpj válido e que ainda não tenha sido utilizado.
Essa lib é algo de suma facilidade que o Python disponibiliza para esse tipo de validação.

Configurei também o projeto para rodar no docker e no Postgress como foi pedido.
No projeto vai o docker-compose e file com as configs para rodar o container e também as configs criadas para o banco de dados.

E um arquivo requirements.txt com as libs usadas.


Segue abaixo o json usado para cadastro de um novo Produtor.

{

            "cpf_cnpj": "44209275859",
            "nome": "Fulano de Tal",
            "nome_fazenda": "Fazenda Feliz",
            "cidade": "Salvador",
            "estado": "Bahia",
            "area_total_hectares": "100.00",
            "area_agricultavel_hectares": "80.00",
            "area_vegetacao_hectares": "20.00",
            "culturas": ["Café", "Cana de Açucar"]
      }

Neste caso usei o meu próprio CPF para disponibilizar um retorno válido, porém usei outros que tinha disponíveis para cadastrar, testar também a adição ou exclusão de várias cultas ou validar as regras dos tamanhos e por fim a exclusão, deixando somente o que usei meu documento salvo no banco.

Caso fique alguma dúvida estarei a disposição.
