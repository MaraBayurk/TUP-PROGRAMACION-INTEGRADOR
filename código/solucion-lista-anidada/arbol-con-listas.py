arbol_razas = [
    "¿Sos alto?",
    [
        ["Si", [
            "¿Te apasionan los fuegos artificiales?",
            [
                ["Si", "Magos"],
                ["No", "Elfos"]
            ]
        ]],
        ["No", [
            "¿Te gusta el oro?",
            [
                ["Si", "Enanos"],
                ["No", "Hobbits"]
            ]
        ]]
    ]
]

def jugar_razas(nodo):
    while True:
        pregunta, opciones = nodo
        respuesta = input(pregunta + " Responde con si o con no: ").strip().capitalize()
        for opcion, hoja in opciones:
            if respuesta == opcion:
                if type(hoja) == str:  # validación directa del tipo
                    return hoja
                else:
                    nodo = hoja      # continuar recorriendo el árbol
                    break
        else:
            print("Respuesta no válida. Usa 'Si' o 'No'.")

#strip: quita espacios al inicio y al final de la cadena
#capitalize: pone la primera letra en mayúscula y el resto en minúscula
#lower: convierte toda la cadena a minúsculas

# Retorna la longitud de un nodo específico en el árbol.
def longitud_camino(nodo, destino, nivel=0):
    if type(nodo) == str:
        return nivel if nodo == destino else -1
    pregunta, opciones = nodo
    for opcion, hoja in opciones:
        res = longitud_camino(hoja, destino, nivel + 1)
        if res != -1:
            return res
    return -1

#Retorna la profundidad máxima del árbol.
def altura_max(nodo):
    if type(nodo) == str:
        return 1
    _, opciones = nodo
    alt = 0
    for opcion, hoja in opciones:
        sub_alt = altura_max(hoja)
        if sub_alt > alt:
            alt = sub_alt
    return alt + 1

# Imprime el árbol de decisiones de forma estructurada
def imprimir_arbol(nodo, nivel=0):
    if type(nodo) == str:
        print('  ' * nivel + '- ' + nodo)
    else:
        pregunta, opciones = nodo
        print('  ' * nivel + pregunta)
        for opcion, subnodo in opciones:
            print('  ' * (nivel + 1) + f'[{opcion}]')
            imprimir_arbol(subnodo, nivel + 2)

def arteAscii(raza):
    if raza == "Magos":
        return("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⡴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢈⣿⣇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⡏⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⡇⠀⠀⠉⠉⠙⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣇⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣦⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⠸⠿⠛⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⡄⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⣤⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣤⣀⠀⠀⠀
        """)
    elif raza == "Elfos":
        return("""
                              ___
                            ,' _ `.
                            \\,' )  )
                              ,'  /
                            ,;  ,'`-.
                          //  /     `-.
                         //  /         `-.
                        //  /             `.               ______
                       //  /                `.           ,'.  . .`.
                      //  /                   `.        /,`.`-.`.`.`.
                     //  /                      `.      ).,-  '.\\')\\\\:
                    ::  :                         `.   (a /a)  :';)`)|
                    ;;  ;                           `.  )'     |'|\\/|
                   ::  :                               /_,     |'|\\ ||
                   ;;  ;                                )__    |'|/`.|
                  ::  :                                  \\_    :'|,'||
                  ||  |                                    `-.' :|  \\|
  _.._-_-,______  ||  |______________________________,',',-,(\\ /||_,'`.
  `-...__.----,.  ||__|_----------------'''''''''''''`..-.(,'))\\||,'
              >-''  _ `._  ____ ____________________..`'`-`/_-||  `.
             /.`--'' `   `' `.. `.`.     `.    `.    `.      `||.
             (_`_...-'   `    : . \\ \\   .  \\     )     `.     |'  \\
              \\_`__..'.   ____;  . : :   )         |\\    \\   /  :  \\
                :--...-'''`._/_.___; ;        )    ; )   /      |   |
                |  ||         \\   / /      _,'    /    __....---|
                :  ::          `-'-'-...--'...--''`-';'/        |
                 :  ::                             ,'  :        :
                 :  ::                           ,'    |\\       |\\
                  :  ::                        ,'      | \\    | ; `.
                  :  ::                      ,'        :  \\   ; \\   `
                   \\  \\\\                   ,'          (   `-'  (
                    \\  \\\\                ,'            /       /|`
                     \\  \\\\            ,-'              : `.__,' |  )
                      \\  \\\\        ,-'                 |        (
                       \\  \\\\    ,-'                    ;        |\\
                        \\  \\\\,-'                       \\        ( \\
                         `. `:.                        ;\\   _,  /  \\
                           `. \\\\                       | \\      \\   \\
                         /`._) ))                      |  `     : ,  `
                         `.___,'                       |   _,'  |  SSt
        """)
    elif raza == "Enanos":
        return("""
                              ___A___
                             /   |   \\
                            / __ | __ \\
                            |/ o\\_/o \\|
                            (.--(_)--.)
                        .===/.-'\\_/`-.\\===.
                      .'\\  /           \\ / `.
                    /___ |_\\           /_|___\\_
                   <____>'\\ `.       ,' /`<____>
                   /   /   >==`-._.-'==<  /   /
                 _/==='   /  ,---:---.  \\/==,'
                / _ /     |__/v^v^v^v^v\\__)  \\
                \\)|)      |V^V^V^V^V^V^V|\\__/
                 ||        \\`-----|-----'/
                 ||         \\--.__|__,--/
                 ||          |____|____|
                 ||         <_____X_____>
              /A || A\\       \\....|..../
             // \\||/ \\\\       \\   |   /
            ((   []   ))      / v | v \\
             \\\\ /  \\ //      /   ,^    \\
              \\V    V/       `--'   `--'  
        """)
    elif raza == "Hobbits":
        return("""
⠀⠀⠀   ⠀⠀⠀⣰⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⠀⠀⠀⢿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⣿⡆⠀⠀⠈⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀  ⠹⣿⡀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀    ⠈⢿⡟⠛⢻⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀   ⠀⢸⣇⠀⠈⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀      ⠀⣿⡀⠀⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀       ⠸⣧⠀⢻⣿⣿⣿⣿⣿⡙⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⢻⡆⢸⣿⣿⣿⠿⠿⢿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀          ⢿⡀⠹⣿⡇⠀⠀⠈⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣟⣋⣤⣀⣼⣷⣤⣿⣿⣤⣤⣄⣼⣿⣧⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡄⠀⠀⠀
        """
        )

if __name__ == "__main__":
    raza = jugar_razas(arbol_razas)
    print(f"\n🎉 Perteneces a la raza de los: {raza}")
    print(arteAscii(raza))
    

    camino = longitud_camino(arbol_razas, raza)
    alt = altura_max(arbol_razas)
    print(f"\nLongitud del camino hasta '{raza}': {camino}")
    print(f"Altura máxima del árbol: {alt}")

    imprimir_arbol(arbol_razas)
