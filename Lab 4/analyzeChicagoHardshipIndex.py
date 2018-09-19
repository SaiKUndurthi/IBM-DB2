import testDB2Connection as connectionObject;
import sqlalchemy
from sqlalchemy import *
import config;
import matplotlib.pyplot as plt;
import seaborn as sns;

chicago_socioeconomic_data = connectionObject.pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv');
db2 = sqlalchemy.create_engine(config.ibm_db_sa);
income_vs_hardship_query = "SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data";
income_vs_hardship = connectionObject.pandas.read_sql(income_vs_hardship_query, connectionObject.pconn);
print(income_vs_hardship.dtypes);
plot = sns.jointplot(x="PER_CAPITA_INCOME_", y="HARDSHIP_INDEX", data=income_vs_hardship)
plt.show();
connectionObject.ibm_db.close(connectionObject.conn)