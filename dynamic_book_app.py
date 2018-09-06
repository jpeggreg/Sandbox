
from book import Book

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicBookApp(App):

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.book_list = []
        with open("books.csv", "r+") as book_file:
            for book in book_file:
                self.book_list.append(book.strip().split(","))
        print(self.book_list)

    def build(self):
        self.title = "Reading Tracker 2.0"
        self.root = Builder.load_file('dynamic_book_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for book in self.book_list:
            temp_button = Button(text=book[0], id=book[2])
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.name_button.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        pages = instance.id
        self.status_text = "{} has {} pages".format(name, pages)


DynamicBookApp().run()