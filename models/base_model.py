from datetime import datetime
import models
import uuid


class BaseModel:
    """Base Model Class

    that defines all common attributes/methods for other classes
    initialization, serialization and deserialization
    of the future instances.
    
    """

    def __init__(self, *args, **kwargs):
        """
        Base Modele instance are initialized.

        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Return [<class name>] (<self.id>) <self.__dict__>
        Representation of the class for the user.
        """
        
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """Updates a Base Model instance

        Updates the public instance attribute `updated_at`
        with the current datetime and dumps the class data
        into a file

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This method will be the first piece of the
        
        serialization/deserialization process
        create a dictionary representation with 
        “simple object type” of our BaseModel
        
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
