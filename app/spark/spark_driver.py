import pyspark.sql
from google.cloud import storage
from pyspark.sql import SparkSession


def getSparkSession(spark_app_name=None):
   return SparkSession.builder \
        .appName(spark_app_name) \
        .getOrCreate()


def getGCPStorageBlobs(bucket=None):
    gcs_storage = storage.Client()
    try:
       blobs = list(gcs_storage.bucket(bucket).list_blobs())
       return blobs
    except Exception as e:
        print(e)


def parseGCPStorageBlobs(blobs:list):
    blob_attributes = [blob.__dict__.get("_properties") for blob in blobs]
    parsed_blobs = [blob.get("id") for blob in blob_attributes]
    return parsed_blobs



def createSparkSession():
    spark = SparkSession.builder \
        .appName('Alexander-Spark-App-Test') \
        .getOrCreate()
    return spark

def createDataFrame(sparkSession):
    return sparkSession \
        .read \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .csv("https://storage.googleapis.com/neo4j-graphconnect-amey-alexander/gossipcop_fake.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=alexanderbqserviceaccount%40neo4j-se-team-201905.iam.gserviceaccount.com%2F20220525%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220525T203908Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=24ba9e07daafef8e30895e19a23102eb71148cb006f92d2915f323dfe791783d7bd66c45a1353841e39d9c736fe403ad2fd20c95e4b043875385284847a75cf67b96e05c942b8bed8409fb4acf64103d0cdc80addb594a87f9db3d54bd4cc5bc9efb58248a5d511b23e56ce81279ab49b387722d1e1266b902d1650cd8a2cde2cb8d4198ef3792339298f870c202a98db443c20c830e267ae00cd618ebf83bde7123adc33ea14f4b69e8b29544c73e6c219ba379084d8c8c4e7fbcde5145f20a4218284803c0e2ec22ba159103efb4dee1844283f961e0f0ac08ed2f2289363a4f575ee52d2eb05b7320f0c4db9dc5e69127ec1d46d94acebd1694d232f55959")





if __name__ == "__main__":



    # First Blob, since there are multiple files
    raw_blobs = getGCPStorageBlobs("neo4j-graphconnect-amey-alexander")
    cloud_object = parseGCPStorageBlobs(raw_blobs)[0]
    spark_session = createSparkSession()
    df = createDataFrame(spark_session)
























