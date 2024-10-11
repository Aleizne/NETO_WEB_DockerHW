# Сборка образа

docker build -t my_smart_home . 

# Запуск контейнера

docker run --name smart_home_container -d -p 8000:8000 my_smart_home