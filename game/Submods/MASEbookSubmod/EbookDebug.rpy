init 5 python:
    EbookDebug = True
    if EbookDebug:
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="ebook_checktxt",
                random=True
            )
        )
label ebook_checktxt:
    $ eb_function.check_txt()
    $ eb_function.move_txt()
    return

label ebook_showtest:
    python:
        test = ["第一行", "第二行", "这是一个好长好长的第三行啊啊啊这是一个好长好长的第三行啊啊啊这是一个好长好长的第三行啊啊啊这是一个好长好长的第三行啊啊啊这是一个好长好长的第三行啊啊啊这是一个好长好长的第三行啊啊啊这是一个好长好长的第三行啊啊啊这是一个好长好长的第三行啊啊啊",
            "第四行desu"]
    show ebook_paper zorder 12
    show screen ebook_show(test)
    with Pause(10)
    hide screen ebook_show
    