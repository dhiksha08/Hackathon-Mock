def split_sequence(arr, k):
  """
  Divides a sequence into sub-sequences with sum less than or equal to k.

  Args:
    arr: A list of integers representing the sequence.
    k: The maximum allowed sum for each sub-sequence.

  Returns:
    A list of lists, where each sub-list represents a sub-sequence.
  """
  subsequences = []
  current_sum = 0
  current_subsequence = []
  for element in arr:
    if current_sum + element <= k:
      current_sum += element
      current_subsequence.append(element)
    else:
      if current_subsequence:
        subsequences.append(current_subsequence)
      current_sum = element
      current_subsequence = [element]
  if current_subsequence:
    subsequences.append(current_subsequence)
  return subsequences

# Example usage
arr = [70, 70, 90, 50, 70, 90, 110, 70, 110, 70, 70, 110, 110, 90, 50, 90, 110, 90, 70, 110]
k = 600

subsequences = split_sequence(arr, k)
print(f"Subsequences: {subsequences}")
