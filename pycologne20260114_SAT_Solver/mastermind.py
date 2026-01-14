import colorsys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pefs

PEG_COLORS = mpl.colormaps["tab10"].colors


def _generate_color(i, total):
    if total <= 1:
        return '#FF0000'
    hue = (i - 1) / total
    rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
    return f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}'


def score(guess, code, n_colors):
    g, c = np.array(guess), np.array(code)
    assert all(g > 0) and all(g <= n_colors)
    black = (g == c).sum().item()
    guess_count = np.bincount(g, minlength=n_colors + 1)
    code_count = np.bincount(c, minlength=n_colors + 1)
    white = np.minimum(guess_count, code_count).sum() - black
    return black, white.item()


class Game:
    def __init__(self, n_pegs=5, n_colors=8):
        self.n_pegs = n_pegs
        self.n_colors = n_colors
        self.guesses = []
        self._code = np.random.choice(n_colors, n_pegs, replace=True) + 1
        
    def guess(self, g):
        g = list(g)
        assert len(g) == self.n_pegs
        black_pegs, white_pegs = score(g, self._code, self.n_colors)
        self.guesses.append((g.copy(), black_pegs, white_pegs))
        return black_pegs, white_pegs

    def display(self):
        n_rows = max(7, len(self.guesses) + 1)
        
        # Set up the figure
        fig, ax = plt.subplots(figsize=(10, 8))
        
        peg_radius = 0.25
        row_height = peg_radius * 3
        col_width = peg_radius * 3
        feedback_peg_radius = 0.15        
        feedback_area_height = 2 * feedback_peg_radius + 0.2
        feedback_area_width = 4 * feedback_peg_radius + 0.3
        # Draw the board background
        board_width = self.n_pegs * col_width + feedback_area_width + 0.1 + 0.2 + 0.1
        board_height = n_rows * row_height + 0.2
        
        board_rect = patches.Rectangle((0, 0), board_width, board_height, 
                                    linewidth=2, edgecolor="black",
                                    facecolor="#e7c496")
        ax.add_patch(board_rect)
        
        for row in range(n_rows):
            y_pos = board_height - (row + .5) * row_height - 0.1            
            
            try:
                guess, black_pegs, white_pegs = self.guesses[row]
            except:
                guess, black_pegs, white_pegs = [], -1, -1
            for col in range(self.n_pegs):
                x_pos = col * col_width + col_width/2 + 0.1
                                
                hole = patches.Circle((x_pos, y_pos), peg_radius + 0.02, 
                                    facecolor="darkgray", edgecolor="black")
                ax.add_patch(hole)
                try:                    
                    color = guess[col] # Fails with IndexError if no quess for this row
                    peg = patches.Circle((x_pos, y_pos), peg_radius, facecolor=PEG_COLORS[color - 1], edgecolor="black", linewidth=2)
                    ax.add_patch(peg)
                    label = ax.text(x_pos, y_pos, str(color), ha="center", va="center", fontsize=12, fontweight="bold", color="white")
                    label.set_path_effects([pefs.Stroke(linewidth=2, foreground="black"), pefs.Normal()])
                except IndexError:
                    pass
                
            feedback_area_x = self.n_pegs * col_width + 0.2
            feedback_bg = patches.Rectangle((feedback_area_x, y_pos - feedback_peg_radius - 0.1), 
                                             feedback_area_width, feedback_area_height,
                                             facecolor="#ddd", edgecolor="black", linewidth=1)
            ax.add_patch(feedback_bg)
            
            black_peg_x = feedback_area_x + 0.1 + feedback_peg_radius
            white_peg_x = black_peg_x + 2 * feedback_peg_radius + 0.1
            black_peg_y = y_pos
            black_peg = patches.Circle((black_peg_x, black_peg_y), feedback_peg_radius, 
                                         facecolor="black", edgecolor="gray")
            ax.add_patch(black_peg)
            white_peg = patches.Circle((white_peg_x, black_peg_y), feedback_peg_radius, 
                                        facecolor="white", edgecolor="black")
            ax.add_patch(white_peg)
            if black_pegs >= 0:
                ax.text(black_peg_x, black_peg_y, str(black_pegs), ha="center", va="center", fontsize=10, fontweight="bold", color="white")                     
            if white_pegs >= 0:
                ax.text(white_peg_x, black_peg_y, str(white_pegs), ha="center", va="center", fontsize=10, fontweight="bold", color="black")                     
            
            # font_size = max(8, int(feedback_peg_radius * 20))
            # ax.text(black_peg_x, black_peg_y, str(black_pegs), 
            #             ha='center', va='center', fontsize=font_size, 
            #             fontweight='bold', color='white')
            ax.text(-0.25, y_pos, f'{row+1}', ha="center", va="center", fontsize=12, fontweight="bold")
        
        # Set axis properties with dynamic scaling
        fig_width = board_width + 0.5
        fig_height = board_height
        fig.set_size_inches(fig_width, fig_height)
        
        ax.set_xlim(-1, board_width)
        ax.set_ylim(0, board_height)
        ax.set_aspect("equal")
        ax.axis("off")
        plt.tight_layout()
        plt.show()
