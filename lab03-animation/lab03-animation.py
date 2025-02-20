import arcade


def cesped():
    """Cesped"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BANGLADESH_GREEN)


def hojas():
    """Hojas del arbol"""
    # HOJA1
    arcade.draw_triangle_filled(250, 200, 550, 200, 400, 350, arcade.color.LIME_GREEN)
    # HOJA2
    arcade.draw_triangle_filled(270, 290, 530, 290, 400, 430, arcade.color.LIME_GREEN)
    # HOJA3
    arcade.draw_triangle_filled(290, 380, 510, 380, 400, 510, arcade.color.LIME_GREEN)


def bolas_navidad():
    """Bolas de navidad"""
    # BOLA1
    arcade.draw_circle_filled(350, 240, 15, arcade.color.RED)
    # BOLA2
    arcade.draw_circle_filled(430, 300, 15, arcade.color.PURPLE)
    # BOLA3
    arcade.draw_circle_filled(365, 345, 15, arcade.color.DARK_BLUE)
    # BOLA4
    arcade.draw_circle_filled(455, 410, 15, arcade.color.RED)
    # BOLA5
    arcade.draw_circle_filled(375, 430, 15, arcade.color.PURPLE)
    # BOLA6
    arcade.draw_circle_filled(460, 240, 15, arcade.color.DARK_BLUE)


def estrella():
    """Estrella"""
    arcade.draw_polygon_filled([[400, 480],
                                [420, 455],
                                [425, 490],
                                [445, 500],
                                [410, 510],
                                [400, 540],
                                [390, 510],
                                [355, 500],
                                [375, 490],
                                [380, 455]],
                               arcade.color.GOLD)


def arbol():
    # Tronco del árbol
    arcade.draw_lrtb_rectangle_filled(380, 420, 200, 60, arcade.color.DARK_BROWN)
    # Hojas del árbol
    hojas()
    # Bolas de navidad
    bolas_navidad()
    # Estrella
    estrella()


def sol():
    """Sol"""
    arcade.draw_circle_filled(750, 550, 200, arcade.color.YELLOW)


def nube(x, y):
    """Nube"""
    arcade.draw_circle_filled(110 + x, 500 + y, 50, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(180 + x, 470 + y, 50, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(170 + x, 535 + y, 50, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(210 + x, 530 + y, 50, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(250 + x, 490 + y, 50, arcade.color.LIGHT_GRAY)


def draw_main():
    """Hace el dibujo completo"""


def ventanas_casa():
    """Ventanas de la casa"""
    # VENTANA1
    arcade.draw_lrtb_rectangle_filled(60, 95, 190, 155, arcade.color.BONE)
    arcade.draw_lrtb_rectangle_filled(65, 90, 185, 160, arcade.color.BLACK)
    # VENTANA2
    arcade.draw_lrtb_rectangle_filled(105, 140, 190, 155, arcade.color.BONE)
    arcade.draw_lrtb_rectangle_filled(110, 135, 185, 160, arcade.color.BLACK)


def casa():
    """Casa del fondo"""
    # PARED
    arcade.draw_lrtb_rectangle_filled(50, 150, 200, 100, arcade.color.GRAY_BLUE)
    # TEJADO
    arcade.draw_triangle_filled(40, 200, 160, 200, 100, 250, arcade.color.LIGHT_RED_OCHRE)
    # PUERTA
    arcade.draw_lrtb_rectangle_filled(85, 115, 140, 100, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(105, 118, 5, arcade.color.BLACK)
    # Ventanas
    ventanas_casa()


def on_draw(delta_time):
    """Genera el dibujo principal"""
    arcade.start_render()

    cesped()
    sol()
    nube(on_draw.nube1_x, 60)
    nube(on_draw.nube2_x, 20)
    arbol()
    casa()

    on_draw.nube1_x += 2
    on_draw.nube2_x += 1


on_draw.nube1_x = 100
on_draw.nube2_x = -100


def main():
    """Programa principal"""
    arcade.open_window(800, 600, "PRIMER DIBUJO")
    arcade.set_background_color(arcade.color.BLUE)

    arcade.schedule(on_draw, 1/60)

    arcade.run()

#CODIGO PRINCIPAL
main()


