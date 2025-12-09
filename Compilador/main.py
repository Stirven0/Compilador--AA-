import argparse
import sys
from core.lexer import Lexer

class Compiler:
    def __init__(self, debug_mode: bool = False, backend: str = 'bytecode'):
        self.debug = debug_mode
        self.backend = backend

    def compile(self, source: str, filename: str = "<stdin>") -> bool:
        """Compila el código fuente a código objeto. Retorna True si la compilación fue exitosa."""
        try:
            # 1. Lexer
            lexer = Lexer(source)

        except Exception as e:
            print(f"❌ Error Critico: {e}")
            if self.debug:
                import traceback
                traceback.print_exc()
            return False


def main():
    """Punto de entrada principal del compilador."""
    arg_parser=argparse.ArgumentParser(
        description="Compilador de codigo fuente a codigo objeto",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Ejemplos:
            python main.py -f ejemplo.py                    # Compilar y ejecutar
            python main.py -f ejemplo.py -p -s              # Mostrar AST y tabla de símbolos
            python main.py -f ejemplo.py --backend c        # Generar código C
            python repl.py                                  # Iniciar REPL interactivo
        """
    )
    arg_parser.add_argument('-f', '--file', type=str, help='archivo fuente a compilar')
    arg_parser.add_argument('-d', '--debug', action='store_true', help='activar modo debug')
    arg_parser.add_argument('-b', '--backend', type=str, choices=['bytecode', 'c'], default='bytecode', help='backend de generación de código')
    arg_parser.add_argument('-p', '--show-ast', action='store_true', help='mostrar AST generado')
    arg_parser.add_argument('-s', '--show-symbols', action='store_true', help='mostrar tabla de símbolos')

    args=arg_parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r') as f:
                source = f.read()
        except FileNotFoundError:
            print(f"❌ archivo no encontrado: {args.file}")
            sys.exit(1)

        compiler = Compiler(debug_mode=args.debug, backend=args.backend)
        success = compiler.compile(source, args.file)

        sys.exit(0 if success else 1)
    else:
        print("ℹ️  ingresa un archivo fuente con la opción -f <archivo> o usa el REPL mediante  \n\npython repl.py")
        sys.exit(1)
if __name__ == "__main__":
    main()
