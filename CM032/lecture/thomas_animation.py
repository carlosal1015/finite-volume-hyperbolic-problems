#!/usr/bin/env python3
"""
Manim animation for Thomas Algorithm (Tridiagonal Matrix Algorithm)
Based on CM032/lecture/thomas.tex
"""

import numpy as np
from manim import *


class ThomasAlgorithmIntro(Scene):
    """Introduction to Thomas Algorithm"""

    def construct(self):
        # Title
        title = Title("Algoritmo de Thomas", include_underline=True)
        self.add(title)

        # Subtitle
        subtitle = Text(
            "Tridiagonal Matrix Algorithm", font_size=32, color=BLUE
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)

        # Problem statement
        problem = Text(
            "Resuelve sistemas lineales tridiagonales Ax = d", font_size=28, color=WHITE
        ).shift(DOWN * 2)

        self.play(Write(problem))
        self.wait(2)


class TridiagonalMatrix(Scene):
    """Show the structure of a tridiagonal matrix"""

    def construct(self):
        title = Title("Matriz Tridiagonal Ax = d", include_underline=True)
        self.add(title)

        # Create a tridiagonal matrix
        matrix_data = [
            [r"b_1", r"c_1", "0", r"\cdots", "0"],
            [r"a_2", r"b_2", r"c_2", "0", r"\vdots"],
            ["0", r"a_3", r"b_3", r"c_3", "0"],
            [r"\vdots", "0", r"\ddots", r"\ddots", r"\vdots"],
            ["0", r"\cdots", "0", r"a_n", r"b_n"],
        ]

        A = Matrix(matrix_data, h_buff=0.8, v_buff=0.8, element_alignment_corner=ORIGIN)

        # Create vectors
        x_data = [[r"x_1"], [r"x_2"], [r"x_3"], [r"\vdots"], [r"x_n"]]
        d_data = [[r"d_1"], [r"d_2"], [r"d_3"], [r"\vdots"], [r"d_n"]]

        x = Matrix(x_data, h_buff=0.6, v_buff=0.8)
        d = Matrix(d_data, h_buff=0.6, v_buff=0.8)

        # Arrange matrices
        group = VGroup(A, x, d)
        group.arrange(RIGHT, buff=0.5)

        # Add equal sign and equals vector
        eq1 = Text("=", font_size=40).move_to(A.get_right() + RIGHT * 0.3)
        eq2 = Text("=", font_size=40).next_to(x, RIGHT, buff=0.3)

        equation = VGroup(A, eq1, x, eq2, d)
        equation.center()

        self.play(Write(A))
        self.wait(1)
        self.play(Write(x), Write(eq1))
        self.wait(1)
        self.play(Write(d), Write(eq2))
        self.wait(2)

        # Highlight diagonal structure
        highlight_text = Text(
            "Solo 3 diagonales no-nulas: superior, principal, inferior",
            font_size=24,
            color=YELLOW,
        ).next_to(equation, DOWN, buff=1)

        self.play(Write(highlight_text))
        self.wait(2)


class ForwardElimination(Scene):
    """Forward elimination process"""

    def construct(self):
        title = Title("Paso 1: Eliminación Hacia Adelante", include_underline=True)
        self.add(title)

        # Step 1: First row
        step1_title = (
            Text("Fila 1:", font_size=28, color=BLUE)
            .to_edge(LEFT, buff=0.5)
            .shift(UP * 2)
        )
        self.add(step1_title)

        eq1 = MathTex(r"b_1 x_1 + c_1 x_2 = d_1").next_to(step1_title, DOWN, buff=0.3)
        eq1_norm = MathTex(r"x_1 + \frac{c_1}{b_1} x_2 = \frac{d_1}{b_1}").next_to(
            eq1, DOWN, buff=0.3
        )

        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq1_norm))
        self.wait(1)

        # Define c'_1 and d'_1
        defs1 = (
            VGroup(
                MathTex(r"c'_1 = \frac{c_1}{b_1}"), MathTex(r"d'_1 = \frac{d_1}{b_1}")
            )
            .arrange(DOWN, buff=0.2)
            .next_to(eq1_norm, DOWN, buff=0.3)
        )

        self.play(Write(defs1))
        self.wait(1)

        result1 = MathTex(r"x_1 + c'_1 x_2 = d'_1").next_to(defs1, DOWN, buff=0.3)
        self.play(Write(result1))
        self.wait(2)

        # Step 2: Second row
        step2_title = Text("Fila 2:", font_size=28, color=BLUE).next_to(
            result1, DOWN, buff=0.8
        )
        self.add(step2_title)

        eq2 = MathTex(r"a_2 x_1 + b_2 x_2 + c_2 x_3 = d_2").next_to(
            step2_title, DOWN, buff=0.3
        )
        self.play(Write(eq2))
        self.wait(1)

        # Elimination
        elim_text = Text(
            "Elimina x₁ usando la fila 1:", font_size=20, color=YELLOW
        ).next_to(eq2, DOWN, buff=0.3)
        self.play(Write(elim_text))
        self.wait(1)

        eq2_new = MathTex(r"(b_2 - a_2 c'_1) x_2 + c_2 x_3 = d_2 - a_2 d'_1").next_to(
            elim_text, DOWN, buff=0.3
        )
        self.play(Write(eq2_new))
        self.wait(1)

        # Define c'_2 and d'_2
        defs2 = (
            VGroup(
                MathTex(r"c'_2 = \frac{c_2}{b_2 - a_2 c'_1}"),
                MathTex(r"d'_2 = \frac{d_2 - a_2 d'_1}{b_2 - a_2 c'_1}"),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(eq2_new, DOWN, buff=0.3)
        )

        self.play(Write(defs2))
        self.wait(1)

        self.wait(2)


class RecurrenceFormulas(Scene):
    """Show the recurrence formulas"""

    def construct(self):
        title = Title("Fórmulas de Recurrencia", include_underline=True)
        self.add(title)

        # Forward elimination formulas
        forward_title = Text(
            "Eliminación hacia adelante:", font_size=26, color=BLUE
        ).to_edge(UP, buff=0.5)
        self.add(forward_title)

        formulas1 = (
            VGroup(
                MathTex(r"c'_1 = \frac{c_1}{b_1}, \quad d'_1 = \frac{d_1}{b_1}"),
                MathTex(
                    r"c'_i = \frac{c_i}{b_i - a_i c'_{i-1}}, \quad d'_i = \frac{d_i - a_i d'_{i-1}}{b_i - a_i c'_{i-1}}"
                ),
                MathTex(r"i = 2, 3, \ldots, n"),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(forward_title, DOWN, buff=0.5)
        )

        for formula in formulas1:
            self.play(Write(formula))
            self.wait(0.5)

        self.wait(1)

        # Back substitution formulas
        backward_title = Text(
            "Sustitución hacia atrás:", font_size=26, color=BLUE
        ).next_to(formulas1, DOWN, buff=0.8)
        self.play(Write(backward_title))

        formulas2 = (
            VGroup(
                MathTex(r"x_n = d'_n"),
                MathTex(r"x_i = d'_i - c'_i x_{i+1}, \quad i = n-1, n-2, \ldots, 1"),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(backward_title, DOWN, buff=0.5)
        )

        for formula in formulas2:
            self.play(Write(formula))
            self.wait(0.5)

        self.wait(2)


class UpperTriangularForm(Scene):
    """Show the resulting upper triangular form"""

    def construct(self):
        title = Title("Forma Triangular Superior Ux = d'", include_underline=True)
        self.add(title)

        # Create upper triangular matrix
        matrix_data = [
            ["1", r"c'_1", "0", r"\cdots", "0"],
            ["0", "1", r"c'_2", "0", r"\vdots"],
            ["0", "0", "1", r"c'_3", "0"],
            [r"\vdots", "0", r"\ddots", r"\ddots", r"\vdots"],
            ["0", r"\cdots", "0", "0", "1"],
        ]

        U = Matrix(matrix_data, h_buff=0.8, v_buff=0.8)

        # Create vectors
        x_data = [[r"x_1"], [r"x_2"], [r"x_3"], [r"\vdots"], [r"x_n"]]
        d_data = [[r"d'_1"], [r"d'_2"], [r"d'_3"], [r"\vdots"], [r"d'_n"]]

        x = Matrix(x_data, h_buff=0.6, v_buff=0.8)
        d = Matrix(d_data, h_buff=0.6, v_buff=0.8)

        eq1 = Text("=", font_size=40)
        eq2 = Text("=", font_size=40)

        equation = VGroup(U, eq1, x, eq2, d)
        equation.arrange(RIGHT, buff=0.3)
        equation.center()

        self.play(Write(U))
        self.wait(0.5)
        self.play(Write(eq1), Write(x))
        self.wait(0.5)
        self.play(Write(eq2), Write(d))
        self.wait(2)

        # Highlight features
        features = (
            VGroup(
                Text("✓ Diagonal principal: todos 1's", font_size=20, color=GREEN),
                Text("✓ Diagonal superior: c'ᵢ", font_size=20, color=GREEN),
                Text("✓ Diagonal inferior: todos 0's", font_size=20, color=GREEN),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(equation, DOWN, buff=1)
        )

        for feature in features:
            self.play(Write(feature))
            self.wait(0.3)

        self.wait(2)


class NumericalExample(Scene):
    """Numerical example with 3x3 system"""

    def construct(self):
        title = Title("Ejemplo Numérico (3×3)", include_underline=True)
        self.add(title)

        # System
        system_text = Text("Sistema original:", font_size=24, color=BLUE).to_edge(
            UP, buff=0.5
        )
        self.add(system_text)

        # Simple 3x3 tridiagonal system
        system = (
            VGroup(
                MathTex(r"2x_1 + 1x_2 = 5"),
                MathTex(r"1x_1 + 2x_2 + 1x_3 = 6"),
                MathTex(r"1x_2 + 2x_3 = 5"),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(system_text, DOWN, buff=0.3)
        )

        self.play(Write(system))
        self.wait(2)

        # Forward elimination
        forward_text = Text(
            "Eliminación hacia adelante:", font_size=24, color=BLUE
        ).next_to(system, DOWN, buff=0.8)
        self.play(Write(forward_text))
        self.wait(0.5)

        # Step 1
        step1 = Text("Fila 1 / b₁ = 2:", font_size=20, color=YELLOW).next_to(
            forward_text, DOWN, buff=0.3
        )
        step1_eq = MathTex(r"x_1 + 0.5x_2 = 2.5").next_to(step1, RIGHT, buff=0.3)
        self.play(Write(step1), Write(step1_eq))
        self.wait(1)

        # Step 2
        step2 = Text("Elimina x₁ de fila 2:", font_size=20, color=YELLOW).next_to(
            step1, DOWN, buff=0.3
        )
        step2_eq = MathTex(r"1.5x_2 + 1x_3 = 3.5").next_to(step2, RIGHT, buff=0.3)
        self.play(Write(step2), Write(step2_eq))
        self.wait(1)

        # Step 3
        step3 = Text("Divide por 1.5:", font_size=20, color=YELLOW).next_to(
            step2, DOWN, buff=0.3
        )
        step3_eq = MathTex(r"x_2 + 0.667x_3 = 2.333").next_to(step3, RIGHT, buff=0.3)
        self.play(Write(step3), Write(step3_eq))
        self.wait(1)

        # Back substitution
        back_text = Text("Sustitución hacia atrás:", font_size=24, color=BLUE).next_to(
            step3, DOWN, buff=0.8
        )
        self.play(Write(back_text))
        self.wait(0.5)

        back_steps = (
            VGroup(
                MathTex(r"x_3 = 2.333"),
                MathTex(r"x_2 = 2.333 - 0.667(2.333) = 1"),
                MathTex(r"x_1 = 2.5 - 0.5(1) = 2"),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(back_text, DOWN, buff=0.3)
        )

        for step in back_steps:
            self.play(Write(step))
            self.wait(0.5)

        # Solution
        solution = Text(
            "Solución: x = [2, 1, 2.333]ᵀ", font_size=22, color=GREEN
        ).next_to(back_steps, DOWN, buff=0.5)
        self.play(Write(solution))
        self.wait(2)


class AlgorithmSummary(Scene):
    """Algorithm summary and complexity"""

    def construct(self):
        title = Title("Resumen del Algoritmo de Thomas", include_underline=True)
        self.add(title)

        # Two phases
        phase1_title = (
            Text("Fase 1: Eliminación", font_size=26, color=BLUE)
            .to_edge(LEFT, buff=0.5)
            .shift(UP * 1)
        )
        self.play(Write(phase1_title))

        phase1_steps = (
            VGroup(
                MathTex(r"c'_1 = \frac{c_1}{b_1}, \quad d'_1 = \frac{d_1}{b_1}"),
                MathTex(r"c'_i = \frac{c_i}{b_i - a_i c'_{i-1}}"),
                MathTex(r"d'_i = \frac{d_i - a_i d'_{i-1}}{b_i - a_i c'_{i-1}}"),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(phase1_title, DOWN, buff=0.3)
        )

        self.play(Write(phase1_steps))
        self.wait(1)

        phase2_title = (
            Text("Fase 2: Sustitución", font_size=26, color=BLUE)
            .to_edge(RIGHT, buff=0.5)
            .shift(UP * 1)
        )
        self.play(Write(phase2_title))

        phase2_steps = (
            VGroup(
                MathTex(r"x_n = d'_n"),
                MathTex(r"x_i = d'_i - c'_i x_{i+1}"),
                MathTex(r"i = n-1, n-2, \ldots, 1"),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(phase2_title, DOWN, buff=0.3)
        )

        self.play(Write(phase2_steps))
        self.wait(2)

        # Complexity
        complexity = (
            VGroup(
                Text("Complejidad: O(n)", font_size=24, color=YELLOW),
                Text(
                    "vs O(n³) para eliminación gaussiana general",
                    font_size=20,
                    color=WHITE,
                ),
            )
            .arrange(DOWN, buff=0.3)
            .shift(DOWN * 3)
        )

        self.play(Write(complexity[0]))
        self.wait(0.5)
        self.play(Write(complexity[1]))
        self.wait(2)

        # Applications
        apps_title = Text("Aplicaciones:", font_size=22, color=BLUE).next_to(
            complexity, DOWN, buff=1
        )
        self.play(Write(apps_title))

        apps = (
            VGroup(
                Text(
                    "• Ecuaciones diferenciales (splines, diferencias finitas)",
                    font_size=18,
                ),
                Text("• Problemas de flujo de calor", font_size=18),
                Text("• Dinámica de fluidos", font_size=18),
                Text("• Análisis estructural", font_size=18),
            )
            .arrange(DOWN, buff=0.2)
            .next_to(apps_title, DOWN, buff=0.2)
        )

        self.play(Write(apps))
        self.wait(3)


class CompleteScene(Scene):
    """Complete overview scene"""

    def construct(self):
        # Create a flowchart-like representation
        title = Title("Flujo del Algoritmo de Thomas", include_underline=True)
        self.add(title)

        # Input
        input_box = RoundedRectangle(width=3, height=0.6, color=BLUE).shift(UP * 3)
        input_text = Text("Sistema Ax = d", font_size=16, color=BLACK).move_to(
            input_box
        )
        input_group = VGroup(input_box, input_text)

        self.play(Write(input_group))

        # Arrow down
        arrow1 = Arrow(input_box.get_bottom(), DOWN, color=WHITE, buff=0.3).shift(
            UP * 1.5
        )
        self.play(Write(arrow1))

        # Forward elimination
        forward_box = RoundedRectangle(width=4, height=0.6, color=GREEN).shift(UP * 0.5)
        forward_text = Text("Eliminación (c', d')", font_size=16, color=BLACK).move_to(
            forward_box
        )
        forward_group = VGroup(forward_box, forward_text)

        self.play(Write(forward_group))

        # Arrow down
        arrow2 = Arrow(forward_box.get_bottom(), DOWN, color=WHITE, buff=0.3).shift(
            UP * 0.2
        )
        self.play(Write(arrow2))

        # Upper triangular
        upper_box = RoundedRectangle(width=4, height=0.6, color=YELLOW).shift(
            DOWN * 1.2
        )
        upper_text = Text("Forma Ux = d'", font_size=16, color=BLACK).move_to(upper_box)
        upper_group = VGroup(upper_box, upper_text)

        self.play(Write(upper_group))

        # Arrow down
        arrow3 = Arrow(upper_box.get_bottom(), DOWN, color=WHITE, buff=0.3).shift(
            DOWN * 0.8
        )
        self.play(Write(arrow3))

        # Back substitution
        back_box = RoundedRectangle(width=4, height=0.6, color=GREEN).shift(DOWN * 2.9)
        back_text = Text("Sustitución hacia atrás", font_size=16, color=BLACK).move_to(
            back_box
        )
        back_group = VGroup(back_box, back_text)

        self.play(Write(back_group))

        # Arrow down
        arrow4 = Arrow(back_box.get_bottom(), DOWN, color=WHITE, buff=0.3).shift(
            DOWN * 2.6
        )
        self.play(Write(arrow4))

        # Output
        output_box = RoundedRectangle(width=3, height=0.6, color=RED).shift(DOWN * 4.3)
        output_text = Text("Solución x", font_size=16, color=BLACK).move_to(output_box)
        output_group = VGroup(output_box, output_text)

        self.play(Write(output_group))

        self.wait(2)


# Main execution
if __name__ == "__main__":
    import sys
    from pathlib import Path

    # Get the script directory
    script_dir = Path(__file__).parent
    output_dir = script_dir / "animations"
    output_dir.mkdir(exist_ok=True)

    print(f"Creating animations in {output_dir}")

    scenes = [
        ThomasAlgorithmIntro,
        TridiagonalMatrix,
        ForwardElimination,
        RecurrenceFormulas,
        UpperTriangularForm,
        NumericalExample,
        AlgorithmSummary,
        CompleteScene,
    ]

    for scene_class in scenes:
        print(f"Rendering {scene_class.__name__}...")
