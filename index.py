from manim import *
import numpy as np
import json


with open("parametros_simulacao.json", "r") as file:
    params = json.load(file)

class DoublePendulum(ThreeDScene):
    def construct(self):

        # Parâmetros da simulação
        
        g = params["g"]
        L1, L2 = params["L1"], params["L2"]
        M1, M2 = params["M1"], params["M2"]
        dt = params["dt"]

        # velocidades iniciais
        theta1, theta2 = params["theta1"], params["theta2"]
        omega1, omega2 = params["omega1"], params["omega2"]

        # Ponto de origem
        origin = np.array([0, 0, 2])

        # Criação dos objetos do pêndulo
        rod1 = Line(origin, origin, color=BLUE)
        rod2 = Line(origin, origin, color=GREEN)
        mass1 = Sphere(radius=0.25, color=BLUE)
        mass2 = Sphere(radius=0.25, color=GREEN)

        rod1.set_color(PURPLE)
        mass1.set_color(YELLOW)


        pendulum = VGroup(rod1, rod2, mass1, mass2)
        self.add(pendulum)

        # Adicionando eixos 3D e rótulos
        axes = ThreeDAxes()
        axes.set_color(GREY)    
        lab_x = axes.get_x_axis_label(Tex("$x$"))
        lab_y = axes.get_y_axis_label(Tex("$y$"))
        lab_z = axes.get_z_axis_label(Tex("$z$"))
        self.add(axes, lab_x, lab_y, lab_z)

        self.rotation = -45  

        def update(mob, dt=dt):
            nonlocal theta1, theta2, omega1, omega2

            # ângulo delta
            delta = theta2 - theta1

            # Cálculo das acelerações usando as equações do pêndulo duplo
            den = 2*M1 + M2 - M2*np.cos(2*theta1 - 2*theta2)
            
            a1 = (-g*(2*M1+M2)*np.sin(theta1) - M2*g*np.sin(theta1-2*theta2) -2*np.sin(delta)*M2*(omega2**2*L2 + omega1**2*L1*np.cos(delta))) / (L1*den)
            
            a2 = (2*np.sin(delta)*(omega1**2*L1*(M1+M2) + g*(M1+M2)*np.cos(theta1) + omega2**2*L2*M2*np.cos(delta))) / (L2*den)

            # Avelocidades e ângulos
            omega1 += a1 * dt
            omega2 += a2 * dt
            theta1 += omega1 * dt
            theta2 += omega2 * dt

            # posições das massas
            pos1 = origin + L1 * np.array([0, np.sin(theta1), -np.cos(theta1)])
            pos2 = pos1 + L2 * np.array([0, np.sin(theta2), np.cos(theta2)])

            rod1.put_start_and_end_on(origin, pos1)
            rod2.put_start_and_end_on(pos1, pos2)
            mass1.move_to(pos1)
            mass2.move_to(pos2)

            # camera
            self.rotation += 1
            self.set_camera_orientation(phi=60*DEGREES, theta=self.rotation*DEGREES)

        # update pendulo
        pendulum.add_updater(update)

        self.wait(10)

DoublePendulum().render()
