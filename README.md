# Tópicos Especiales en Telemática | Reto 5

* Juan Manuel Muñoz Arias

# 1. Introducción
Este reto busca reforzar los conocimientos acerca de EMR y Hadoop, mediante la realización de varios ejercicios con MrJob y Python.

# 1.1 Configuración del entorno

Primero que todo, es necesario crear un entorno virtual en Python (preferiblemente 3.x) e instalar las librerías necesarias con este comando

```sh
pip install -r requirements.txt
```

Una vez listo, habrá que configurar MrJob para que se pueda comunicar a AWS sobre boto3.

```sh
runners:
    emr:
        aws_secret_access_key: <Tu access key de AWS>
        aws_access_key_id: <Tu access key id de AWS>
        aws_session_token: <Tu session token de AWS>
        region: <Tu región de AWS>
        ec2_key_pair_file: <Ruta a tu key .pem de AWS>
        ec2_key_pair: <Nombre de tu key .pem de AWS>
        ssh_tunnel: true
```

Y eso será todo lo necesario para empezar a correr programas.

# 2. Ejercicios de la DIAN

En la carpeta data se almacenan los datasets mientras que en el resto se encuentran los resultados de cada programa.

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/6a6c4e65-0188-46c9-84b5-722bd67ec06d)

Estos son los comando con el cual se corrieron los programas y sus resultados.

# 2.1. Ejercicio 1

```sh
python DIAN/src/average_sector_salary.py -r emr s3://jmmunoza-lab-emr/data/DIAN/data/dataempleados.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/DIAN/resultaveragesectorsalary
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/4e189b64-8edc-477b-8a0b-32ce3ab8217c)


# 2.2. Ejercicio 2

```sh
python DIAN/src/average_employee_salary.py -r emr s3://jmmunoza-lab-emr/data/DIAN/data/dataempleados.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/DIAN/resultaverageemployeesalary
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/f415aaa0-3e70-469d-a662-71144901f2a1)

# 3. Ejercicios de las Acciones

En la carpeta data se almacenan los datasets mientras que en el resto se encuentran los resultados de cada programa.

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/b4167c25-2da8-421e-99ff-e7923b35a04a)

Estos son los comando con el cual se corrieron los programas y sus resultados.

# 3.1. Ejercicio 1

```sh
python INVESTMENTS/src/calculate_stock_prices.py -r emr s3://jmmunoza-lab-emr/data/INVESTMENTS/data/dataempresas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/INVESTMENTS/result_calculate_stock_prices
```
![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/4e994812-3182-4969-8bad-3cec098155fb)


# 3.2. Ejercicio 2

```sh
python INVESTMENTS/src/stable_stocks.py -r emr s3://jmmunoza-lab-emr/data/INVESTMENTS/data/dataempresas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/INVESTMENTS/result_stable_stocks
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/b18c11d0-04db-44b0-b42d-9c01e4c789a3)


# 3.3. Ejercicio 3

```sh
python INVESTMENTS/src/black_day.py -r emr s3://jmmunoza-lab-emr/data/INVESTMENTS/data/dataempresas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/INVESTMENTS/result_black_day
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/adca5ade-e5e9-4225-9ca4-34d021a227ff)


# 4. Ejercicios de las Películas

En la carpeta data se almacenan los datasets mientras que en el resto se encuentran los resultados de cada programa.

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/112eef32-6576-414c-9222-b4e693f13dd1)

Estos son los comando con el cual se corrieron los programas y sus resultados.

# 4.1. Ejercicio 1

```sh
python MOVIES/src/day_best_average_rating.py -r emr s3://jmmunoza-lab-emr/data/MOVIES/data/datapeliculas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/MOVIES/day_best_average_rating
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/735b1609-8c61-4d42-b871-abbecbc6c032)


# 4.2. Ejercicio 2

```sh
python MOVIES/src/day_with_less_movies.py -r emr s3://jmmunoza-lab-emr/data/MOVIES/data/datapeliculas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/MOVIES/day_with_less_movies
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/e4e19ad6-984e-4835-a439-6eff4a11c0df)


# 4.3. Ejercicio 3

```sh
python MOVIES/src/day_with_more_movies.py -r emr s3://jmmunoza-lab-emr/data/MOVIES/data/datapeliculas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/MOVIES/day_with_more_movies
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/4c304344-286e-47ad-8fb3-17235d4c8b10)


# 4.4. Ejercicio 4

```sh
python MOVIES/src/day_worst_average_rating.py -r emr s3://jmmunoza-lab-emr/data/MOVIES/data/datapeliculas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/MOVIES/day_worst_average_rating
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/5032115b-7a62-4ab0-b2e4-576cbd4dbf1d)

# 4.5. Ejercicio 5

```sh
python MOVIES/src/movies_per_user.py -r emr s3://jmmunoza-lab-emr/data/MOVIES/data/datapeliculas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/MOVIES/movies_per_user
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/af715785-7552-4e37-b27b-810ab97e1d72)

# 4.6. Ejercicio 6

```sh
python MOVIES/src/users_per_movie.py -r emr s3://jmmunoza-lab-emr/data/MOVIES/data/datapeliculas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/MOVIES/users_per_movie
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/22d734c2-4d29-4b3e-90c9-5eb894cdc220)

# 4.7. Ejercicio 7

```sh
python MOVIES/src/worst_best_movie_per_genre.py -r emr s3://jmmunoza-lab-emr/data/MOVIES/data/datapeliculas.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/MOVIES/worst_best_movie_per_genre
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/51e8154a-fdd4-4243-896b-80302b95bffe)

