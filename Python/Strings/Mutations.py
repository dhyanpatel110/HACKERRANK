Task:
  Read a given string, change the character at a given index and then print the modified string.
  
Example:
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

CODE:
  def mutate_string(string, position, character):
    l = list(string)
    l[position] = character;
    string = ''.join(l);
    return string
  if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
    
    
    