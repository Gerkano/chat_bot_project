from tkinter import *
from tkinter import scrolledtext, ttk
import tkinter.font as font
from PIL import ImageTk, Image
from chatbot_config import AI_engine
from translator import LT_translate
import time
from topic_list import Progresor
from run_reset_gif import ResetGIF
import logging

logging.basicConfig(filename='logs_here.log', level=logging.DEBUG)

# GUI class which is main of the application
class GUI(Tk):

    def __init__(self) -> None:
      super().__init__()
      
      # Classes used through out the GUI
      self.translate = LT_translate
      self.chatbot = AI_engine
      self.topic = Progresor()
      self.rgif = ResetGIF

      # Main window and widgets
      self.main_menu()
      self.window_config()
      self.widgets()

      # Packs of main window and widgetss
      self.canvas1.pack(fill = "both", expand = True)
      self.canvas1.create_image( 0, 0, image = self.bg, anchor = "nw")
      self.text_area_canvas = self.canvas1.create_window( 45, 10, anchor = "nw", window = self.text_area)
      self.field_canvas = self.canvas1.create_window( 50, 325, anchor = "nw", window = self.field)
      self.button_canvas = self.canvas1.create_window( 250, 354, anchor = "nw", window = self.button)

    # Window and widget configurations, fonts, images 
    def window_config(self) -> None:
      self.title("Sad bot")
      self.geometry("600x500")
      self.canvas1 = Canvas(self, width = 600, height = 500)
      self.bgcolor = '#333359'
      self['background']=self.bgcolor
      self.img = ImageTk.PhotoImage(Image.open("images/bot_picture1.PNG"))
      self.myFont = font.Font(family='Bookman Old Style', size=12, weight='bold')
      self.bg = ImageTk.PhotoImage(file = "images/background.jpg")

    # Otpions menu buttons and commands
    def main_menu(self) -> None:
      menu_1 = Menu(self)
      self.config(menu=menu_1)
      submenu_1 = Menu(menu_1, tearoff = 0)
      menu_1.add_cascade(label="Options", menu=submenu_1)
      submenu_1.add_command(label="Reset memory", command=self.reset_memory)
      submenu_1.add_command(label="Learn english", command=self.learn_chatbot)
      submenu_1.add_command(label="Exit", command=self.destroy)

    # Widgets: Buttons, entry fields, test areas
    def widgets(self) -> None:
      self.user_input = StringVar()
      self.text_area = scrolledtext.ScrolledText(self,  width=45, height=16, wrap = WORD, font= self.myFont)
      self.text_area.config(state='disabled')
      self.field = Entry(self, width=45, font=self.myFont)
      self.button = Button(self, image=self.img, borderwidth=0, command=self._initiate_response) 
      self.button.config(width=80, height=80)
      self.bind("<Return>", lambda event: self._initiate_response())

    # User input, translations, Chatbot output, text area edit with output and translations
    def _initiate_response(self) -> None:
      self.user_input.set(self.field.get())
      user_input = self.user_input.get()
      logging.debug(f'Your entry: {user_input}')
      sad_bot_response = self.chatbot(user_input).sad_bot_ai()
      logging.debug(f'Chatterbot generated response: {sad_bot_response}')
      input_LT = self.translate(user_input).translate_input_lt()
      logging.debug(f'Your entry in lithuanian language: {input_LT}')
      output_LT = self.translate(sad_bot_response).translate_input_lt()
      logging.debug(f'Chatterbot response in lithuanian language: {output_LT}')
      translated = (f" You: {user_input}\n   (Lithuanian: {input_LT}) \n\n Sad bot: {sad_bot_response} \n   (Lithuanian: {output_LT}) \n\n")
      self.text_area.config(state='normal')
      self.text_area.insert('end', translated)
      self.text_area.yview('end')
      self.text_area.config(state='disabled')
      self.field.delete(0, 'end')

    # Method for chatbot to learning english
    def learn_chatbot(self) -> None:
      self.learn_progress_bar()

    # Learning progress bar after learn english initiated
    def learn_progress_bar(self) -> None:
      self.my_progress = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode='determinate')
      self.my_progress_canvas = self.canvas1.create_window( 130, 450, anchor = "nw", window = self.my_progress)
      self.__progress_step()
      
    # Progress step after each module is learned
    def __progress_step(self) -> None:
      self.tasks = len(self.topic.list_of_topic_names()) 
      self.count = 0
      logging.debug(f'Topics to learn for Chatterbot: {self.topic.list_of_topic_names()}')
      for file in self.topic.list_of_topic_names():
        time.sleep(1)
        self.my_progress['value'] += 100/self.tasks
        self.update_idletasks()
        self.chatbot().learn_english(file)
        self.count += 1
        logging.debug(f'Topic being installed: {file}')
        if self.count >= self.tasks:
          self.progress_stop()
          break

    # Progess bar stop after learning is complete, progress bar dissapears and the text area edited with Sad bot feedback
    def progress_stop(self) -> None:
      self.my_progress.stop()
      self.my_progress.destroy()
      self.text_area.config(state='normal')
      self.text_area.insert('end', "Sad bot: I'm ALIVE !!1!0!1 \n")
      self.text_area.yview('end')
      self.text_area.config(state='disabled')
      self.field.delete(0, 'end')

    # Chat bot memory reset
    def reset_memory(self) -> None:
      self.chatbot().bot_memory_wipe()
      self.rgif.play_gif(self)
      self.text_area.config(state='normal')
      self.text_area.delete(0.0, 'end')
      self.text_area.config(state='disabled')
      

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
