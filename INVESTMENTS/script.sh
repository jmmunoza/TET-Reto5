python INVESTMENTS/src/calculate_stock_prices.py -r emr s3://jmmunoza-lab-emr/data/INVESTMENTS/data/dataempresas.txt  --conf-path=mrjob.conf --cluster-id=j-1W9CLE4ROVQNH --output-dir=s3://jmmunoza-lab-emr/data/INVESTMENTS/result_calculate_stock_prices
python INVESTMENTS/src/stable_stocks.py -r emr s3://jmmunoza-lab-emr/data/INVESTMENTS/data/dataempresas.txt  --conf-path=mrjob.conf --cluster-id=j-1W9CLE4ROVQNH --output-dir=s3://jmmunoza-lab-emr/data/INVESTMENTS/result_stable_stocks
python INVESTMENTS/src/black_day.py -r emr s3://jmmunoza-lab-emr/data/INVESTMENTS/data/dataempresas.txt  --conf-path=mrjob.conf --cluster-id=j-1W9CLE4ROVQNH --output-dir=s3://jmmunoza-lab-emr/data/INVESTMENTS/result_black_day