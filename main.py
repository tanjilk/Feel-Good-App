# Importar necessários pacotes de kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.gridlayout import GridLayout
import json
from datetime import datetime

# Carrega o design.kv com o método Builder
Builder.load_file('design.kv')

# Classe LoginScreen que faz henrança com o objeto Screen
# Login Screen pagina inicial


class LoginScreen(Screen):
	# Se pressionar no botao do sign up, irá para sign up
	# Ir para a pagina Sign Up

	# Botão de sign up
	def sign_up(self):
		self.manager.current = "sign_up_screen"
		print("Sign Up Button Pressed.")

	# Butão do Login
	def login(self, username, password):
		with open("users.json") as file:
			users = json.load(file)
		# Verifica se os credenciais estão corretos

		# Verifica se o input do username está no ficheiro json e verifica se a password do username é igual a da password do input

		if username in users and users[username]['password'] == password:
			# Se correspondeu, irá para outra pagina
			self.manager.current = 'login_screen_success'
		else:
			# Se não correspondeu, irá para outra página
			
			self.ids.wrong_login.text = "Wrong username or password!"

class RootWidget(ScreenManager):
	pass

# Classe depois de fazer login com sucesso
class LoginScreenSuccess(Screen):
	def log_out(self):
		self.manager.transition.direction = "right"
		self.manager.current = "login_screen"

# Classe da pagina de criar conta

class SignUpScreen(Screen):
	# Método para adicionar os dados
	def add_user(self, username, password):
		with open("users.json") as file:
			users = json.load(file)
		# Recebe Dados
		users[username] = {
			'username':username,
			'password':password,
			'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")
		}
		# Adiciona Dados
		with open("users.json", 'w') as file:
			json.dump(users, file)
		self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
	def go_back(self):

		self.manager.transition.direction = 'right'
		self.manager.current = "login_screen"

# Classe para criar a aplicação

class MainApp(App):
	def build(self):
		return RootWidget()

# Rodar a aplicação

if __name__ == "__main__":
	MainApp().run()

