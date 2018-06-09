from matplotlib import pyplot as plt

def d_color(x: list, y: list) -> (list, list, list, list):
    ax, ay, bx, by = [], [], [], []
    for xi, yi in zip(x, y):
        if yi > 1 - xi:
            ax.append(xi)
            ay.append(yi)
        if yi < 1 - xi:
            bx.append(xi)
            by.append(yi)
    return ax, ay, bx, by


def main():
    x = []
    y = []
    with open("aout.txt") as target:
        for i in target.readlines():
            g = i.split(",")
            x.append(float(g[0]))
            y.append(float(g[1]))
    
    reg_x = [1, 0]
    reg_y = [0, 1]
    plt.plot(reg_x, reg_y)
    ax, ay, bx, by = d_color(x, y)
    plt.scatter(ax, ay, c="r")
    plt.scatter(bx, by, c="g")
    plt.show()

if __name__ == '__main__':
    main()
