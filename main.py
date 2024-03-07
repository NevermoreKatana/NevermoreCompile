from antlr4 import *
from antlr4_gen.grammar.nevermorecompilerLexer import nevermorecompilerLexer
from antlr4_gen.grammar.nevermorecompilerParser import nevermorecompilerParser
from antlr4_gen.grammar.nevermorecompilerVisitor import nevermorecompilerVisitor
from antlr4_gen.grammar.nevermorecompilerListener import nevermorecompilerListener
from llvmlite import ir, binding

import json

with open('input.txt', 'r') as file:
    input_text = file.read()

input_stream = InputStream(input_text)
lexer = nevermorecompilerLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = nevermorecompilerParser(stream)
tree = parser.prog()

# listener = nevermorecompilerListener()
# walker = ParseTreeWalker()
visitor = nevermorecompilerVisitor()
visitor.visit(tree)
# walker.walk(listener, tree)


class EvalVisitor(nevermorecompilerVisitor):
    def __init__(self):
        self.variables = {}
        self.tmp_variable = {}
        self.ast = []
    def visitStat(self, ctx: nevermorecompilerParser.StatContext):
        if ctx.ifStatement():
            return self.visitIfStatement(ctx.ifStatement())
        elif ctx.printState():
            return self.visitPrintState(ctx.printState())
        elif ctx.assignmentStatement():
            return self.visitAssignmentStatement(ctx.assignmentStatement())
        elif ctx.ifElseStatement():
            return self.visitIfElseStatement(ctx.ifElseStatement())
        elif ctx.forStatement():
            return self.visitForStatement(ctx.forStatement())
        elif ctx.whileStatement():
            return  self.visitWhileStatement(ctx.whileStatement())
        elif ctx.doWhileStatement():
            return self.visitDoWhileStatement(ctx.doWhileStatement())
        elif ctx.globalStatement():
            return self.visitGlobalStatement(ctx.globalStatement())
        elif ctx.functionStatement():
            return self.visitFunctionStatement(ctx.functionStatement())
        elif ctx.functionCall():
            return self.visitFunctionCall(ctx.functionCall())


    def visitProg(self, ctx: nevermorecompilerParser.ProgContext):               
        for child in ctx.functionStatement():
            ast_node = self.visit(child)
            if ast_node not in self.ast:
                self.ast.append(ast_node)
        if ctx.globalStatement() is not None:
            global_ast_node = self.visit(ctx.globalStatement())
            if global_ast_node not in self.ast:
                self.ast.append(global_ast_node)
        return json.dumps(self.ast)

    def visitExpr(self, ctx: nevermorecompilerParser.ExprContext):
        if ctx.ID():
            variable_name = ctx.ID().getText()
            if variable_name in self.variables:
                self.variables[variable_name]["value"]
                return {"type": "VAR", "value": variable_name}
            else:
                raise ValueError(f"Variable '{variable_name}' is not defined.")
        elif ctx.INT():
            return {"type": "INT", "value": int(ctx.INT().getText())}
        elif ctx.DOUBLE():
            return {"type": "DOUBLE", "value": float(ctx.DOUBLE().getText())}
        elif ctx.functionCall():
            function_call = self.visit(ctx.functionCall())
            return function_call
        elif ctx.DIV():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "DIV", "left": left_expr, "right":right_expr}
        elif ctx.MUL():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "MUL", "left": left_expr, "right":right_expr}
        elif ctx.ADD():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "ADD", "left": left_expr, "right": right_expr}
        elif ctx.SUB():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "SUB", "left": left_expr, "right":right_expr}
        elif ctx.GT():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "GT", "left": left_expr, "right": right_expr}
        elif ctx.LT():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "LT", "left": left_expr, "right": right_expr}
        elif ctx.EQ_EQ():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "EQ_EQ", "left": left_expr, "right": right_expr}
        elif ctx.NOT_EQ():
            left_expr = self.visit(ctx.expr(0))
            right_expr = self.visit(ctx.expr(1))
            return {"type": "NOT_EQ", "left": left_expr, "right": right_expr}
        
        return self.visitChildren(ctx)


    def visitFunctionCall(self, ctx: nevermorecompilerParser.FunctionCallContext):
        function_name = ctx.functionName().getText()
        function_type = ctx.funcType().getText()
        args_dict = []
        args_ctx = ctx.functionParams()
        if args_ctx:
            for i in range(args_ctx.getChildCount()):
                arg_ctx = args_ctx.getChild(i)
                if isinstance(arg_ctx, nevermorecompilerParser.FunctionExprContext):
                    args_dict.append(arg_ctx.getText())
        
        function_call = {
            "functionCall":{
                "name": function_name,
                "type": function_type,
                "params": args_dict
            }
        }
        return function_call
    
    
    def visitFunctionStatement(self, ctx:nevermorecompilerParser.FunctionStatementContext):
        func_name = ctx.functionName().getText()
        func_type = ctx.funcType().getText()
        return_ = ctx.ret()

        function_body = []
        
        args_dict = {}
        args_ctx = ctx.functionArgs()
        
        if args_ctx:
            for i in range(args_ctx.getChildCount()):
                arg_ctx = args_ctx.getChild(i)
                if isinstance(arg_ctx, nevermorecompilerParser.TypeContext):
                    type_name = arg_ctx.getText()
                    var_name = args_ctx.getChild(i + 1).getText()
                    self.variables[var_name] = {"type": type_name, "value": var_name}
                    args_dict[var_name] = type_name

        
        for stat_ctx in ctx.functionBody().stat():
            body_node = self.visit(stat_ctx)
            if body_node in self.ast:
                self.ast.remove(body_node)
            if body_node:
                function_body.append(body_node)
    
        function_body = {
                "functionStatement": {
                    "name": func_name,
                    "type": func_type,
                    "args": args_dict,
                    "return": return_.functionExpr().getText() if return_ else None,
                    "body": function_body,
                    "END_STATE": ";"
                }
        }
        for k, v in args_dict.items():
            del self.variables[k]
        print(self.variables)
        return function_body

    def visitPrintBody(self, ctx: nevermorecompilerParser.PrintBodyContext):
        if ctx.ID():
            return {"type": "ID", "value": ctx.ID().getText()}
        elif ctx.INT():
            return {"type": "INT", "value": int(ctx.INT().getText())}
        elif ctx.DOUBLE():
            return {"type": "DOUBLE", "value": float(ctx.DOUBLE().getText())}

    def visitPrintState(self, ctx: nevermorecompilerParser.PrintStateContext):
        expr_result = self.visit(ctx.printBody())

        print_node = {
            "stat": {
                "printStatement": {
                    "expr": expr_result,
                    "END_STATE": ";"
                }
            }
        }
        self.ast.append(print_node)
        return print_node

    def visitGlobalStatement(self, ctx: nevermorecompilerParser.GlobalStatementContext):
        variables = {}
        for globalBody in ctx.globalBody():
            variable_name = globalBody.ID().getText()
            type_ = globalBody.type_().getText()
            variables[variable_name] = type_
            self.variables[variable_name] = {"type": type_, "value": None}


        global_node = {
            "globalStatement": variables
        }

        self.ast.append(global_node)
        return global_node

    def visitIfElseStatement(self, ctx: nevermorecompilerParser.IfElseStatementContext):
        condition = self.visit(ctx.equation())
        if_body = []
        else_body = []

        for stat_ctx in ctx.ifBody().stat():
            body_node = self.visit(stat_ctx)
            if body_node in self.ast:
                self.ast.remove(body_node)
            if body_node:
                if_body.append(body_node)

        for stat_ctx in ctx.elseBody().stat():
            body_node = self.visit(stat_ctx)
            if body_node in self.ast:
                self.ast.remove(body_node)
            if body_node:
                else_body.append(body_node)

        if_else_node = {
            "ifElseStatement": {
                "condition": condition,
                "ifBody": if_body,
                "elseBody": else_body
            }
        }

        return if_else_node

    def visitIfStatement(self, ctx: nevermorecompilerParser.IfStatementContext):
        condition = self.visit(ctx.equation())
        body = []

        for stat_ctx in ctx.ifBody().stat():
            body_node = self.visit(stat_ctx)
            if body_node in self.ast:
                self.ast.remove(body_node)
            if body_node:
                body.append(body_node)
        if_node = {
            "ifStatement": {
                "condition": condition,
                "body": body
            }
        }

        return if_node

    def visitForStatement(self, ctx:nevermorecompilerParser.ForStatementContext):
        init = self.visit(ctx.forInit())
        condition = self.visit(ctx.equation())
        modify = self.visit(ctx.forModify())
        body = []
        for stat_ctx in ctx.forBody().stat():
            body_node = self.visit(stat_ctx)
            if body_node in self.ast:
                self.ast.remove(body_node)
            if body_node:
                body.append(body_node)

        for_node = {
            "forStatement": {
                "init": init,
                "condition": condition,
                "modify": modify,
                "body": body
            }
        }
        self.ast.append(for_node)
        return for_node

    def visitWhileStatement(self, ctx:nevermorecompilerParser.WhileStatementContext):
        condition = self.visit(ctx.equation())
        body = []

        for stat_ctx in ctx.whileBody().stat():
            body_node = self.visit(stat_ctx)
            if body_node in self.ast:
                self.ast.remove(body_node)
            if body_node:
                body.append(body_node)

        while_node = {
            "whileStatement": {
                # "ID":
                "condition": condition,
                "body": body
            }
        }
        self.ast.append(while_node)
        return while_node

    def visitDoWhileStatement(self, ctx:nevermorecompilerParser.WhileStatementContext):
        condition = self.visit(ctx.equation())
        body = []


        for stat_ctx in ctx.whileBody().stat():
            body_node = self.visit(stat_ctx)
            if body_node in self.ast:
                self.ast.remove(body_node)
            if body_node:
                body.append(body_node)

        while_node = {
            "doWhileStatement": {
                "body": body,
                "condition": condition
            }
        }
        self.ast.append(while_node)
        return while_node

    def visitForModify(self, ctx:nevermorecompilerParser.ForModifyContext):
        id_name = ctx.ID().getText()
        op = ctx.INCREMENT().getText()
        return {"ID": id_name, "op": op}

    def visitEquation(self, ctx: nevermorecompilerParser.EquationContext):
        left_expr = self.visit(ctx.expr(0))
        right_expr = self.visit(ctx.expr(1))
        op = ctx.relop().getText()
        try:
            left_ID = ctx.expr(0).ID().getText()
            right_ID = ctx.expr(1).ID().getText()
            return {"left": left_expr, "left_ID": left_ID, 'right_ID':right_ID, "op": op, "right": right_expr}
        except:
            return {"left": left_expr, "op": op, "right": right_expr}

    def visitForInit(self, ctx:nevermorecompilerParser.ForInitContext):

        type_ = ctx.type_().getText()
        variable_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        child_count = ctx.expr().getChildCount()
        self.variables[variable_name] = {"type": type_, "value": value, "child": child_count}

        assignment_node = {
            "stat": {
                "assignmentStatement": {
                    "type": type_,
                    "ID": variable_name,
                    "expr": [value] if child_count == 1 else self.flatten_expr(value),
                    "END_STATE": ";"
                }
            }
        }
    
        return assignment_node



    def visitAssignmentStatement(self, ctx: nevermorecompilerParser.AssignmentStatementContext):

        type_ = ctx.type_().getText()
        variable_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        child_count = ctx.expr().getChildCount()
        self.variables[variable_name] = {"type": type_, "value": value, "child": child_count}

        assignment_node = {
            "stat": {
                "assignmentStatement": {
                    "type": type_,
                    "ID": variable_name,
                    "expr": [value] if child_count == 1 else self.flatten_expr(value),
                    "END_STATE": ";"
                }
            }
        }

        self.ast.append(assignment_node)
        return assignment_node

    def flatten_expr(self, expr):
        flattened_expr = []
        if isinstance(expr, dict):
            flattened_expr.append(expr)
        elif isinstance(expr, list):
            for sub_expr in expr:
                flattened_expr.extend(self.flatten_expr(sub_expr))
        return flattened_expr


if __name__ == '__main__':

    ast_visitor = EvalVisitor()
    ast = ast_visitor.visit(tree)
    with open('output_files/ast.json', 'w') as f:
        f.write(json.dumps(json.loads(ast), indent=1))
    print('AST построено')
    


