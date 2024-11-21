import pandas as pd
import numpy as np

def calculate_entropy(probabilities):
    probabilities = probabilities[probabilities > 0]
    return -np.sum(probabilities * np.log2(probabilities))

def main():
    data = pd.read_csv('условная-энтропия-данные.csv', index_col=0).to_numpy()

    total_sum = data.sum()
    joint_probabilities = data / total_sum

    marginal_a = joint_probabilities.sum(axis=1)
    marginal_b = joint_probabilities.sum(axis=0)

    h_ab = calculate_entropy(joint_probabilities.flatten())
    h_a = calculate_entropy(marginal_a)
    h_b = calculate_entropy(marginal_b)

    ha_b = h_ab - h_a

    i_a_b = h_b - ha_b

    return [round(h_ab, 2), round(h_a, 2), round(h_b, 2), round(ha_b, 2), round(i_a_b, 2)]

if __name__ == "__main__":
    result = main()
    print(result)
