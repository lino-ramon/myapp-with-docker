from flask import Flask, jsonify
import mysql.connector
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': '172.17.0.3',
    'port': '3306',
    'user': 'root',
    'password': 'mypassword123',
    'database': 'mydatabase',
}

# Endpoint para obter os produtos
@app.route('/products', methods=['GET'])
def get_products():
    try:
        logger.info("=> Iniciando busca de produtos no MySql")
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Executando a query para obter os dados da tabela "products"
        cursor.execute('SELECT * FROM products')
        products_data = cursor.fetchall()

        logger.debug("=> Lendo produtos do MySql - Produtos: [%s]", products_data)
        # Convertendo a lista de tuplas em um dicionário para facilitar a conversão em JSON
        products_list = []
        for product in products_data:
            product_dict = {
                'id': product[0],
                'name': product[1],
                'price': float(product[2])
            }
            products_list.append(product_dict)

        cursor.close()
        connection.close()

        return jsonify(products_list)

    except Exception as e:
        logger.exception("=> Erro na leitura dos produtos - Erro: [%s]", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)-6s - %(message)s',
        encoding='utf-8',
        handlers=[
            logging.StreamHandler()
        ]
    )
    logger.info("=> Iniciando aplicação na porta 9001!")
    app.run(debug=True, host='0.0.0.0', port=9001)
