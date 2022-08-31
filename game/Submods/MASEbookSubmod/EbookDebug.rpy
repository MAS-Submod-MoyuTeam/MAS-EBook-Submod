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