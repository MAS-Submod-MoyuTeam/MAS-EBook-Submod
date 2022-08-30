init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="MAS Ebook Submod",
        description="让你和莫妮卡一起读书",
        version='0.0.1',
        settings_pane="np_setting_pane"
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