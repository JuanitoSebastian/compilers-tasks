from dataclasses import dataclass
from typing import Union,Literal

@dataclass
class Location:
  line: int | None
  column: int | None
  file: str | None

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Location):
      return False
    if (self.line is None and self.column is None and self.file is None) or (other.line is None and other.column is None and other.file is None):
      return True
    return self.line == other.line and self.column == other.column and self.file == other.file

L = Location(None, None, None)

TokenType = Literal['integer', 'operator', 'punctuation', 'identifier']

@dataclass
class Token:
  type: TokenType
  value: str
  location: Location
