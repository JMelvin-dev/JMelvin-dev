print(r'''                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure.")
print("You're at a cross road. where do you want to go?")
print(f'\tType "left" or "right"')
choose = input()
choose = choose.lower()
if choose == 'left':
  print("You've come to a lake. There is an island in the middle of the lake.")
  print(f'\tType "wait" to wait for a boat. Type "swim" to swim across.')
  ch = input()
  ch=ch.lower()
  if ch == 'wait':
    print("You arrive at the island unharmed. there is a house with 3 doors.")
    print(f"\tOne red, one yellow and one blue. Which colour do you choose?")
    color = input()
    color=color.lower()
    if color == 'yellow':
      print("YOU WON!")
    elif color == 'blue':
      print(r'''Crocodile ate you..
            THE |  |
    __ |  |   ___      ___    __       _  _
  ,'  ||  |  .   `.  ,'  ,'. |  |,'`.,' || `.
 :    ||  |:`.`.   ::  ,',' :|  .^..'`._|'--'
 :    ||  |:  `.`. ;:,','   ;|  |    .--.|``.
  `.__||__| `.__`.`   '___,' |__|    `._||_,' SSt

                     _____
                   ,'    .`-._
                  / .-'  <>  .\
                 / .  , '___..'-._
               .'/  `.`. _,'
               |.  `-.`./
              /`.` ` _. `.
             : .|  .' `  _`.
             ;  ;. .  .'`  _\
            /. /\:.  .  ,'`  \
       _-.,'_,'  \:. . .  ,-'':
       ``--'     ,'``-._.   ` |,-.
                 \ . `  ` --''|, .\ ,
                  \.`._` .  ` | . :/|_
               _.-.>. \:.  ,- :\/\.`./
              '`---'.,.'`.    .\  `-'
                    '     `.`   `._
                            `-._`. ``.
                                `-. ` `.
                                   `.  .\
                                     \   :
                                      )` ;
               ____                  / ./
             ``-.._ ```----....___.-'.,'
                   ```----...._____.-'  SSt



          Game Over.''')

    else:
      print(r'''    The room is in fire
            
               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             ..Game Over.''')
  elif ch=='swim':
    print(r'''You are Dead..!
                  \
          \ \  / /
  \ \      \ \/ /
   \ \     |   /
    \  \   |   |
     \  \  |   |
\\    \  \ |   ---------#-----
- ------  \|    --------#------
 --------       |       |
         \      |       |
          |     |       |
          |     |       |
          |     |       |
          |     |    _+m#m+_
          |     |   Jp     qh
          |     |   O       O
          |     |   Yb     dY
          |     |    "Y5m2Y"
          |     |
          |     |
         /   /\  \
          Game over''')
  else:
    print("You have choosen another..")
else:
  print(r'''You fell into a hole.
          ,
               }`-.   ,          ,
               \ \ '-' \      .-'{
               _} .  | ,`\   /  ' ;    .-;\
              {    \ |    | / `/  '-.,/ ; |
              { -- -.  '  '`-, .--._.' ;  \__
               \     \ | '  /  |`.    ;    _,`\
                '. '-     ' `_- '.`;  ; ,-`_.-'
            ,--.  \    `   /` '--'  `;.` (`  _
         .--.\  '._) '-. \ \ `-.    ;     `-';|
         '. -. '         __ '.  ;  ;     _,-' /
          { __'.\  ' '-,/; `-'   ';`.- `   .-'
           '-.  `-._'  | `;     ;`'   .-'`
             <_ -'   ` .\  `;  ;     (_.'`\
             _.;-"``"'-._'. `:;  ___, _.-' |
         .-'\'. '.` \ \_,_`\ ;##`   `';  _.'
        /_'._\ \  \__;#####./###.      \`
        \.' .'`/"`/ (#######)###::.. _.'
         '.' .'  ; , |:.  `|()##`"""`
       jgs `'-../__/_\::   /O()()o
                    ()'._.'`()()'


Game Over.''')