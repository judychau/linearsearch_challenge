def linear_search(items, n_items, key, ascending, match_type):
  """ This function finds the element in the array
      that best fits the search criteria. It returns
      the match type and the index of the matching item."""
  
  #check if n_items matches the length of the items array
  if n_items != len(items):
    return "n_items doesn't match"

  index = 0
  found = False
  stop = False

  while index < n_items and not found and not stop:
    #ascending
    if ascending == 1:
      #check if key matches an item
      if items[index] == key:
        found = True
        if match_type in ("LessThanEquals", "GreaterThanEquals", "Equals"):
          return "FoundExact", index
        elif match_type == "LessThan":
          if index <= 0:
            return "NotFound", "X"
          else:
            return "FoundLess", index - 1
        elif match_type == "GreaterThan":
          if items[n_items-1] == key:
            return "NotFound", "X"
          else:
            return "FoundGreater", index + 1
        else:
          return "Check match type"
      #no match, find the item greater than the key and stop
      elif items[index] > key:
        stop = True
        if match_type == "Equals":
          return "NotFound", "X"
        elif match_type in ("LessThan", "LessThanEquals"):
            if index <= 0:
              return "NotFound", "X"
            else:
              return "FoundLess", index - 1
        elif match_type in ("GreaterThan", "GreaterThanEquals"):
            return "FoundGreater", index
        else:
          return "Check match type"
      #no item is greater than the key
      elif items[n_items-1] < key:
        return "NotFound", "X"
      else:
        index = index + 1

    #descending
    elif ascending == 0:
      #check if the key matches an item
      if items[index] == key:
        found = True
        if match_type in ("LessThanEquals", "GreaterThanEquals", "Equals"):
          return "FoundExact", index
        elif match_type == "LessThan":
          if index == n_items-1:
            return "NotFound", "X"
          else:
            return "FoundLess", index + 1
        elif match_type == "GreaterThan":
          if index <= key:
            return "NotFound", "X"
          else:
            return "FoundGreater", index - 1
        else:
          return "Check match type"
      #no match, find the item less than the key and stop
      elif items[index] < key:
        stop = True
        if match_type == "Equals":
          return "NotFound", "X"
        elif match_type in ("LessThan", "LessThanEquals"):
            if index == n_items - 1:
              return "NotFound", "X"
            else:
              return "FoundLess", index
        elif match_type in ("GreaterThan", "GreaterThanEquals"):
            if index <= 0:
              return "NotFound", "X"
            else:
              return "FoundGreater", index - 1
        else:
          return "Check match type"
      #no item is less than the key
      elif items[n_items-1] > key:
        return "NotFound", "X"
      else:
        index = index + 1
    
    #ascending value is wrong  
    else:
      return "Check ascending value"

