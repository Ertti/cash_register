def go_to_main_kategorijas(current_window):
    current_window.destroy()
    from main_kategorijas import main_kategorijas_page
    main_kategorijas_page()

def go_to_konditorija(current_window):
    current_window.destroy()
    from Konditorija import konditorija_page
    konditorija_page()