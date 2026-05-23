# ================================================================
# Project Title : Recent Methodologies in Intermediate Code Generation (ICG)
# Part : Static Single Assignment (SSA) - Streamlit Frontend Version
# Course : Compiler Design (CCA3)
# Institute : MIT World Peace University
# Authors : Spruha Umarani
#  ================================================================

import streamlit as st


# ---------- SSA Conversion Logic ----------

def convert_to_ssa(code_lines):

    versions = {}

    ssa_output = []

    for line in code_lines:

        if "=" not in line:
            continue

        var, expr = [x.strip() for x in line.split('=')]


        # Replace variables using previous/latest versions
        for v in versions:

            expr = expr.replace(
                v,
                f"{v}{versions[v]}"
            )


        # Create new version for assigned variable
        versions[var] = versions.get(var, 0) + 1

        var_versioned = f"{var}{versions[var]}"


        # Append SSA statement
        ssa_output.append(
            f"{var_versioned} = {expr}"
        )

    return ssa_output


# ---------- Streamlit Frontend ----------

st.set_page_config(
    page_title="SSA Simulator",
    page_icon="🧠",
    layout="centered"
)

st.title("Static Single Assignment (SSA) Simulator")

st.write(
    "Demonstrating a Recent Methodology "
    "in Intermediate Code Generation (ICG)"
)

st.info(
    "Each variable is assigned only once. "
    "New versions (a1, a2, etc.) are "
    "created whenever values change."
)


# ---------- User Input ----------

n = st.number_input(
    "Enter number of statements:",
    min_value=1,
    step=1
)

code_lines = []

for i in range(n):

    stmt = st.text_input(
        f"Statement {i + 1}",
        placeholder="e.g. a = b + c"
    )

    if stmt:
        code_lines.append(stmt)


# ---------- SSA Button ----------

if st.button("Convert to SSA"):

    if code_lines:

        st.subheader("Original Code")

        for line in code_lines:
            st.text(line)


        ssa_code = convert_to_ssa(code_lines)


        st.subheader("SSA Form")

        for line in ssa_code:
            st.code(line, language="text")

    else:

        st.warning(
            "Please enter at least one statement."
        )