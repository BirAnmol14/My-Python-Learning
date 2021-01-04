import ytmp3
import tkinter as tk


def downloadVideo():
    if len(txt.get())==0:
        return
    url=txt.get()
    txt.delete(0,len(url))
    txt.pack_forget()
    getBut.pack_forget()
    dataLabel.configure(text='Download complete')    
    ytmp3.downloaderUI(url)

#Building UI
root=tk.Tk()
root.geometry('700x600')
root.title('YTMP3')
dataLabel=tk.Label(root,text='Enter youtube url',font=('poppins',20,'bold'))
txt=tk.Entry(root,width=50)
getBut=tk.Button(root,text='Download',command=downloadVideo)
dataLabel.pack(padx=10, pady=10)
txt.pack(padx=10, pady=10)
getBut.pack(padx=10, pady=10)
root.mainloop()
