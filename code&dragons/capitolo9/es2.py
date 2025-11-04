def read_safe(text: str | None, default: str = '') -> str:
    if text == None:
        return default
    return text
  
