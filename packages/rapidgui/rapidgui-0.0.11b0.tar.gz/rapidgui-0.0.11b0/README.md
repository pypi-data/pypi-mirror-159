# rapidGui

No fuss rapid gui for quick and easy development

## how to use:

For quick setup, create instance of quickgui class and add member variables:

    q = rapidgui.quickGui()
    
    q.value = "eyooo?"
    q.variable = 42.0

    def clickMe():
        print("hello world")

    q.hello = clickMe

This will create a tkinter window that contains titles and controls to change these variables.

Currently only these types are supported:

> int, float - will create a ttk.spinbox
>
>string - will create a ttk.entry
>
>function - will create a ttk.button