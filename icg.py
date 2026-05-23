# ================================================================
# Project Title : Recent Methodologies in Intermediate Code Generation (ICG)
# Part : Three Address Code (TAC) Generator - Streamlit Frontend Version
# Course : Compiler Design (CCA3)
# Institute : MIT World Peace University
# Authors : Spruha Umarani
# ================================================================

import streamlit as st

# ---------- Helper Function: Infix to Postfix Conversion ----------
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = ""

    for ch in expression:
        if ch.isalnum():
            output += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[ch]:
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()
    return output


# ---------- Function: Generate Three Address Code (TAC) ----------
def generate_icg(expression):
    temp_count = 1
    stack = []
    output = []

    for ch in expression:
        if ch.isalnum():
            stack.append(ch)
        elif ch in "+-*/^":
            op2 = stack.pop()
            op1 = stack.pop()
            temp = f"t{temp_count}"
            temp_count += 1
            output.append(f"{temp} = {op1} {ch} {op2}")
            stack.append(temp)

    result = stack.pop()
    output.append(f"a = {result}")
    return output


# ---------- Streamlit Frontend ----------
st.set_page_config(page_title="3AC Generator", page_icon="⚙️", layout="centered")

st.title("⚙️ Three Address Code (3AC) Generator")
st.write("### Traditional Intermediate Code Generation (ICG) Technique")

st.info("Enter an infix expression like `a*b+c/d` to generate the equivalent Three Address Code (TAC).")

expression = st.text_input("Enter infix expression:", placeholder="e.g. a*b+c/d")

if st.button("Generate 3AC"):
    if expression.strip():
        postfix_expr = infix_to_postfix(expression.replace(" ", ""))
        st.subheader("📘 Postfix Expression:")
        st.code(postfix_expr, language="text")

        tac = generate_icg(postfix_expr)
        st.subheader("✅ Generated Three Address Code:")
        for line in tac:
            st.code(line, language="text")
    else:
        st.warning("Please enter a valid infix expression.")
