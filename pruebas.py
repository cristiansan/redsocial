# import kivy
# from kivy.uix.label import Label

# class MyApp(App):
#     def build(self):
#         return Label(text="Tech with Tim")

# if __name__ ==" __pruebas__":
#     MyApp().run()


# from kivy.app import App
# from kivy.uix.button import Button
#id, nombre, apellido, clave, email, ciudad, edad, sexo, fecha_nac, posteo

# class TituloApp(App):
#     def build(self):
#         return Button(text='Hello World')

# TituloApp().run()
from usuario import Usuario

test= Usuario(1, "antocris", "lunasan", "234234", "sdfsdfq@sdfsdf.com", "Caracas", "40", "M", "10-10-1990")
test.set_posteo("hola")
test.set_posteo("chau")

print(test.get_nombre())
print(test.get_posteo())

fff=print(f'id: {test.id}')
print(fff)
