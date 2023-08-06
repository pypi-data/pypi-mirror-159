import time
from typing import List, Union
from zaiclient.request.BaseEvent import BaseEvent
from zaiclient.exceptions.InputTypeNotEqualException import InputTypeNotEqualException
from zaiclient.exceptions.InputLengthNotEqualException import InputLengthNotEqualException

class RateEvent(BaseEvent):
    
    __default_event_type = "rate"
    
    def __init__(self, user_id: str, item_ids: Union[str, List[str]], ratings: Union[float, List[float], int, List[int]], timestamp: float = time.time()):
        
        if not isinstance(user_id, str):
            raise TypeError("User ID must be a string value.")
        
        if not ((type(item_ids) == str and (type(ratings) == float or type(ratings) == int)) 
                 or (isinstance(item_ids, List) and isinstance(ratings, List))):
            raise InputTypeNotEqualException
        
        if isinstance(item_ids, List) and isinstance(ratings, List):
            if not (all(isinstance(item_id, str) for item_id in item_ids) and all(isinstance(rating, (int, float)) for rating in ratings)):
                raise TypeError("The ids and values in list do not have the same type.")
        
        _item_ids = [item_ids] if type(item_ids) == str else item_ids
        _event_values = [ratings] if isinstance(ratings, (float, int)) else ratings
        
        if len(_item_ids) != len(_event_values):
            raise InputLengthNotEqualException
        
        super().__init__(user_id, _item_ids, timestamp, self.__default_event_type, _event_values)