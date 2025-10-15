
import sys
import re

variables = {}
functions = {}

def parse_value(val_str):
    val_str = val_str.strip()
    if val_str.startswith('$'):
        var_name = val_str[1:].strip()
        return variables.get(var_name, {"error": f"Variável '${var_name}' não foi definida."})
    if val_str.startswith('"') and val_str.endswith('"'):
        return val_str[1:-1]
    try: return int(val_str)
    except ValueError: pass
    try: return float(val_str)
    except ValueError: pass
    if val_str in variables:
        return variables[val_str]
    return {"error": f"Valor ou nome de variável inválido: {val_str}"}

def execute_code_block(code_block):
    commands = [cmd.strip() for cmd in code_block.split(';') if cmd.strip()]
    for command in commands:
        execute_line(command + ';')

def execute_line(line):
    cleaned_line = line.split('!', 1)[0].strip()
    if not cleaned_line:
        return

    try:
        if cleaned_line.startswith('f ') and '(' in cleaned_line:
            match = re.match(r"f\s+(\w+)\s*\((.*)\);", cleaned_line)
            if match:
                func_name, func_body = match.groups()
                functions[func_name] = func_body
            else:
                print(f"Erro de Sintaxe: Definição de função inválida.")
            return

        if cleaned_line.startswith('f '):
            func_name = cleaned_line[2:].rstrip(';').strip()
            if func_name in functions: execute_code_block(functions[func_name])
            else: print(f"Erro: Função '{func_name}' não foi definida.")
            return

        if cleaned_line.startswith('if '):
            try:
                start_body_index = cleaned_line.index('(')
                cond_str = cleaned_line[3:start_body_index].strip()
                end_body_index = cleaned_line.rindex(')')
                body_code = cleaned_line[start_body_index + 1:end_body_index].strip()

                left_str, right_str = [s.strip() for s in cond_str.split('=', 1)]
                left_val, right_val = parse_value(left_str), parse_value(right_str)
                if isinstance(left_val, dict): print(left_val.get('error')); return
                if isinstance(right_val, dict): print(right_val.get('error')); return

                if left_val == right_val:
                    execute_code_block(body_code)
            except ValueError:
                print(f"Erro de Sintaxe: 'if' com parênteses desbalanceados.")
            return

        if cleaned_line.startswith('calc '):
            body, dest_var = [s.strip() for s in cleaned_line[5:].rstrip(';').split('->', 1)]
            op_char = next((op for op in ['+', '-', '*', '/'] if op in body), None)
            if not op_char: print(f"Erro: Expressão inválida para 'calc'."); return
            left_str, right_str = [s.strip() for s in body.split(op_char, 1)]
            left_val, right_val = parse_value(left_str), parse_value(right_str)
            if isinstance(left_val, dict): print(left_val.get('error')); return
            if isinstance(right_val, dict): print(right_val.get('error')); return
            if not isinstance(left_val, (int, float)) or not isinstance(right_val, (int, float)):
                print(f"Erro: Operações matemáticas só com números."); return
            if op_char == '+': result = left_val + right_val
            elif op_char == '-': result = left_val - right_val
            elif op_char == '*': result = left_val * right_val
            elif op_char == '/':
                if right_val == 0: print("Erro: Divisão por zero."); return
                result = left_val / right_val
            variables[dest_var] = result
            return

        if cleaned_line.startswith('var '):
            body = cleaned_line[4:].rstrip(';').strip()
            var_name, right_side = body.split('=', 1)
            value = parse_value(right_side.strip())
            if isinstance(value, dict): print(value.get('error')); return
            variables[var_name.strip()] = value
            return

        if cleaned_line.startswith('say '):
            arg_str = cleaned_line[4:].strip()
            if arg_str.endswith(';'):
                arg_str = arg_str[:-1].strip()
            value = parse_value(arg_str)
            if isinstance(value, dict): print(value.get('error')); return
            print(value)
            return

        print(f"Erro de Sintaxe: Comando não reconhecido: '{cleaned_line}'")

    except Exception as e:
        print(f"Erro Crítico ao processar a linha '{cleaned_line}'. Detalhes: {e}")

def run_interpreter(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                execute_line(line)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_interpreter(sys.argv[1])
    else:
        print("Uso: python3 ojl_interpreter.py <arquivo.ojl>")
