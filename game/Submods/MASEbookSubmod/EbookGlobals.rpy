init -900 python in eb_globals:
    import store
    submod_path = renpy.config.basedir + "/game/Submods/MASEbookSubmod"
    ebook_path = submod_path + "/EBooks"
    check_path = renpy.config.basedir + "/characters"

    if renpy.android:
        submod_path = renpy.config.basedir + "/game/Submods/MASEbookSubmod"
        ebook_path = submod_path + "/EBooks"
        check_path = renpy.config.basedir + "/characters"
        
    # 待处理txt
    new_txt = []

    debugmode = True