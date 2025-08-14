#!/user/bin/env python3
"""
suhail alaboud
"""
def index_range(page: int, page_size: int) -> tuble:
  start_index = page - 1) * page_size
  end_index = start_index + page_size
  return (start_index, end_index)
  
