# treasure island game
print(
    """
    Welcome to the treasure island!
    Your mission is to find the treasure.    
    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..:: .lcf/
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~
   """)

while True:
    user_action = input("Welcome to treasure island!\nAre you going left or right(Left/Right)")

    if user_action == 'Left':
        user_action = input("""
                  _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                      
 ___.'       '.       /               '-._         
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-'
You find a river\n do you swing or wait?(Swing/Wait) """)
    elif user_action != 'Left':
        print("Fall into a hole\n GAME OVER.")
        break

    if user_action == "Wait":
        user_action = input("""
              ________
             / ______ \
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\    /   \/
    ________|__________|__ (\|||/) _________
   hjw     /____________\
   `97     |____________|
   The sun guided you to a two door path\nWhich door?(Blue/Red/Yellow) """)

    elif user_action == "Swing":
        print("""
        Eaten by croc.
        

                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                      (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
        """)

        break

    if user_action == "Yellow":
        print("""
            Congratulations!!
            _______________
            |@@@@|     |####|
            |@@@@|     |####|
            |@@@@|     |####|
            \@@@@|     |####/
             \@@@|     |###/
              `@@|_____|##'
                   (O)
                .-'''''-.
              .'  * * *  `.
             :  *       *  :
            : ~ A S C I I ~ :
            : ~ A W A R D ~ :
             :  *       *  :
              `.  * * *  .'
                `-.....-'
        """)
        break

    elif user_action == "Red":
        print("""
   Eaten by a Beast. Game Over.
          ( )___( )
          /__oo   \
         ( \/     )
         | `=/    |
        /         \
       /  /    \   \
      /  (      \   \ 
     ( ,_/_      \   \
      \_ '=       \   )
        ""'       /  /
        ;        /  /'?
        :       (((( /
         `._   \  _ (
          __|   |  /_    
        ("__,.."'_._.)   
        
        """)
        break
    elif user_action == "Blue":
        print(
            """
    Burned by fire. Game over
    
    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..jb
            """
        )
        break
    else:
        print("You dumb. Game over")
        break







