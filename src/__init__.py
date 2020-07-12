import aqt
from aqt import dialogs, mw


from .editcurrent import PersistentEditCurrent
from .reviewer import PersistentReviewer
from .tagedit import PersistentTagEdit

def init():
    dialogs.register_dialog('EditCurrent', PersistentEditCurrent, None)

    aqt.tagedit.TagEdit = PersistentTagEdit
    mw.reviewer = PersistentReviewer(mw)