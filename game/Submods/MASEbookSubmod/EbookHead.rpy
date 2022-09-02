init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="MAS Ebook Submod",
        description="让你和莫妮卡一起读书",
        version='0.0.1',
    )
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MAS Ebook Submod",
            user_name="MAS-Submod-MoyuTeam",
            repository_name="MAS-EBook-Submod",
            update_dir="",
            attachment_id=None
        )
# animated_book
# (760, 50) (1240, 680)
image ebook_paper = "Submods/MASEbookSubmod/notebook.png"
screen ebook_show(texts=[]):
    viewport:
        area (760, 50, 480, 630)
        child_size (480, 630)
        vbox:
            box_wrap False
            for text1 in texts:
                hbox:
                    text text1:
                        font "gui/font/npy.ttf"
                        size 10