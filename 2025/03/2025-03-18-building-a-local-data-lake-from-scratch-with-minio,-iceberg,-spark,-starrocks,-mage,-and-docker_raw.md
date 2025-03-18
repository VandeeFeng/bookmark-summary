Title: Building a Local Data Lake from scratch with MinIO, Iceberg, Spark, StarRocks, Mage, and Docker

URL Source: https://blog.det.life/building-a-local-data-lake-from-scratch-with-minio-iceberg-spark-starrocks-mage-and-docker-c12436e6ff9d

Published Time: 2024-07-13T00:55:21.139Z

Markdown Content:
[![Image 1: George Zefkilis](https://miro.medium.com/v2/resize:fill:88:88/1*fF-jH8breY1SKJs3GGNocg.jpeg)](https://medium.com/@georgioszefkilis?source=post_page---byline--c12436e6ff9d---------------------------------------)

[![Image 2: Data Engineer Things](https://miro.medium.com/v2/resize:fill:48:48/1*HtZXPy85bDrTZm9tMXi6aQ.png)](https://blog.det.life/?source=post_page---byline--c12436e6ff9d---------------------------------------)

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*iZPuMSj7CA_kZI-l6gF3yg.png)

Image from [here](https://tractionwise.com/data-lake-marketing-magie-analytics/)

Hello again, fellow technology enthusiasts! I am a software/data engineer who transitioned from data science. The learning curve in this new role has been quite steep, providing me with the opportunity to work with a plethora of new tools, languages, frameworks, and technologies.

One of the challenges I have faced is quickly developing and testing various technologies and understanding how they interact with each other. Data engineering projects, in particular, are often complex and involve multiple components to simulate an end-to-end system.

In this post, I would like to share some of these technologies and demonstrate how they work together through a small project that I use myself.

Let’s jump into it!!

**The project**
---------------

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*AD7rLnphrGYJjSr7vHldRw.png)

Basic Illustration of the data pipeline

The project aims to demonstrate how to establish a system where you can extract, transform, and load data into a local data lake and query the data using a SQL engine.

> [A data lake stores both relational data from business applications and non-relational data from various sources. Unlike traditional databases, data lakes do not require a predefined schema, allowing you to store all data without prior design. This flexibility enables various types of analytics, including SQL queries, big data analytics, full-text search, real-time analytics, and machine learning, to uncover valuable insights.](https://aws.amazon.com/what-is/data-lake/)

The technologies/frameworks we will use are the following:

1.  [**Docker:**](https://www.docker.com/) You may already be familiar with Docker. If not, it is a technology you must learn, as it significantly accelerates the process of building and testing applications.
2.  [**Mage:**](https://www.mage.ai/) Mage will be our data pipeline orchestrator for building and running our scripts. While not strictly required for this project, as a data engineer, it is essential to familiarise yourself with orchestrating pipelines, and Mage is an excellent tool for this purpose.
3.  [**Spark**](https://spark.apache.org/)**:** Spark, a popular unified analytics engine for large-scale data processing, will be used to perform basic transformations on our data.
4.  [**Minio**](https://min.io/)**:** MinIO is a high-performance, S3-compatible object store. In this project, it will serve as our data lake where we will store our data.
5.  **Apache Iceberg/Delta:** Both [Apache Iceberg](https://iceberg.apache.org/) and [Delta Lake](https://delta.io/) are advanced table formats that enhance data lakes with features like schema evolution, ACID transactions, and time travel. They improve data reliability, query performance, and scalability, making data lakes more efficient for large-scale analytics. In this project, I will demonstrate Iceberg.
6.  [**StarRocks**](https://www.starrocks.io/)**:** StarRocks is a high-performance analytical database that supports real-time and batch data ingestion from various data sources. It allows direct analysis of data stored in data lakes with zero data migration. In our project, it will be used to query data from our data lake.

As you can see, several technologies and frameworks are required to establish a solid foundation for our data lake. While different technologies can be used, the core principles remain the same for any data engineering project.

**Set up services**
-------------------

I will start building the project repository around Mage, as it will serve as the orchestrator and connector between our services. I like Mage for its simplicity and intuitive approach to building robust and scalable data pipelines.

Let’ start!!!

First I create an empty repository and add the following files/folders

1.  `.env`
2.  `Makefile`
3.  `Dockerfile`
4.  `docker-compose.yaml`

In the `.env` file, we will store the credentials needed for our services. Fortunately, we only need two for accessing our Minio services:

MINIO\_ACCESS\_KEY= choose\_a\_key  
MINIO\_SECRET\_KEY= choose\_a\_secret

Additionally, to simplify our workflow and avoid memorizing Docker and other complex commands, we will add the following Makefile to easily call them each time.

  
IMAGE\_NAME = mage\_demoCOMPOSE\_FILE = docker-compose.yaml

build:  
 docker build -t $(IMAGE\_NAME) .

up:  
 docker-compose -f $(COMPOSE\_FILE) up -d

down:  
 docker-compose -f $(COMPOSE\_FILE) down

browse:  
 open http://localhost:6789

create:  
 docker run -it -p 6789:6789 -v path/to/your/project:/home/src mageai/mageai \\  
  /app/run\_app.sh mage start $(IMAGE\_NAME)

Now we need to create our Mage project where our pipelines will run. We will use the following Dockerfile (provided by Mage), which includes a few Spark-specific commands. If you want to use Mage without Spark, you can simply remove the Spark-specific commands.

FROM mageai/mageai:0.9.72ARG PROJECT\_NAME=mage\_demo   
ARG MAGE\_CODE\_PATH=/home/mage\_code  
ARG USER\_CODE\_PATH=${MAGE\_CODE\_PATH}/${PROJECT\_NAME}

WORKDIR ${MAGE\_CODE\_PATH}

COPY ${PROJECT\_NAME} ${PROJECT\_NAME}

ENV USER\_CODE\_PATH=${USER\_CODE\_PATH}

RUN echo 'deb http://deb.debian.org/debian bullseye main' \> /etc/apt/sources.list.d/bullseye.list

RUN apt-get update -y && \\  
    apt-get install -y openjdk-11-jdk wget

RUN rm /etc/apt/sources.list.d/bullseye.list

RUN pip3 install -r ${USER\_CODE\_PATH}/requirements.txt

RUN python3 /app/install\_other\_dependencies.py --path ${USER\_CODE\_PATH}

ENV PYTHONPATH="${PYTHONPATH}:/home/src"

CMD \["/bin/sh", "-c", "/app/run\_app.sh"\]

The `Dockerfile` above will create the Mage project, including a standalone Spark cluster (managing by Mage), avoiding the need to create a separate Spark image (although you can do that too).

Now we need to create the project (remember to change the path to your project in the Makefile). This can be done by simply running the following command in your CLI:

> `_make create_`

Congratulations! You have just set up Mage. You should now see the following in your repository :

![Image 5](https://miro.medium.com/v2/resize:fit:700/1*tqepIn4oNkKDdrmAcbUM_w.png)

Mage file structure (You can restructure it a bit, for example i have the .gitignore in the root directory instead)

You can check the UI as well by running:

> `make browse`

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*S5G9sDDupE6lwM6FeLcTqg.png)

The project is currently empty and built with the `mageai/mageai:latest` image. Once we start adding pipelines, adjusting requirements and to include the Spark cluster, we will build our own image by simply typing:

> `make build`

**Put everything together**
---------------------------

The last file we need to add to our repository is the `docker-compose.yaml` file. Since this project utilizes multiple technologies, we want them to run on the same network. Therefore, we need to create a `docker-compose.yaml` file to ensure they can all run together seamlessly.

version: '3'  
services:  
  mage:  
      
    image: mage\_demo  
    container\_name: mage   
    ports:  
      \- "6789:6789"  
    volumes:  
      \- .:/home/mage\_code  
    environment:  
      MINIO\_ACCESS\_KEY: ${MINIO\_ACCESS\_KEY}  
      MINIO\_SECRET\_KEY: ${MINIO\_SECRET\_KEY}starrocks-fe-0:  
    image: starrocks/fe-ubuntu:latest  
    hostname: starrocks-fe-0  
    container\_name: starrocks-fe-0  
    command:  
      \- /bin/bash  
      \- \-c  
      \- |  
        /opt/starrocks/fe\_entrypoint.sh starrocks-fe-0  
    environment:  
      \- HOST\_TYPE=FQDN  
      \- TZ=Asia/Shanghai  
      \- AWS\_ACCESS\_KEY\_ID=${MINIO\_ACCESS\_KEY}  
      \- AWS\_SECRET\_ACCESS\_KEY=${MINIO\_SECRET\_KEY}  
    ports:  
      \- "8030:8030"  
      \- "9020:9020"  
      \- "9030:9030"  
    volumes:  
       \- singleton\_fe0\_data:/opt/starrocks/fe/meta  
    healthcheck:  
      test: \["CMD", "curl", "-f", "http://localhost:9030"\]  
      interval: 5s  
      timeout: 5s  
      retries: 30

starrocks-be-0:  
    image: starrocks/be-ubuntu:latest  
    hostname: starrocks-be-0  
    container\_name: starrocks-be-0  
    command:  
      \- /bin/bash  
      \- \-c  
      \- |  
        /opt/starrocks/be\_entrypoint.sh starrocks-fe-0  
    environment:  
      \- HOST\_TYPE=FQDN  
      \- TZ=Asia/Shanghai  
    ports:  
      \- "8040:8040"  
    depends\_on:  
      \- starrocks-fe-0  
    volumes:  
      \- singleton\_be0\_data:/opt/starrocks/be/storage

minio:  
    container\_name: minio  
    image: quay.io/minio/minio  
    ports:  
      \- '9000:9000'  
      \- '9001:9001'  
    volumes:  
      \- './minio\_data:/data'  
    environment:  
      \- MINIO\_ROOT\_USER=${MINIO\_ACCESS\_KEY}  
      \- MINIO\_ROOT\_PASSWORD=${MINIO\_SECRET\_KEY}  
    command: server \--console-address ":9001" /data

volumes:  
  singleton\_fe0\_data:  
  singleton\_be0\_data:  
  minio\_data:

The `docker-compose.yaml` file above contains all the technologies we will use for this demo (excluding Spark, as we are using a standalone cluster as described earlier). For MinIO credentials, you can either create a `.env` file (which is always recommended) or hardcode them into the YAML file.

Then you can start all the services together by typing

> `make up`

If you check Docker Desktop or run `docker ps` in your command line, you should see all the containers.

![Image 7](https://miro.medium.com/v2/resize:fit:700/1*_FFQWS-WOIj-I7NZ3Av2EQ.png)

Containers started for all services in docker-compose.yaml

Notice that the image for Mage is the one we built, and the name must match the one specified in the Makefile, aligning with the name given to the image under the Mage service.

Now, let’s check that everything is running correctly.

To check MinIO, go to `localhost:9001`, and you should see the following image.

![Image 8](https://miro.medium.com/v2/resize:fit:700/1*MD8A9KZE62j-M_28nysg1w.png)

Minio log-in page

Once you enter the credentials specified either in the `.env` file or hardcoded in the YAML file, you should see the following:

![Image 9](https://miro.medium.com/v2/resize:fit:700/1*qsH4pG3Pj-6PgmMBvzGavA.png)

Minio interface

Perfect our Minio storage works fine.

Now let’s establish the connection for StarRocks using my go-to database tool, [DBeaver](https://dbeaver.io/). It’s very easy:

1.  Choose a new database connection.
2.  Select MySQL (a StarRocks plugin might be available as well).
3.  Enter the following details:

*   Host: `localhost`
*   Port: `9030`
*   Username: `root`

4\. Test the connection, and you should see the following:s

![Image 10](https://miro.medium.com/v2/resize:fit:700/1*6MWyAcaWu_RF88YL4l-xaQ.png)

Click “OK” and then “Finish.” That’s all there is to it. You will have the connection set up (instead of “mage\_demo,” it will be named “localhost” unless you rename it)

![Image 11](https://miro.medium.com/v2/resize:fit:664/1*cEptKC5jjQ1y9s5Uttc8PQ.png)

Perfect, all our services are now in place except for the last one… Spark!

The most challenging part about Spark was finding the necessary jar files for S3, Iceberg, and Delta (optional). After some searching and a lot of trial and error, I created a `spark-config` folder (added to `.gitignore`) under the `mage_demo` directory with the required jar files shown in the picture. You can find these jar files on [Maven Repository](https://mvnrepository.com/).

![Image 12](https://miro.medium.com/v2/resize:fit:700/1*Qs1mAfqruKpSEoYtrq28jg.png)

Jar files used for configuring Spark

Now, we need to add these jar files to the `spark_config` section in the project's `metadata.yaml` file. Add the following configuration to `spark_config`:

spark\_config:  
    
  app\_name: 'MageSparkSession'  
    
    
  spark\_master: "local"  
    
    
  executor\_env: {}  
    
    
  spark\_jars: \[  
      
    '/home/mage\_code/mage\_demo/spark-config/hadoop-aws-3.3.4.jar',   
    '/home/mage\_code/mage\_demo/spark-config/aws-java-sdk-bundle-1.12.262.jar',  
    '/home/mage\_code/mage\_demo/spark-config/delta-storage-2.4.0.jar',  
    '/home/mage\_code/mage\_demo/spark-config/delta-core\_2.12-2.4.0.jar',  
      
    '/home/mage\_code/mage\_demo/spark-config/bundle-2.26.15.jar',  
    '/home/mage\_code/mage\_demo/spark-config/url-connection-client-2.26.15.jar',  
    '/home/mage\_code/mage\_demo/spark-config/iceberg-spark-runtime-3.5\_2.12-1.5.2.jar',\]  
    
    
  spark\_home:  
    
    
  others: {}

Since we are using a standalone Spark cluster, we will use the local spark-master. If we were using, for example, the Bitnami Spark image, we could adjust the Spark master to `spark://spark:7077` or the appropriate address.

Awesome! Now that we have configured all our services (usually the most time-consuming part when starting a project), we are ready to build our pipelines and see how all the components work together.

**It’s……. Showtime!!!**
-----------------------

If you have completed all the previous steps, let’s begin by adding the following packages to our `requirements.txt` file.

pyspark==3.4.0  
minio  
delta-spark==2.4.0 

Then, build the (Mage) image by running:

make build

Next, spin up the containers with:

make up

Finally, use:

make browse

to open the Mage UI, allowing us to work in parallel with our IDE.

It’s time to configure our Spark session. We will add the Spark session to a factory, allowing us to extend it for other sessions, such as Delta. This `spark_session_factory` enables us to easily switch between configurations and makes the sessions accessible from all pipelines, so we don't need to rebuild them every time.

> [A SparkSession serves as the unified entry point for Spark applications, connecting to all of Spark’s core functionalities, such as RDDs, DataFrames, and Datasets. It provides a consistent interface for working with structured data processing and is one of the first objects you create when developing a Spark SQL application.](https://sparkbyexamples.com/spark/sparksession-explained-with-examples/)

I will demonstrate the process specifically for Iceberg, but the factory concept ensures that you can extend this setup to include multiple sessions as needed.

from pyspark.sql import SparkSession  
from abc import ABC, abstractmethod  
from delta import configure\_spark\_with\_delta\_pipclass SparkSessionFactory(ABC):  
    @abstractmethod  
    def create\_spark\_session(self):  
        pass

@abstractmethod  
    def configure\_s3(self):  
        pass

class IcebergSparkSession:  
    def \_\_init\_\_(self, app\_name, warehouse\_path, s3\_endpoint, s3\_access\_key, s3\_secret\_key):  
        self.app\_name = app\_name  
        self.warehouse\_path = warehouse\_path  
        self.s3\_endpoint = s3\_endpoint  
        self.s3\_access\_key = s3\_access\_key  
        self.s3\_secret\_key = s3\_secret\_key  
        self.spark = self.create\_spark\_session()  
        self.configure\_s3()

def create\_spark\_session(self):  
        packages = \[  
            "hadoop-aws-3.3.4",  
            'org.apache.iceberg:iceberg-spark-runtime-3.5\_2.12-1.5.2',  
            'aws-java-sdk-bundle-1.12.262'  
        \]

builder = SparkSession.builder.appName(self.app\_name) \\  
            .config("spark.jars.packages", ",".join(packages)) \\  
            .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \\  
            .config("spark.sql.catalog.spark\_catalog", "org.apache.iceberg.spark.SparkCatalog") \\  
            .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \\  
            .config("spark.sql.catalog.local.type", "hadoop") \\  
            .config("spark.sql.catalog.local.warehouse", self.warehouse\_path)

return builder.getOrCreate()

def configure\_s3(self):  
        sc = self.spark.sparkContext  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.access.key", self.s3\_access\_key)  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.secret.key", self.s3\_secret\_key)  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.endpoint", self.s3\_endpoint)  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

class DeltaSparkSession(SparkSessionFactory):  
    def \_\_init\_\_(self, app\_name, s3\_endpoint, s3\_access\_key, s3\_secret\_key):  
        self.app\_name = app\_name  
        self.s3\_endpoint = s3\_endpoint  
        self.s3\_access\_key = s3\_access\_key  
        self.s3\_secret\_key = s3\_secret\_key  
        self.spark = self.create\_spark\_session()  
        self.configure\_s3()

def create\_spark\_session(self):  
        extra\_packages = \[  
            "org.apache.hadoop:hadoop-aws:3.3.4",  
            "io.delta:delta-core\_2.12:2.4.0",  
            "aws-java-sdk-bundle-1.12.262",  
            'delta-storage-2.4.0'  
        \]  
        builder = SparkSession.builder.appName(self.app\_name) \\  
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \\  
            .config("spark.sql.catalog.spark\_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")  
        return configure\_spark\_with\_delta\_pip(builder, extra\_packages=extra\_packages).getOrCreate()

def configure\_s3(self):  
        sc = self.spark.sparkContext  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.access.key", self.s3\_access\_key)  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.secret.key", self.s3\_secret\_key)  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.endpoint", self.s3\_endpoint)  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")  
        sc.\_jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

def get\_spark\_session(session\_type, \*\*kwargs):  
    if session\_type == "iceberg":  
        return IcebergSparkSession(\*\*kwargs)  
    elif session\_type == "delta":  
        return DeltaSparkSession(\*\*kwargs)  
    else:  
        raise ValueError("Invalid session type")

Perfect now let’s build our first pipeline. The most important thing we need at this point is… you guessed it..data!! I downloaded some random Airbnb data from [here](https://insideairbnb.com/get-the-data/) and stored it in a file in my project directory . Make sure to add this file to your `.gitignore`.

Creating a pipeline in Mage is very easy. Simply go to the UI, click “New Pipeline,” and select “Standard (Batch)” from the drop-down menu. You should then see the pipeline development interface.

![Image 13](https://miro.medium.com/v2/resize:fit:700/1*r99VjLg-BE_yLHWapqZFxA.png)

Mage UI for pipeline development

For demonstration purposes, we will start by adding a custom block to our project. Typically, you would begin with a data loader, followed by a transformer, and then a data exporter for a classic ETL process. In this custom block, we will write our data to our S3 bucket using the Apache Iceberg format.

from minio import Minio  
from pyspark.sql import SparkSession  
from pyspark.sql import functions as F  
import os  
from mage\_demo.utils.spark\_session\_factory import get\_spark\_sessiondef stop\_existing\_spark\_session():  
    try:  
        existing\_spark = SparkSession.builder.getOrCreate()  
        if existing\_spark:  
            existing\_spark.stop()  
    except Exception as e:  
        print(f"No existing Spark session to stop: {e}")

stop\_existing\_spark\_session()

MINIO\_ACCESS\_KEY = os.environ.get('MINIO\_ACCESS\_KEY')  
MINIO\_SECRET\_KEY = os.environ.get('MINIO\_SECRET\_KEY')

iceberg\_spark\_session = get\_spark\_session(  
    "iceberg",  
    app\_name="MageSparkSession",  
    warehouse\_path="s3a://iceberg-demo-bucket/warehouse",  
    s3\_endpoint="http://minio:9000",  
    s3\_access\_key=MINIO\_ACCESS\_KEY,  
    s3\_secret\_key=MINIO\_SECRET\_KEY  
)  
client = Minio(  
    "minio:9000",  
    access\_key=MINIO\_ACCESS\_KEY,  
    secret\_key=MINIO\_SECRET\_KEY,  
    secure=False  
)

minio\_bucket = "iceberg-demo-bucket"  
found = client.bucket\_exists(minio\_bucket)  
if not found:  
    client.make\_bucket(minio\_bucket)

@custom  
def iceberg\_table\_write(\*args, \*\*kwargs):  
    data\_folder = "mage\_demo/data"    
    for filename in os.listdir(data\_folder):  
        if filename.endswith(".csv"):  
            file\_path = os.path.join(data\_folder, filename)

df = iceberg\_spark\_session.spark.read.csv(file\_path, header=True, inferSchema=True)  
              
            table\_name = f"local.iceberg\_demo.{os.path.splitext(os.path.basename(file\_path))\[0\]}"

if table\_name.split('.')\[-1\] == 'listings':  
                print('process listings')  
                split\_cols = F.split(df\['name'\], '·')

is\_review\_present = F.trim(split\_cols.getItem(1)).startswith('★')

df = df.withColumn('description', F.trim(split\_cols.getItem(0))) \\  
                        .withColumn('reviews', F.when(is\_review\_present, F.trim(F.regexp\_replace(split\_cols.getItem(1), '★', ''))).otherwise(None)) \\  
                        .withColumn('bedrooms', F.when(is\_review\_present, F.trim(split\_cols.getItem(2))).otherwise(F.trim(split\_cols.getItem(1)))) \\  
                        .withColumn('beds', F.when(is\_review\_present, F.trim(split\_cols.getItem(3))).otherwise(F.trim(split\_cols.getItem(2)))) \\  
                        .withColumn('baths', F.when(is\_review\_present, F.trim(split\_cols.getItem(4))).otherwise(F.trim(split\_cols.getItem(3))))

df = df.drop('name', 'neighbourhood\_group', 'license')

df.writeTo(table\_name) \\  
                .createOrReplace()

return "Iceberg tables created successfully"

@test  
def test\_output(output, \*args) -\> None:  
    """  
    Template code for testing the output of the block.  
    """  
    assert output is not None, 'The output is undefined'

You can execute the script from the UI or, in more complex scenarios, set up triggers to run it on a regular basis. It might take a couple of minutes to run, and you may see several warnings the first time, likely due to the Mage standalone cluster.

![Image 14](https://miro.medium.com/v2/resize:fit:700/1*9bpjDJYWq1EbxExCk7ikaA.png)

Spark block run successfully

Once the block is completed, you can check if your data has been inserted into MinIO. You should see that our bucket is in place and contains all the data along with the metadata.

![Image 15](https://miro.medium.com/v2/resize:fit:700/1*epaazlLYY527nNVyPnwezw.png)

Minio UI shows the buckets

![Image 16](https://miro.medium.com/v2/resize:fit:700/1*baXd33d0_EA7L2K8PxNkog.png)

Iceberg bucket content

With Mage, you can create more complex pipelines with multiple intermediate steps.

If you want to read the data in Mage using a Python script, you can create another custom or transformation block and add the following code:

from mage\_demo.utils.spark\_session\_factory import get\_spark\_session  
import osMINIO\_ACCESS\_KEY = os.environ.get('MINIO\_ACCESS\_KEY')  
MINIO\_SECRET\_KEY = os.environ.get('MINIO\_SECRET\_KEY')  
  
iceberg\_spark\_session = get\_spark\_session(  
    "iceberg",  
    app\_name="MageSparkSession",  
    warehouse\_path="s3a://iceberg-demo-bucket/warehouse",  
    s3\_endpoint="http://minio:9000",  
    s3\_access\_key=MINIO\_ACCESS\_KEY,  
    s3\_secret\_key=MINIO\_SECRET\_KEY  
)

@custom  
def iceberg\_table\_read(\*args, \*\*kwargs):  
    """  
    Read data from a MinIO bucket using either Iceberg .  
    """  
      
    table\_name = "local.iceberg\_demo.listings"

df = iceberg\_spark\_session.spark.table(table\_name)

return df

@test  
def test\_output(output, \*args) -\> None:  
    """  
    Template code for testing the output of the block.  
    """  
    assert output is not None, 'The output is undefined'

If the script runs successfully, you should see the DataFrame displayed.

![Image 17](https://miro.medium.com/v2/resize:fit:700/1*3BCypuy3MF8xn5B5rjdZmA.png)

However, it might be more flexible to query the data using SQL in a SQL engine. StarRocks, apart from being a robust and fast data warehouse, can be used for this purpose as well.

To query the data using SQL in StarRocks, we will need to follow these steps:

1.  **Create a Catalog**: This is the first step to set up our environment for querying the data.

CREATE EXTERNAL CATALOG iceberg\_catalog  
PROPERTIES (  
    "type"\="iceberg",  
    "iceberg.catalog.type"\="hadoop",  
    "iceberg.catalog.warehouse"\="s3a://iceberg-demo-bucket/warehouse",  
    "aws.s3.endpoint"\="http://minio:9000",  
    "aws.s3.access\_key"\="your access key",  
    "aws.s3.secret\_key"\="your secret key",  
    "aws.s3.enable\_ssl" \= "false",  
 "aws.s3.enable\_path\_style\_access" \= "true"  
);

Then, we can validate that the catalog was created by typing:

SHOW CATALOGS;

![Image 18](https://miro.medium.com/v2/resize:fit:700/1*OIOQeZheBeQ_kXwDl_EK1g.png)

2\. **Set the Iceberg Catalog**: To specify the Iceberg catalog in the current session, type:

SET CATALOG iceberg\_catalog;

Then we can check the databases within the catalog by typing

SHOW DATABASES FROM iceberg\_catalog;

![Image 19](https://miro.medium.com/v2/resize:fit:384/1*B5e7QKpkHtSPEh0VVNTjfA.png)

`iceberg_demo` is the database we want, and it matches the picture from MinIO above.

3\. Then use [USE](https://docs.starrocks.io/docs/sql-reference/sql-statements/data-definition/USE/) to specify an active database,`iceberg_demo` in our case:

USE iceberg\_demo;

Now, we can see the tables, which will be the same as those in MinIO, by typing:

SHOW tables;

![Image 20](https://miro.medium.com/v2/resize:fit:550/1*Yt_A67Bnrqd16Qs3jC1NmA.png)

We see that our tables are in place, and now we can start exploring the data with more flexibility than in a Python script.

For example, we can perform a dummy check to see which neighborhood has the highest number of 5-star reviews:

SELECT   
  neighbourhood,   
  count(\*) as no\_reviews  
FROM listings   
WHERE reviews \='5.0'  
GROUP BY 1  
ORDER BY COUNT(\*) DESC

![Image 21](https://miro.medium.com/v2/resize:fit:696/1*vrzcD3dyKyYgay4ugZyRsg.png)

Query result from Iceberg tables in StarRocks

Congratulations! You have successfully built a local data lake using all the main components necessary for a data engineering project. If you want to explore more about Delta Lake, the process is similar with some differences in transformations, which you can find detailed in the [repository](https://github.com/georgezefko/mage_projects/tree/feat/sparkDataLake). For StarRocks integrations, it is slightly more complex than Iceberg, but you can find more information in the official documentation [here](https://docs.starrocks.io/docs/data_source/catalog/deltalake_catalog/).

**Conclusion**
--------------

Building a data engineering project requires many services to work together before starting to build the actual pipelines to convey data across the ecosystem. Configuring, setting up, and understanding these services is crucial for establishing a healthy system.

In this project, we have set up all the necessary services to build a local data lake, including a data pipeline orchestrator tool and a SQL engine. We initiated a Spark session for Apache Iceberg and Delta formats and performed a simple ETL process. Although simple, having this foundation set is a crucial step before creating more complex pipelines.

Of course, there are many ways to set up a project, but I hope you found this post helpful. I am always open to feedback and suggestions for improvements.

Happy learning!
