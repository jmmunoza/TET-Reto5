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


# 2.3. Ejercicio 3

```sh
python DIAN/src/employee_sector_history.py -r emr s3://jmmunoza-lab-emr/data/DIAN/data/dataempleados.txt  --conf-path=mrjob.conf --cluster-id=<CLUSTERID> --output-dir=s3://jmmunoza-lab-emr/data/DIAN/employeesectorhistory
```

![image](https://github.com/jmmunoza/TET-Reto5/assets/69641274/b2e60008-1a73-4f5c-97be-0dfaff2a2364)

