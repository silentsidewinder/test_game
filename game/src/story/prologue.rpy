label prologue:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sitting room

    # Start playing the music
    play music hope

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # Voice
    voice "audio/voice/greeting.ogg"

    show eileen happy

    # These display lines of dialogue.

    c_eileen "You've created a new Ren'Py game."

    c_eileen "This step is to show you  the branching dialogue options"

    c_eileen "Choose how to respond"

    menu:
        "Rude":
            show eileen angry

            c_eileen "F U."

        "Kind":
            show eileen surprised

            c_eileen "I didn't expect that."


    # Stop the music with a 2-seconds fadeout
    stop music fadeout 2.0
