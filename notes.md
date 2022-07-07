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