import streamlit as st

# Our built-in database
elements_db = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "mass": 1.008, "fact": "Most abundant element in the universe."},
    "He": {"name": "Helium", "atomic_number": 2, "mass": 4.0026, "fact": "Becomes a superfluid at near absolute zero."},
    "O": {"name": "Oxygen", "atomic_number": 8, "mass": 15.999, "fact": "Makes up about 21% of the Earth's atmosphere."},
    "C": {"name": "Carbon", "atomic_number": 6, "mass": 12.011, "fact": "The basis of all known life on Earth."}
}

# 1. Page Configuration and Title
st.set_page_config(page_title="Element Finder", page_icon="🧪")
st.title("🧪 Element Information Finder")
st.write("Welcome to the interactive periodic table lookup tool! Type a symbol below to see its properties.")

# 2. User Input Box
symbol = st.text_input("Enter an element symbol (e.g., H, He, O, C):").strip().capitalize()

# 3. Logic and Display
if symbol: # This runs only if the user has typed something
    if symbol in elements_db:
        data = elements_db[symbol]
        
        # Shows a green success banner
        st.success(f"Element Found: {data['name']} ({symbol})")
        
        # Layout columns for a clean, dashboard-like look
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Atomic Number", data['atomic_number'])
        with col2:
            st.metric("Atomic Mass", f"{data['mass']} u")
            
        # Shows a blue info banner
        st.info(f"**Fun Fact:** {data['fact']}")
    else:
        # Shows a red error banner
        st.error("Element not found in the database. Check your spelling or add it to the code!")

st.divider()
st.caption("Developed for Experiential Learning Project")