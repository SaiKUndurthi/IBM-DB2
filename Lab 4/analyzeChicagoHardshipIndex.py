import testDB2Connection as connectionObject;
import sqlalchemy
from sqlalchemy import *
import config;

chicago_socioeconomic_data = connectionObject.pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv');
print(chicago_socioeconomic_data);
db2 = sqlalchemy.create_engine(config.ibm_db_sa);
chicago_socioeconomic_data.to_sql('chicago_socioeconomic_data',con=db2,if_exists='fail');