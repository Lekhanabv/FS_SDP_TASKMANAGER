from pydantic import BaseModel,ConfigDict,Field
class TaskCreate(BaseModel):
    tittle: str = Field(min_length=1,max_length=200)
    
class TaskUpdate(BaseModel):
    completed: bool
class TaskResponse(BaseModel):
    id:int
    tittle:str
    completed:bool

    model_config = ConfigDict(from_attributes=True)
