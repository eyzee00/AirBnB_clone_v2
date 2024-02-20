#/usr/bin/python3
"""defines a database based storage engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
import os



class DBStorage:
    """defines a database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initiates a dbEngine"""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST", default="localhost")
        db = os.getenv("HBNB_MYSQL_DB")
        
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}:3306/{}"
            .format(user, passwd, host, db),
            pool_pre_ping=True
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """query on the current db session all objects of a class"""
        
        classes = filter(lambda c: cls is None or c.__name__ == cls,
                          Base.__subclasses__())
        objects = {}
        
        for class_obj in classes:
            class_name = class_obj.__name__
            query = self.__session.query(class_obj).all()
        
        for result in query:
            key = "{}.{}".format(class_name, result.id)
            objects[key] = result

        return objects
    
    def new(self, obj):
        """add an object to the curerent db session"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete form the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.city import City
        from models.state import State
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        ))
