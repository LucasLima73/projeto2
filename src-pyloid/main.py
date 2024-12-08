from pyloid import (
    Pyloid,
    PyloidAPI,
    Bridge,
    TrayEvent,
    is_production,
    get_production_path,
)
import os
import time

app = Pyloid(app_name="Pyloid-App", single_instance=True)

# Configurar ícones do aplicativo
try:
    if is_production():
        app.set_icon(os.path.join(get_production_path(), "icons/icon.png"))
        app.set_tray_icon(os.path.join(get_production_path(), "icons/icon.png"))
    else:
        app.set_icon("src-pyloid/icons/icon.png")
        app.set_tray_icon("src-pyloid/icons/icon.png")
except Exception as e:
    print(f"Erro ao configurar ícones: {e}")

############################## Splash Screen ##############################
# Configuração da Splash Screen
try:
    splash_image_path = (
        os.path.join(get_production_path(), "src-pyloid/icons/icon.png")
        if is_production()
        else "src-pyloid/icons/icon.png"
    )

    splash_window = app.create_window("Splash Screen Example", resizable=False)
    splash_window.set_static_image_splash_screen(image_path=splash_image_path)
    splash_window.set_size(400, 400)
    splash_window.center()
    splash_window.show()

    # Simulação de carregamento ou inicialização
    time.sleep(5)

    # Fecha a Splash Screen
    splash_window.close()
except Exception as e:
    print(f"Erro ao exibir a Splash Screen: {e}")
############################################################################

############################## Tray ################################
def on_double_click():
    print("Tray icon was double-clicked.")

try:
    app.set_tray_actions(
        {
            TrayEvent.DoubleClick: on_double_click,
        }
    )
    app.set_tray_menu_items(
        [
            {"label": "Show Window", "callback": app.show_and_focus_main_window},
            {"label": "Exit", "callback": app.quit},
        ]
    )
except Exception as e:
    print(f"Erro ao configurar o Tray: {e}")
####################################################################

############################## Bridge ##############################
class custom(PyloidAPI):
    @Bridge(result=str)
    def create_window(self):
        window = self.app.create_window(
            title="Pyloid Browser-2",
            js_apis=[custom()],
        )

        window.set_size(1000, 800)
        window.set_position(0, 0)

        try:
            if is_production():
                window.set_dev_tools(False)
                window.load_file(os.path.join(get_production_path(), "build/index.html"))
            else:
                window.set_dev_tools(True)
                window.load_url("http://localhost:5173")
        except Exception as e:
            print(f"Erro ao carregar a janela principal: {e}")

        window.show()
        window.focus()
        return window.id
####################################################################

############################## Main Window #########################
try:
    if is_production():
        # production
        window = app.create_window(
            title="Pyloid Browser-production",
            js_apis=[custom()],
        )
        window.load_file(os.path.join(get_production_path(), "build/index.html"))
    else:
        window = app.create_window(
            title="Pyloid Browser-dev",
            js_apis=[custom()],
            dev_tools=True,
        )
        window.load_url("http://localhost:5173")

    window.show_and_focus()
except Exception as e:
    print(f"Erro ao inicializar a janela principal: {e}")
####################################################################

app.run()
