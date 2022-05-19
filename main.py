import sys, pygame, random

pygame.init()


class Application:
    res = 1000, 500

    # color palette
    BG = 245, 245, 245
    C1 = 224, 243, 219
    C2 = 168, 221, 181
    C3 = 67, 162, 202
    COLORS = [C1, C2, C3]

    def __init__(self, res):
        self.width = res[0]
        self.height = res[1]

    def generate_data(self, n, min, max):
        data = []
        for _ in range(n):
            data.append(random.randint(min, max))
        return data

    def init_data(self, data):
        side_padding = 5 * (self.width / len(data))
        top_padding = self.height / 5
        begin = side_padding

        self.min = min(data)
        self.max = max(data)
        bar_width = (self.width - side_padding * 2) // len(data)
        max_bar_height = self.height - top_padding

        # initialize window
        window = pygame.display.set_mode(self.res)
        pygame.display.set_caption("Sorting Visualizer")
        window.fill(self.BG)
        pygame.display.update()

        # iterate through data and determine coordinates
        for i, val in enumerate(data):
            bar_height = round((self.height - top_padding) / (self.max - self.min))
            x = begin + i * bar_width
            y = self.height - (val * bar_height)
            bar_color = self.COLORS[i % 3]

            # draw data
            pygame.draw.rect(window, bar_color, (x, y, bar_width, self.height))
            # bar borders (WIP)
            # pygame.draw.line(window, BLACK)


def main():
    run = True
    res = 1000, 500

    n = 100
    min = 0
    max = 100

    app = Application(res)
    data = app.generate_data(n, min, max)
    app.init_data(data)

    # main loop
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                data = app.generate_data(n, min, max)
                app.init_data(data)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
