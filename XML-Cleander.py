# Import the RegEx and GUI modules
import re
from tkinter import * 
from tkinter import messagebox

#Create Application
class App:

  def __init__(self, master):
    self.sample = StringVar()
          
    #Create Footer
    body = Frame(master)
    footer = Frame(master)
    statusbar = Frame(master)
    
    # Establish Structure
    self.textentry = Text(body, height=10, width=90)
    self.textresults = Text(body, height=10, width=90)
    self.buttondisplay = Button(footer, text="Display Cleanup", command=self.processuserinput)
    self.buttonsave = Button(footer, text="Create XML", command=self.savecleanxml)
    self.buttonquit = Button(footer, text="Quit", fg="red", bg="GREY", command=footer.quit)
    self.status = Label(statusbar, textvariable=self.sample, bd=2,)
        
    # Generate Structure
    body.pack(side=TOP)
    self.textentry.pack(side=TOP)
    self.textresults.pack(side=TOP)
    
    footer.pack(side=TOP)       
    self.buttonquit.pack(side=RIGHT)
    self.buttonsave.pack(side=RIGHT)
    self.buttondisplay.pack(side=RIGHT)
    
    statusbar.pack(side=TOP)
    self.status.pack(side=RIGHT)
                
    #Populate Text Box with Text
    self.textentry.insert(END, "Copy from TCP")
    self.textresults.insert(END, "Results....")
  
  def processuserinput(self):
    # Reset variables 
    count = 0 
        
    # Set the max length of on XML node
    maxtextlength = 500
    cleantext = ''
       
    # Create list of common HTML tags to replace with ""
    commonhtmltags = ['<p>','</p>','<b>','</b>','<br>','</br>','<br/>','</li>','<li>','<ul>','</ul>','</div>','<span>','</span>',';br/gt;']

    # Delete the current Results Box
    self.textresults.delete(1.0,END)
        
    # Split Variable into lines
    for cleanlines in self.textentry.get(1.0,END).splitlines():
          
      # Replace any non-printable characters 
      cleanlines = cleanlines.encode("ascii",errors="ignore").decode()
          
      # Replace common HTML tags and count occurrences  
      for commonhtmltag in commonhtmltags:
        count += cleanlines.count(commonhtmltag)
        cleanlines = cleanlines.replace(commonhtmltag,'')

      # Replace invalid XML tag opening
      count += cleanlines.count('-<')
      cleanlines = cleanlines.replace('-<', '<')
      
      # Replace longer HTML tags (Matches anything that starts with the text, maybe characters that aren't ">", and then ">")
      cleanlines = re.sub("<div[^>]*>","",cleanlines)
      cleanlines = re.sub("<p [^>]*>","",cleanlines)

      # Shorten text when XML nodes exceeds the max length and count occurrences
      if len(cleanlines) > maxtextlength:
        count += 1
        cleanlines = cleanlines[:cleanlines.find('>') + 50] + "--Text Shortened--" + cleanlines[cleanlines.rfind('<'):]        
    
      # Add the clean line to the cleantext variable
      cleantext += cleanlines + "\n"
    
    # Copy the cleantext variable into the result box. 
    self.textresults.insert(END, cleantext)
        
    # Print out the error count
    errorcount = "{} Errors Found and Fixed".format(count)
    self.sample.set(errorcount)
    return errorcount
  
  def savecleanxml(cleanxml):
    print("hello")
    testboy = processuserinput()
    print(testboy)

root = Tk()
root.title("XML Cleaner")
root.geometry("500x400")
app = App(root)

root.mainloop()
root.destroy() # optional; see description below
