#!python3
import numpy as np

class Data(object):
    def __init__(label, features):
        self.label = label
        self.features = features


class KMeans(object):
    def __init__(self, k: int):
        self.k = k

    def fit(self, data: np.ndarray):
        center_points = data[self.k,]
        for center_point in center_points:
            flag = True
            new_center_point = center_point
            distance = []
            for point in data:
                vec = new_center_point - point
                distance.append(vec)
            distance.sort(key=np.linalg.norm)
            group = distance[:len(distance) // self.k]
            
            move = np.array(group).mean(axis=0)
            new_center_point = new_center_point + move
            print(f"Center: {new_center_point}, Move: {move}")
            if (np.linalg.norm(move) <= 0.0001):
                flag = False

def main():
    data = []
    km = KMeans(2)
    with open("aout.txt") as f:
        for line in f.readlines():
            data.append(line.rstrip("\n").split(","))
    
    data = np.array(data, dtype=np.float)

    try:
        km.fit(data)
    except KeyboardInterrupt:
        print("end")

if __name__ == '__main__':
    main()
