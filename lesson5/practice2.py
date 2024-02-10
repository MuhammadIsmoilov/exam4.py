letter = input()
def english_letters(letter):
   cnt = letter.lower() 
   uniq = ''
   for i in cnt: 
      if i not in uniq:
         uniq +=i

   if len(cnt) == 26:
      print('YES')
   else:
      print('NO')
english_letters(letter)           