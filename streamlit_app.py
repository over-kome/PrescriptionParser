import streamlit as st

from parser import format_simple, parse_medication_list

st.set_page_config(page_title="Prescription Parser", layout="wide")
st.title("Prescription Parser")
st.caption("Cole a prescrição bagunçada à esquerda — a versão limpa aparece à direita.")

left, right = st.columns(2)

with left:
    raw = st.text_area(
        "Entrada",
        height=600,
        placeholder=(
            "Dapagliflozina 10 mg\n"
            "1 comprimido, a cada 1 diaOralComprimido de liberação controlada"
            "Período:10/06/2026 - IndeterminadoQuantidade:30\n"
            "..."
        ),
    )

with right:
    st.markdown("**Saída**")
    meds = parse_medication_list(raw) if raw.strip() else []
    output = "\n\n".join(format_simple(m) for m in meds)
    if output:
        st.code(output, language=None)
    else:
        st.caption("(cole algo à esquerda)")
