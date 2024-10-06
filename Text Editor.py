from tkinter import *  # Import all from tkinter
import tkinter.filedialog as tk  # Import the filedialog for opening/saving files
import tkinter.messagebox as tk2  # Import the messagebox for pop-up messages


# Define the Application class that extends the tkinter Frame
class Application(Frame):

    # Initialize the class and set up the interface
    def __init__(self, master):
        # Call the constructor of the parent class (Frame)
        super(Application, self).__init__(master)
        # Create the UI components (widgets)
        self.create_widgets()

    # Method to create the text editor interface
    def create_widgets(self):
        # Create a text widget where users can type text
        self.text1 = Text(width=20, height=20)
        # Set the text widget to expand and fill the entire window
        self.text1.pack(expand=YES, fill=BOTH)

        # Create a menu bar for the main window
        menubar = Menu(self)

        # Create sub-menus for File, Edit, and Tools
        filemenu = Menu(menubar, tearoff=0)  # File menu
        editmenu = Menu(menubar, tearoff=0)  # Edit menu
        toolsmenu = Menu(menubar, tearoff=0)  # Tools menu

        # Add commands (menu items) to the File menu
        filemenu.add_command(label='New', command=self.newDoc)  # New document
        filemenu.add_command(label='Save', command=self.saveDoc)  # Save document
        filemenu.add_command(label='Open', command=self.openDoc)  # Open document

        # Add commands (menu items) to the Edit menu
        editmenu.add_command(label='Copy', command=self.copy)  # Copy text
        editmenu.add_command(label='Paste', command=self.paste)  # Paste text
        editmenu.add_command(label='Clear', command=self.clear)  # Clear text

        # Add a command (menu item) to the Tools menu
        toolsmenu.add_command(label='Word Count', command=self.wordCount)  # Word count tool

        # Add sub-menus to the main menu bar
        menubar.add_cascade(label='File', menu=filemenu)  # File menu
        menubar.add_cascade(label='Edit', menu=editmenu)  # Edit menu
        menubar.add_cascade(label='Tools', menu=toolsmenu)  # Tools menu

        # Attach the menu bar to the root window
        root.config(menu=menubar)

    # Method to create a new document (clears the text box)
    def newDoc(self):
        # Prompt the user to confirm if unsaved work might be lost
        if tk2.askyesno("Message", "Unsaved work will be lost. Continue?"):
            # If yes, clear the text box
            self.text1.delete("1.0", END)

    # Method to save the document to a file
    def saveDoc(self):
        # Open the save dialog to specify file name and location
        savefile = tk.asksaveasfile(mode='w', defaultextension=".txt")
        if savefile is not None:  # Ensure a file is selected
            # Get the text content from the text box
            text2save = str(self.text1.get("1.0", END))
            # Write the text to the selected file
            savefile.write(text2save)
            savefile.close()  # Close the file after saving

    # Method to open an existing file
    def openDoc(self):
        # Open a file dialog to choose a file
        openfile = tk.askopenfile(mode='r')
        if openfile is not None:  # Ensure a file is selected
            # Read the contents of the selected file
            text = openfile.read()
            # Clear the text box before inserting new content
            self.text1.delete("1.0", END)
            # Insert the file content into the text box
            self.text1.insert(END, text)
            openfile.close()  # Close the file after reading

    # Method to copy the selected text
    def copy(self):
        try:
            # Copy the selected text into the clipboard
            var = str(self.text1.get(SEL_FIRST, SEL_LAST))
            # Clear the clipboard first
            self.clipboard_clear()
            # Append the selected text to the clipboard
            self.clipboard_append(var)
        except TclError:
            # If no text is selected, show an error message
            tk2.showinfo('Error', 'No text selected to copy')

    # Method to paste text from the clipboard
    def paste(self):
        try:
            # Get the clipboard text
            result = self.selection_get(selection="CLIPBOARD")
            # Insert the clipboard text at the current cursor position
            self.text1.insert(INSERT, result)
        except TclError:
            # If clipboard is empty, show an error message
            tk2.showinfo('Error', 'Nothing to paste from clipboard')

    # Method to clear all text from the text box
    def clear(self):
        # Clear the entire text box content
        self.text1.delete("1.0", END)

    # Method to count words in the text box
    def wordCount(self):
        # Get all the text content from the text box
        userText = self.text1.get("1.0", END)
        # Split the text by whitespace to get individual words
        wordList = userText.split()
        # Calculate the number of words
        number_of_words = len(wordList)
        # Display the word count in a message box
        tk2.showinfo('Word Count', f'Words: {number_of_words}')


# Create the root window (main application window)
root = Tk()
root.title('Text Editor')  # Set the title of the window
root.geometry('700x600')  # Set the window size

# Create an instance of the Application class
app = Application(root)

# Start the main event loop (keeps the window open)
app.mainloop()
