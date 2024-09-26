import streamlit as st

# Initialisation de X dans le session state si elle n'existe pas
if 'X' not in st.session_state:
    st.session_state.X = "Le toggle n'a pas été utilisé"

# Fonction de mise à jour de X uniquement lorsque le toggle change
def update_x():
    st.session_state.X = "Le toggle est activé" if st.session_state.toggle else "Le toggle est désactivé"

# Création du toggle avec session_state et rappel lors du changement d'état
st.toggle('Activer/désactiver', key='toggle', on_change=update_x)

# Affichage de la variable X
st.write(f"Valeur de X : {st.session_state.X}")