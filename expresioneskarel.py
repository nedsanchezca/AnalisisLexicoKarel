import ply.lex as lex

expresiones = ["Arrancar_programa", "Terminar_programa", "Empezar_ejecucion", "Acabar_ejecucion", "Apagar", "Dirijase", "Rotar_izquierda", "Recolectar_zumbidito", "Abandonar_zumbidito", "Coma_Y_Punto"]

t_ignore = r'\t | \n'
t_Arrancar_programa = r'iniciar-programa'
t_Terminar_programa = r'finalizar-programa'
t_Empezar_ejecucion = r'inicia-ejecucion'
t_Acabar_ejecucion  = r'termina-ejecucion'
t_Apagar = r'apagate'
t_Dirijase = r'avanza'
t_Rotar_izquierda = r'gira-izquierda'
t_Recolectar_zumbidito = r'coge-zumbador'
t_Abandonar_zumbidito  = r'deja-zumbador'
t_Coma_Y_Punto = r'\;'

def error(t):
    print("Expresión inválida '%s'" % t.value[0])
    t.lexer.skip(1)

def abrir_archivo(nombre):
    archivo = open(nombre, r)
    return archivo.read()

lex.lex()

lex.input(abrir_archivo("archivo.txt"))
while True:
    tok = lex.token()
    if not tok: break
    print(str(tok.value) + " - " + str(tok.type))
