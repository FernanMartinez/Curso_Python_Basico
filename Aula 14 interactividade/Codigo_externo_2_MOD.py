import numpy as np
import matplotlib.pyplot as plt
y = np.random.rand(1000)
x = np.arange(0, len(y))
plt.scatter(x=x,
            y=y,
            s=np.random.uniform(low=1, high=50, size=len(x)),
            c=np.random.uniform(low=1, high=10, size=len(x)),marker="*",
            alpha=0.8)
plt.title("Scarter plot")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
