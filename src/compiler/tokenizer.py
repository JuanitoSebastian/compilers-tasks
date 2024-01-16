import re

INTEGER_OR_VARIABLE_REGEX = r'([0-9]+)|([a-zA-Z_]+)'

def tokenize(source_code: str) -> list[str]:
  pos = 0
  tokens = []
  while pos < len(source_code):
    token, new_pos = check_for_match_at(source_code, pos)
    if token:
      tokens.append(token)
    pos = new_pos
  return tokens


def check_for_match_at(source_code: str, pos: int) -> tuple[str | None, int]:
  regex = re.compile(INTEGER_OR_VARIABLE_REGEX)
  match = regex.match(source_code, pos)
  if match:
    return match.group(0), match.end()
  else:
    return None, pos + 1