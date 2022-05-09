def second_from_begin(*args):
   tup_to_set = set(args)
   result = [itr for itr in tup_to_set]
   result.sort()
   return result[1]
