docker-compose -f local.yaml up --build -d
sleep 20

docker exec -i fastapi-template-db-1 mysql -uroot -ppass123 -e "CREATE TABLE string_table (id INT NOT NULL AUTO_INCREMENT, string_text VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, PRIMARY KEY (id));" my_project