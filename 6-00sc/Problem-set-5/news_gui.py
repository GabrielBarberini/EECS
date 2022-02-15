import Tkinter
import time

#root = Tk()
#root.withdraw()

# The Popup class
class Popup:
    def __init__(self):
        self.root = Tkinter.Tk()
	self.root.withdraw()
	"""
	self.root.mainloop()
        def drawALot():
            self.root = Tk()
            self.root.withdraw()
            self.root.mainloop()
        thread.start_new_thread(drawALot, ())
	"""
    def start(self):
        self.root.mainloop()

    def _makeTheWindow(self, item):
        """
        Private method that does the actual window drawing
        """
        root = Tkinter.Toplevel()
        root.wm_title("News Alert")
        
        w = root.winfo_screenwidth()/20
        h = root.winfo_screenheight()/4
        
        title = Tkinter.Text(root, padx=5, pady=5, height=3, wrap=Tkinter.WORD, bg="white")
        title.tag_config("title", foreground="black", font=("helvetica", 12, "bold"))
        title.tag_config("subject", foreground="black", font=("helvetica", 12, "bold"))
        title.insert(Tkinter.INSERT, "Title: %s" % item.get_title(), "title")
        title.insert(Tkinter.INSERT, "\nSubject: ", "subject")
        title.insert(Tkinter.INSERT, item.get_subject().rstrip(), "subject")    
        
        title.config(state=Tkinter.DISABLED, relief = Tkinter.FLAT)
        title.grid(sticky=Tkinter.W+Tkinter.E)
        
        summary = Tkinter.Text(root, padx=10, pady=5, height=15, wrap=Tkinter.WORD, bg="white")
        summary.tag_config("text", foreground="black", font=("helvetica", 12))
        summary.insert(Tkinter.INSERT, item.get_summary().lstrip(), "text")
        
        summary.config(state=Tkinter.DISABLED, relief = Tkinter.FLAT)
        summary.grid(sticky=Tkinter.W+Tkinter.E)
        
        link = Tkinter.Text(root, padx=5, pady=5, height=4, bg="white")
        link.tag_config("url", foreground="blue", font=("helvetica", 10, "bold"))
        link.insert(Tkinter.INSERT, item.get_link(), "url")
        
        link.config(state=Tkinter.DISABLED, relief=Tkinter.FLAT)
        link.grid(sticky=Tkinter.W+Tkinter.E)

    def newWindow(self, item):
        """
        Displays a popup with the contents of the NewsStory newsitem
        """
        self.root.after(0, self._makeTheWindow, item)

        
       

