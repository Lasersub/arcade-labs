import arcade

arcade.open_window(800,600,"PRIMER DIBUJO")
arcade.set_background_color(arcade.color.BLUE)

arcade.start_render()

#Césped
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BANGLADESH_GREEN)

#Tronco del árbol
arcade.draw_lrtb_rectangle_filled(380, 420, 200, 60, arcade.color.DARK_BROWN)

#Hojas del árbol
#HOJA1
arcade.draw_triangle_filled(250, 200, 550, 200, 400, 350, arcade.color.LIME_GREEN)
#HOJA2
arcade.draw_triangle_filled(270, 290, 530, 290, 400, 430, arcade.color.LIME_GREEN)
#HOJA3
arcade.draw_triangle_filled(290, 380, 510, 380, 400, 510, arcade.color.LIME_GREEN)

#Sol
arcade.draw_circle_filled(750, 550, 200, arcade.color.YELLOW)

#Bolas de navidad
#BOLA1
arcade.draw_circle_filled(350, 240, 15, arcade.color.RED)

#BOLA2
arcade.draw_circle_filled(430, 300, 15, arcade.color.PURPLE)

#BOLA3
arcade.draw_circle_filled(365, 345, 15, arcade.color.DARK_BLUE)

#BOLA4
arcade.draw_circle_filled(455, 410, 15, arcade.color.RED)

#BOLA5
arcade.draw_circle_filled(375, 430, 15, arcade.color.PURPLE)

#BOLA6
arcade.draw_circle_filled(460, 240, 15, arcade.color.DARK_BLUE)

#Estrella
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

#Nube
arcade.draw_circle_filled(110, 500, 50, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(180, 470, 50, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(170, 535, 50, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(210, 530, 50, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(250, 490, 50, arcade.color.LIGHT_GRAY)

#Casa del fondo
#PARED
arcade.draw_lrtb_rectangle_filled(50, 150, 200, 100, arcade.color.GRAY_BLUE)

#TEJADO
arcade.draw_triangle_filled(40, 200, 160, 200, 100, 250, arcade.color.LIGHT_RED_OCHRE)

#PUERTA
arcade.draw_lrtb_rectangle_filled(85, 115, 140, 100, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(105, 118, 5, arcade.color.BLACK)

#VENTANA1
arcade.draw_lrtb_rectangle_filled(60, 95, 190, 155, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(65, 90, 185, 160, arcade.color.BLACK)

#VENTANA2
arcade.draw_lrtb_rectangle_filled(105, 140, 190, 155, arcade.color.BONE)
arcade.draw_lrtb_rectangle_filled(110, 135, 185, 160, arcade.color.BLACK)








arcade.finish_render()

arcade.run()
