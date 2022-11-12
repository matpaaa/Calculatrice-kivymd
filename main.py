import sqlite3
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable

Window.size = (300, 500)

KV = """
MDFloatLayout:

    MDBottomNavigation:
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: "calculatrice"
            text: "Calculatrice"
            icon: "calculator"

            MDCard:
                size_hint: .9,.2
                pos_hint: {"center_x":.5,"center_y":.87}
                md_bg_color: "white"

            MDLabel:
                id: label
                text: ""
                pos_hint: {"center_y":.87}
                halign: "center"
                bold: True
                font_style: "H5"

            MDTextButton:
                text: "AC"
                pos_hint: {"center_x":.12,"center_y":.7}
                size_hint_x: .1
                on_press: app.ac()  
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDTextButton:
                text: "PI"
                pos_hint: {"center_x":.37,"center_y":.7}
                size_hint_x: .05
                on_press: app.pi()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: parenthese
                text: "()"
                pos_hint: {"center_x":.62,"center_y":.7}
                size_hint_x: .05
                on_press: app.parenthese()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: diviser
                text: "/"
                pos_hint: {"center_x":.87,"center_y":.7}
                size_hint_x: .05
                on_press: app.diviser()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color


            MDRectangleFlatButton:
                id: sept
                text: "7"
                pos_hint: {"center_x":.12,"center_y":.6}
                size_hint_x: .05
                on_press: app.sept()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: huit
                text: "8"
                pos_hint: {"center_x":.37,"center_y":.6}
                size_hint_x: .05
                on_press: app.huit()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: neuf
                text: "9"
                pos_hint: {"center_x":.62,"center_y":.6}
                size_hint_x: .05
                on_press: app.neuf()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: quatre
                text: "4"
                pos_hint: {"center_x":.12,"center_y":.5}
                size_hint_x: .05
                on_press: app.quatre()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: cinq
                text: "5"
                pos_hint: {"center_x":.37,"center_y":.5}
                size_hint_x: .05
                on_press: app.cinq()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: six
                text: "6"
                pos_hint: {"center_x":.62,"center_y":.5}
                size_hint_x: .05
                on_press: app.six()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: un
                text: "1"
                pos_hint: {"center_x":.12,"center_y":.4}
                size_hint_x: .05
                on_press: app.un()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: deux
                text: "2"
                pos_hint: {"center_x":.37,"center_y":.4}
                size_hint_x: .05
                on_press: app.deux()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: trois
                text: "3"
                pos_hint: {"center_x":.62,"center_y":.4}
                size_hint_x: .05
                on_press: app.trois()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color


            MDRaisedButton:
                text: "*"
                pos_hint: {"center_x":.87,"center_y":.6}
                size_hint_x: .05
                elevation: 0
                on_press: app.fois()
                theme_text_color: "Custom"
                md_bg_color: app.theme_cls.primary_color

            MDRaisedButton:
                text: "-"
                pos_hint: {"center_x":.87,"center_y":.5}
                size_hint_x: .05
                elevation: 0
                on_press: app.moins()
                theme_text_color: "Custom"
                md_bg_color: app.theme_cls.primary_color

            MDRaisedButton:
                text: "+"
                pos_hint: {"center_x":.87,"center_y":.4}
                size_hint_x: .05
                elevation: 0
                on_press: app.plus()
                theme_text_color: "Custom"
                md_bg_color: app.theme_cls.primary_color


            MDRectangleFlatButton:
                id: zero
                text: "0"
                pos_hint: {"center_x":.37,"center_y":.3}
                size_hint_x: .05
                on_press: app.zero()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDRectangleFlatButton:
                id: virgule
                text: ","
                pos_hint: {"center_x":.62,"center_y":.3}
                size_hint_x: .05
                on_press: app.virgule()
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color

            MDFillRoundFlatButton:
                text: "="
                pos_hint: {"center_x":.87,"center_y":.3}
                size_hint_x: .05
                on_press: app.egale()
                theme_text_color: "Custom"
                md_bg_color: app.theme_cls.primary_color

            MDRaisedButton:
                text: "²"
                pos_hint: {"center_x":.12,"center_y":.3}
                size_hint_x: .05
                elevation: 0
                on_press: app.carre()
                theme_text_color: "Custom"
                md_bg_color: app.theme_cls.primary_color

            MDIconButton:
                icon: "delete"
                pos_hint: {"center_x":.5,"center_y":.15}
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_press: app.delete()


        MDBottomNavigationItem:
            name: "historique"
            text: "Historique"
            icon: "database-edit"

            AnchorLayout:
                id: historique



        MDBottomNavigationItem:
            name: "parametre"
            text: "Paramètre"
            icon: "menu"

            MDLabel:
                id: label_switch_theme
                text: "Theme Style :"
                halign: "center"
                pos_hint: {"center_x":.2,"center_y":.9}
                bold: True
                theme_text_color: "Custom"

            MDSwitch:
                on_active: app.switch_theme()
                pos_hint: {"center_x":.6,"center_y":.9}

            MDLabel:
                id: label_switch_color
                text: "Theme Color :"
                halign: "center"
                pos_hint: {"center_x":.2,"center_y":.8}
                bold: True
                theme_text_color: "Custom"

            MDRectangleFlatButton:
                id: red_button
                pos_hint: {"center_x":.55,"center_y":.8}
                text: "Red"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_press: app.switch_color("red")

            MDRectangleFlatButton:
                id: blue_button
                pos_hint: {"center_x":.8,"center_y":.8}
                text: "Blue"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_press: app.switch_color("blue")

            MDRectangleFlatButton:
                id: green_button
                pos_hint: {"center_x":.55,"center_y":.7}
                text: "Green"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_press: app.switch_color("green")

            MDRectangleFlatButton:
                id: purple_button
                pos_hint: {"center_x":.8,"center_y":.7}
                text: "Purple"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_press: app.switch_color("purple")

            MDRectangleFlatButton:
                id: reset_historique_button
                pos_hint: {"center_x":.3,"center_y":.6}
                text: "Supprimer l'Historique"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                on_press: app.delete_historique()
"""


class MainApp(MDApp):
    def build(self):
        self.screen = Screen()
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"

        self.result = ""
        self.x = True
        self.data_tables_values = []
        self.connection = connection
        self.cursor = cursor
        self.init_table = True

        self.button = Builder.load_string(KV)
        self.screen.add_widget(self.button)

        self.create_db()
        self.create_table_data()

        return self.screen

    def create_db(self):
        self.cursor.execute("""create table if not exists Data(
        calcul text,
        resultat text)
        """)
        self.connection.commit()

    def create_table_data(self):
        self.cursor.execute("select * from Data")
        if len(self.cursor.fetchall()) == 0:
            self.data_tables = MDDataTable(
                size_hint=(0.9, 0.85), elevation=0, rows_num=300,
                column_data=[
                    ("Calcul", 30),
                    ("Résultat", 30),
                ],
                row_data=self.data_tables_values
            )
        else:
            self.data_tables = MDDataTable(
                size_hint=(0.9, 0.85), elevation=0, rows_num=300,
                column_data=[
                    ("Calcul", 30),
                    ("Résultat", 30),
                ],
                row_data=self.data_tables_values
            )
            self.cursor.execute("select * from Data")
            if self.init_table:
                for values in self.cursor.fetchall():
                    self.data_tables.add_row(values)
                self.cursor.execute("select * from Data")
                self.data_tables_values = self.cursor.fetchall()

        self.button.ids.historique.add_widget(self.data_tables)
        self.init_table = False
        print(self.data_tables_values)

    def ac(self):
        self.result = ""
        self.button.ids.label.text = ""

    def pi(self):
        self.result += "3.14"
        self.button.ids.label.text = self.result

    def parenthese(self):
        if self.x:
            self.result += ("(")
            self.x = False
        else:
            self.result += (")")
            self.x = True
        self.button.ids.label.text = self.result

    def diviser(self):
        self.result += ("/")
        self.button.ids.label.text = self.result

    def plus(self):
        self.result += ("+")
        self.button.ids.label.text = self.result

    def moins(self):
        self.result += ("-")
        self.button.ids.label.text = self.result

    def fois(self):
        self.result += ("*")
        self.button.ids.label.text = self.result

    def un(self):
        self.result += ("1")
        self.button.ids.label.text = self.result

    def deux(self):
        self.result += ("2")
        self.button.ids.label.text = self.result

    def trois(self):
        self.result += ("3")
        self.button.ids.label.text = self.result

    def quatre(self):
        self.result += ("4")
        self.button.ids.label.text = self.result

    def cinq(self):
        self.result += ("5")
        self.button.ids.label.text = self.result

    def six(self):
        self.result += ("6")
        self.button.ids.label.text = self.result

    def sept(self):
        self.result += ("7")
        self.button.ids.label.text = self.result

    def huit(self):
        self.result += ("8")
        self.button.ids.label.text = self.result

    def neuf(self):
        self.result += ("9")
        self.button.ids.label.text = self.result

    def zero(self):
        self.result += ("0")
        self.button.ids.label.text = self.result

    def virgule(self):
        self.result += (".")
        self.button.ids.label.text = self.result

    def carre(self):
        self.result += ("**2")
        self.button.ids.label.text = self.result

    def delete(self):
        self.result = self.result[:-1]
        self.button.ids.label.text = self.result

    def egale(self):
        if self.result == "":
            self.button.ids.label.text = "ERROR"
            self.result_final = "ERROR"
            return
        try:
            self.result_final = eval(self.result)
            self.button.ids.label.text = str(self.result_final)
        except:
            self.button.ids.label.text = "ERROR"
            self.result_final = "ERROR"
        self.data_tables.add_row((self.result, self.result_final))
        self.data_tables_values = self.data_tables.row_data
        self.cursor.execute("insert into Data values(?,?)",(self.result,self.result_final,))
        self.connection.commit()

    def switch_theme(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.button.ids.label_switch_theme.color = (1, 1, 1, 1)
            self.button.ids.label_switch_color.color = (1, 1, 1, 1)
            self.create_table_data()

        else:
            self.theme_cls.theme_style = "Light"
            self.button.ids.label_switch_theme.color = (0, 0, 0, 1)
            self.button.ids.label_switch_color.color = (0, 0, 0, 1)
            self.create_table_data()

    def switch_color(self, instance):
        if instance == "blue":
            self.theme_cls.primary_palette = "Blue"

        elif instance == "green":
            self.theme_cls.primary_palette = "Green"

        elif instance == "purple":
            self.theme_cls.primary_palette = "Purple"

        elif instance == "red":
            self.theme_cls.primary_palette = "Red"

        self.button.ids.blue_button.line_color = self.theme_cls.primary_color
        self.button.ids.red_button.line_color = self.theme_cls.primary_color
        self.button.ids.green_button.line_color = self.theme_cls.primary_color
        self.button.ids.purple_button.line_color = self.theme_cls.primary_color

        self.button.ids.zero.line_color = self.theme_cls.primary_color
        self.button.ids.un.line_color = self.theme_cls.primary_color
        self.button.ids.deux.line_color = self.theme_cls.primary_color
        self.button.ids.trois.line_color = self.theme_cls.primary_color
        self.button.ids.quatre.line_color = self.theme_cls.primary_color
        self.button.ids.cinq.line_color = self.theme_cls.primary_color
        self.button.ids.six.line_color = self.theme_cls.primary_color
        self.button.ids.sept.line_color = self.theme_cls.primary_color
        self.button.ids.huit.line_color = self.theme_cls.primary_color
        self.button.ids.neuf.line_color = self.theme_cls.primary_color
        self.button.ids.virgule.line_color = self.theme_cls.primary_color
        self.button.ids.parenthese.line_color = self.theme_cls.primary_color
        self.button.ids.diviser.line_color = self.theme_cls.primary_color
        self.button.ids.reset_historique_button.line_color = self.theme_cls.primary_color

    def delete_historique(self):
        if len(self.data_tables.row_data) >= 1:
            for i in range(len(self.data_tables.row_data)):
                self.data_tables.remove_row(self.data_tables.row_data[-1])

        self.data_tables_values = []
        self.cursor.execute("delete from Data")
        self.connection.commit()


connection = sqlite3.connect("data.db")
cursor = connection.cursor()

MainApp().run()

connection.close()