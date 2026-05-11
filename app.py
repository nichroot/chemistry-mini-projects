import streamlit as st

# Our built-in database
elements_db = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "mass": 1.008, "fact": "Most abundant element in the universe."},
    "He": {"name": "Helium", "atomic_number": 2, "mass": 4.0026, "fact": "Becomes a superfluid at near absolute zero."},
    "Li": {"name": "Lithium", "atomic_number": 3, "mass": 6.94, "fact": "The lightest metal, widely used in batteries."},
    "Be": {"name": "Beryllium", "atomic_number": 4, "mass": 9.0122, "fact": "Used in aerospace components due to its stiffness and light weight."},
    "B": {"name": "Boron", "atomic_number": 5, "mass": 10.81, "fact": "Used in flares to produce a distinctive green color."},
    "C": {"name": "Carbon", "atomic_number": 6, "mass": 12.011, "fact": "The basis of all known life on Earth."},
    "N": {"name": "Nitrogen", "atomic_number": 7, "mass": 14.007, "fact": "Makes up about 78% of the Earth's atmosphere."},
    "O": {"name": "Oxygen", "atomic_number": 8, "mass": 15.999, "fact": "Makes up about 21% of the Earth's atmosphere."},
    "F": {"name": "Fluorine", "atomic_number": 9, "mass": 18.998, "fact": "The most reactive chemical element."},
    "Ne": {"name": "Neon", "atomic_number": 10, "mass": 20.180, "fact": "Glows a bright reddish-orange in vacuum discharge tubes."},
    "Na": {"name": "Sodium", "atomic_number": 11, "mass": 22.990, "fact": "A highly reactive metal that can explode in water."},
    "Mg": {"name": "Magnesium", "atomic_number": 12, "mass": 24.305, "fact": "Burns with a brilliant white light."},
    "Al": {"name": "Aluminum", "atomic_number": 13, "mass": 26.982, "fact": "The most abundant metal in the Earth's crust."},
    "Si": {"name": "Silicon", "atomic_number": 14, "mass": 28.085, "fact": "The primary material used to make computer chips."},
    "P": {"name": "Phosphorus", "atomic_number": 15, "mass": 30.974, "fact": "Discovered by an alchemist boiling down urine."},
    "S": {"name": "Sulfur", "atomic_number": 16, "mass": 32.06, "fact": "Known in ancient times as 'brimstone'."},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "mass": 35.45, "fact": "Used widely to purify drinking water and swimming pools."},
    "Ar": {"name": "Argon", "atomic_number": 18, "mass": 39.95, "fact": "An inert gas often used inside incandescent light bulbs."},
    "K": {"name": "Potassium", "atomic_number": 19, "mass": 39.098, "fact": "Essential for nerve function; found abundantly in bananas."},
    "Ca": {"name": "Calcium", "atomic_number": 20, "mass": 40.078, "fact": "Essential for living organisms, particularly in bones and teeth."}
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
