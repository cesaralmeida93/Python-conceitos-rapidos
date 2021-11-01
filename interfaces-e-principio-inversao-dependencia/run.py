from src import use_case
from src.use_case import MyUsecase
from src.database import Database2

use_case = MyUsecase(Database2())

use_case.search_something()
use_case.insert_something()