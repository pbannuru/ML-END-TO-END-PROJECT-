1. __init__.py = where ever you find this it means library is available for import

2. setup.py gives all installments such as housing library and requirements.txt with the help of setup() function
    1. find_packages() : this function returns names of the modules of libraries with __init__.py
    2. we removed -e . in get_reuirement_list() as because find_packages is also installing libraries.

3. -e . = -e search all packages(i.e. __init__.py) to install . gives current directory

4. housing : __init__.py --- library
        1. exception handling -- package = __init__.py
           --> to track all the errors, to handle unexpected things.
           ---> error details:sys --sys module-- shows from ehich module is having error and in which line.
                error message : Exception  -- creates object of exception error shows what is the message
                 super().__init__(error_message) == The Super () method refers to the parent class in the child class. It provides a 
                 temporary object for the parent class. This temporary object can be used for accessing the parent class method.

        2. logger ---package = __init__.py
            --> shows what is happening in the project.
            -->given folder/dir name = "housing_logs" 
               logging file name = current time stamp
               import os---os.makedirs = creates folder ---os.path.join(foldername,filename) this creates a path of logging file.
               def __str__(self):  = print("object" of class)
               def __repr__(self): = when called object gives this func info
        3. pipeline ---package = __init__.py
            --> realworld dataset, pickle of data after FEngg, pickle of model selection, prediction
        4. component(stages) --- package = __init__.py
            --> component means stages in pipeline
                 --> data ingestion: bringing data into system from multiple sources
                 generate hash value and use it to find data set changes.

                 --> data validation:1.schema validation: file name, data type, no.of columns, name of columns
                                     2.null check
                                     3.duplicate data
                                     4. imbalance data
                                     5. domain value : in case of gender column : male, female should be there other than this any 
                                       other entry is present it is not domain value
                                     6. data range
                                     7. anamaly checking
                                     8. Data drift : if the stats of the data change ine data recievd this is called data drift
                --> data transformation: perform EDA, Feature Engineering, create pickle object for feature engg,
                --> model training: model selection, model training, pickle object of model training
                --> model evaluation: use test data for model evaluation

        5. config --- package =  __init__.py
            --> this is done based on entity
            --> for every component need some  
            --> config reads structure, all files in entity and provides configuration to pipeline when required.
        6. entity --- package =  __init__.py
            --> this a kind of table in database 
            --> ex:- for a student management system : database diagram
                entity : student, classroom, subject, teacher, dept, exam etc we create classes for those entities.
            -->ML project : enity : 
            --> in entity we define, artifact of each and evry component of pipeline such as data ingestion artifact,data validation artifact etc, data ingestion config, data validation config etc this entity specifies structure of all these
5. timestamp, hash value can be used to create data versions
6. Artifact : any output generated while running cicd pipeline such as graph,file,folders,report,model etc
7. tuple having name called named tuple looks like dictionary diff is that it cannot be modified as it is immutable.
    --> we have used in entity and given varaible name same as nametuple 
        ex: DataIngestionConfig = nametuple("DataIngestionConfig",["dataset_download_URL","download folder name","raw data file"])  
        this is the format, raw data file = downloaded file will be zip file we need extract and store the data i.e. raw data file

8.starting with configuration.py file:
we have given init constructor where self.config_info reads yaml file, self.time_stamp gives current time, self.training pipeline returns the function get_training_pipeline_config

1.def get_training_pipeline_config(self): 
here 
training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]  = basically config.info reads yaml file , TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config" this is created in constant file __ini__.py file 
it means we are taking self.config.info[training_pipeline_config] his gives value = yaml file value i.e  [pipeline_name: housing ,artifact_dir: artifact]
finally we used nametuple from config entity given value for artifact dir of name tuple i.e. training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)

2.def get_data_ingestion_config(self) ->DataIngestionConfig:
here we have artifact dir same as training pipeline as artifact main folder same for all and then
created specific dataingestion folder with the help of constant.init.py , artifact dir and timestamp,
and reading config.yaml file with self.config.info and using constant .init.py file given all key values.

9. started component file :
it gives artifact as an ouput
component is where all main activities taken place .
    1. data_ingestion.py:

    after developing data_ingestion_config using that in component-data_ingestion.py we develop data_ingestion_artifact as an ouput

    we do code for download_housing _data function using self.data_ingestion_config
    housing_file_name = basename of the file we are downloading
    use tgz dir, tgz file path
    url;ib.request.urlretrieve (url,filepath) this downloads the file
    using tar lib extract zipped downloaded file
 
9'. started entity.artifact_entity.py:
here all outputs of artifacts is declared through nametuple

10. pipeline : start_data_ingestion function is created where we connect all i/p, o/p and run the data ingestion .

11. do EDA
12. create schema.yaml in config folder : scheme is info of data
13. follow same steps for data validation as data ingestion.

14. started data validation:
from config.yaml file taken data validation keys and assigned to constant-__init__.py file
then created nametuple in config.entity.py the result is obtained from configuration.py file. and in name tuple given report file and its path that is html visualisation page.
creating func in component-data validation- for checking wether there is a file train/test available.
using evidently library to check data drift (which means wether our data statistics has changed that wil be checked)

15. in util.py  we have all functions such as rea_yaml_file () this is used in self.config.info whic reads config.yaml file