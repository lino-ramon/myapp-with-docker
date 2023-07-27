echo Criando imagens docker e iniciando os containers.
docker-compose build
docker-compose down
docker-compose up -d

echo Aguardando o serviço MySql ficar UP.
timeout 100
type api\db\script.sql | docker exec -i mysql-container mysql -uroot -pmypassword123
