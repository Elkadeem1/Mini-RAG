from pydantic import BaseModel, Field
from typing import Optional

class proccesRequest(BaseModel):
   field_id : str
   chunk_size: Optional[int] = 100
   overlap_size: Optional[int] = 20
   do_reset: Optional[int] = 0